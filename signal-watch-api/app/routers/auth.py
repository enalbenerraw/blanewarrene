"""Email one-time-passcode authentication.

Two steps:
  POST /auth/request  {email}        -> emails a passcode (generic 200)
  POST /auth/verify   {email, code}  -> returns a JWT on success
"""

from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.database import get_db
from app.services.auth import request_otp, verify_otp, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])


class OtpRequest(BaseModel):
    email: EmailStr


class OtpVerify(BaseModel):
    email: EmailStr
    code: str


class RequestResponse(BaseModel):
    message: str


class TokenResponse(BaseModel):
    token: str
    expires_at: datetime


@router.post("/request", response_model=RequestResponse)
async def request_code(req: OtpRequest, db: AsyncSession = Depends(get_db)):
    """Send a one-time passcode to the email. Always returns the same message
    regardless of whether the address has an account (no enumeration)."""
    await request_otp(db, req.email)
    return RequestResponse(message="If that email is valid, a sign-in code is on its way.")


@router.post("/verify", response_model=TokenResponse)
async def verify_code(req: OtpVerify, db: AsyncSession = Depends(get_db)):
    """Exchange a valid passcode for a JWT."""
    user = await verify_otp(db, req.email, req.code)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired code",
        )
    token, expires_at = create_access_token(user.id)
    return TokenResponse(token=token, expires_at=expires_at)
