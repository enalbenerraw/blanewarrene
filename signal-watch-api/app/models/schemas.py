from pydantic import BaseModel, HttpUrl
from datetime import datetime
from enum import Enum


class BriefingStatus(str, Enum):
    pending = "pending"
    running = "running"
    completed = "completed"
    failed = "failed"


class BriefingRequest(BaseModel):
    company_name: str
    company_url: HttpUrl
    time_period: str = "6 months"


class BriefingResponse(BaseModel):
    id: str
    status: BriefingStatus
    company_name: str
    company_url: str
    created_at: datetime
    content: str | None = None


class BriefingListItem(BaseModel):
    id: str
    company_name: str
    status: BriefingStatus
    created_at: datetime
