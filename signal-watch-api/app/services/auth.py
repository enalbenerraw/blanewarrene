"""Authentication core: one-time passcode issuance/verification and JWTs.

Email-OTP (magic link) flow:
  1. request_otp(email)  -> generates a code, stores it hashed with an expiry,
                            and emails it (or logs it in dev).
  2. verify_otp(email, code) -> validates the code, marks it consumed, and
                            returns the matching User (creating one on first
                            sign-in). The caller mints a JWT from the user id.
"""

import secrets
from datetime import datetime, timedelta, timezone

from jose import jwt, JWTError
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import get_settings
from app.models.database import User, OtpCode

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def _generate_code(length: int) -> str:
    """Return a zero-padded numeric passcode of the given length."""
    upper = 10 ** length
    return str(secrets.randbelow(upper)).zfill(length)


async def request_otp(db: AsyncSession, email: str) -> None:
    """Issue a fresh passcode for the email and deliver it.

    Deliberately reveals nothing about whether the email maps to an existing
    account; callers should always respond with a generic success message.
    """
    # Imported here to avoid a circular import at module load.
    from app.services.email import send_otp_email

    settings = get_settings()
    email = email.strip().lower()
    code = _generate_code(settings.otp_length)
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=settings.otp_expiration_minutes)

    db.add(
        OtpCode(
            email=email,
            code_hash=pwd_context.hash(code),
            expires_at=expires_at,
            consumed=False,
        )
    )
    await db.commit()

    await send_otp_email(email, code)


async def verify_otp(db: AsyncSession, email: str, code: str) -> User | None:
    """Validate a passcode. On success, consume it and return the user.

    Returns None if no live, matching, unconsumed code exists.
    """
    email = email.strip().lower()
    now = datetime.now(timezone.utc)

    result = await db.execute(
        select(OtpCode)
        .where(OtpCode.email == email, OtpCode.consumed == False)  # noqa: E712
        .order_by(OtpCode.created_at.desc())
    )
    candidates = result.scalars().all()

    matched = None
    for otp in candidates:
        if _expired(otp.expires_at, now):
            continue
        if pwd_context.verify(code, otp.code_hash):
            matched = otp
            break

    if matched is None:
        return None

    matched.consumed = True
    user = await _get_or_create_user(db, email)
    await db.commit()
    return user


def _expired(expires_at: datetime, now: datetime) -> bool:
    """Compare timezone-aware now against expires_at, tolerating naive storage."""
    if expires_at.tzinfo is None:
        expires_at = expires_at.replace(tzinfo=timezone.utc)
    return expires_at < now


async def _get_or_create_user(db: AsyncSession, email: str) -> User:
    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    if user is None:
        user = User(email=email)
        db.add(user)
        await db.flush()
    return user


def create_access_token(user_id: str) -> tuple[str, datetime]:
    """Mint a JWT for the user. Returns (token, expires_at)."""
    settings = get_settings()
    expires = datetime.now(timezone.utc) + timedelta(minutes=settings.jwt_expiration_minutes)
    payload = {"sub": user_id, "exp": expires}
    token = jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)
    return token, expires


def decode_access_token(token: str) -> str | None:
    """Return the user id from a valid JWT, or None if invalid/expired."""
    settings = get_settings()
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
    except JWTError:
        return None
    return payload.get("sub")
