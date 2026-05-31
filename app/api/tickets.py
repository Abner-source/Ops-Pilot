from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.ticket import TicketCreate, TicketResponse
from app.services.ticket_service import create_ticket, get_ticket
from app.api.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.post("", response_model=TicketResponse)
def submit_ticket(
    data: TicketCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    ticket = create_ticket(db, data, current_user.id)
    return ticket


@router.get("/{ticket_id}", response_model=TicketResponse)
def fetch_ticket(
    ticket_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    ticket = get_ticket(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket