"""Minimal auth stub — replace with full implementation before production."""

from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from jose import jwt

from app.config import get_settings

router = APIRouter(prefix="/auth", tags=["auth"])


class AuthRequest(BaseModel):
    email: str
    # In production: add password, OAuth, or Sign in with Apple


class AuthResponse(BaseModel):
    token: str
    expires_at: datetime


@router.post("/token", response_model=AuthResponse)
async def get_token(req: AuthRequest):
    """Issue a JWT. This is a stub — wire up real auth before shipping."""
    settings = get_settings()
    expires = datetime.now(timezone.utc) + timedelta(minutes=settings.jwt_expiration_minutes)
    payload = {
        "sub": req.email,
        "exp": expires,
    }
    token = jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)
    return AuthResponse(token=token, expires_at=expires)
