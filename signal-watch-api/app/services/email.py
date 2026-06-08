"""Email transport for one-time passcodes.

When SMTP is configured (smtp_host set), passcodes are delivered over SMTP.
Otherwise they are written to the application log so the auth flow is fully
testable in development without an email provider.
"""

import asyncio
import logging
import smtplib
from email.message import EmailMessage

from app.config import get_settings

logger = logging.getLogger("signalwatch.email")


async def send_otp_email(to_email: str, code: str) -> None:
    """Send a passcode to the given address, or log it in dev mode."""
    settings = get_settings()
    subject = "Your Signal Watch sign-in code"
    body = (
        f"Your Signal Watch sign-in code is: {code}\n\n"
        f"It expires in {settings.otp_expiration_minutes} minutes. "
        "If you did not request this, you can ignore this email."
    )

    if not settings.smtp_host:
        # Dev mode: no provider configured, so surface the code in the log.
        logger.warning("OTP for %s: %s (no SMTP configured, dev mode)", to_email, code)
        return

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = settings.smtp_from
    msg["To"] = to_email
    msg.set_content(body)

    # smtplib is blocking; run it off the event loop.
    await asyncio.to_thread(_send_smtp, msg)


def _send_smtp(msg: EmailMessage) -> None:
    settings = get_settings()
    with smtplib.SMTP(settings.smtp_host, settings.smtp_port, timeout=15) as server:
        if settings.smtp_use_tls:
            server.starttls()
        if settings.smtp_username and settings.smtp_password:
            server.login(settings.smtp_username, settings.smtp_password)
        server.send_message(msg)
