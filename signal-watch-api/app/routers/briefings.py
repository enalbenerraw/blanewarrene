"""Briefing endpoints — create, stream, list, and retrieve reports."""

import json
import uuid
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sse_starlette.sse import EventSourceResponse

from app.models.schemas import BriefingRequest, BriefingResponse, BriefingListItem
from app.models.database import Briefing, get_db
from app.services.agent import generate_briefing, generate_briefing_stream

router = APIRouter(prefix="/briefings", tags=["briefings"])

# Placeholder until auth is wired up
TEMP_USER_ID = "demo-user"


@router.post("", response_model=BriefingResponse)
async def create_briefing(req: BriefingRequest, db: AsyncSession = Depends(get_db)):
    """Create a briefing synchronously — returns the full report when done."""
    briefing = Briefing(
        id=str(uuid.uuid4()),
        user_id=TEMP_USER_ID,
        company_name=req.company_name,
        company_url=str(req.company_url),
        time_period=req.time_period,
        status="running",
    )
    db.add(briefing)
    await db.commit()

    try:
        content = await generate_briefing(
            company_name=req.company_name,
            company_url=str(req.company_url),
            time_period=req.time_period,
        )
        briefing.content = content
        briefing.status = "completed"
    except Exception as e:
        briefing.status = "failed"
        briefing.content = str(e)
    finally:
        await db.commit()
        await db.refresh(briefing)

    return _to_response(briefing)


@router.post("/stream")
async def create_briefing_stream(req: BriefingRequest, db: AsyncSession = Depends(get_db)):
    """Create a briefing with SSE streaming — the iOS app gets live progress updates."""
    briefing = Briefing(
        id=str(uuid.uuid4()),
        user_id=TEMP_USER_ID,
        company_name=req.company_name,
        company_url=str(req.company_url),
        time_period=req.time_period,
        status="running",
    )
    db.add(briefing)
    await db.commit()

    async def event_generator():
        full_content = []
        try:
            async for event in generate_briefing_stream(
                company_name=req.company_name,
                company_url=str(req.company_url),
                time_period=req.time_period,
            ):
                yield {"event": event["type"], "data": json.dumps(event)}
                if event["type"] == "content":
                    full_content.append(event["text"])

            briefing.content = "\n".join(full_content)
            briefing.status = "completed"
        except Exception as e:
            briefing.status = "failed"
            briefing.content = str(e)
            yield {"event": "error", "data": json.dumps({"error": str(e)})}
        finally:
            await db.commit()

    return EventSourceResponse(event_generator())


@router.get("", response_model=list[BriefingListItem])
async def list_briefings(db: AsyncSession = Depends(get_db)):
    """List all briefings for the current user."""
    result = await db.execute(
        select(Briefing)
        .where(Briefing.user_id == TEMP_USER_ID)
        .order_by(Briefing.created_at.desc())
    )
    briefings = result.scalars().all()
    return [
        BriefingListItem(
            id=b.id,
            company_name=b.company_name,
            status=b.status,
            created_at=b.created_at,
        )
        for b in briefings
    ]


@router.get("/{briefing_id}", response_model=BriefingResponse)
async def get_briefing(briefing_id: str, db: AsyncSession = Depends(get_db)):
    """Retrieve a specific briefing by ID."""
    result = await db.execute(select(Briefing).where(Briefing.id == briefing_id))
    briefing = result.scalar_one_or_none()
    if not briefing:
        raise HTTPException(status_code=404, detail="Briefing not found")
    return _to_response(briefing)


def _to_response(b: Briefing) -> BriefingResponse:
    return BriefingResponse(
        id=b.id,
        status=b.status,
        company_name=b.company_name,
        company_url=b.company_url,
        created_at=b.created_at,
        content=b.content,
    )
