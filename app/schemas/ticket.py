from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TicketCreate(BaseModel):
    title: str
    body: str


class TicketResponse(BaseModel):
    id: int
    title: str
    body: str
    status: str
    priority: Optional[str]
    department: Optional[str]
    created_by: Optional[int]
    created_at: datetime

    class Config:
        from_attributes = True