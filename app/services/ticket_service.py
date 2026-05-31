from sqlalchemy.orm import Session
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate


def create_ticket(db: Session, data: TicketCreate, user_id: int):
    ticket = Ticket(
        title=data.title,
        body=data.body,
        status="pending",
        created_by=user_id
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


def get_ticket(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()