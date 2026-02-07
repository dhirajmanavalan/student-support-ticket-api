from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.ticket import TicketCreation , TicketUpdate, TicketResponse
from app.utils.jwt_handler import decode_access_token
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from app.utils.logger import logger

router = APIRouter(prefix='/tickets')
security = HTTPBearer()

TICKETS = []
ticket_counter = 1

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)):
    payload = decode_access_token(credentials.credentials)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    return payload

@router.post('', response_model=TicketResponse)
def create_ticket(ticket : TicketCreation, user = Depends(get_current_user)):
    global ticket_counter
    
    if ticket.priority not in ['Low','High','Medium']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Priority must be Low, Meidum, or High'
        )
        

    new_ticket = {
        "id": ticket_counter,
        "title": ticket.title,
        "description": ticket.description,
        "priority": ticket.priority,
        "status": "Open",
        "created_by": user["username"]
    }
    TICKETS.append(new_ticket)
    logger.info(f"Ticket created | user={user['username']} | ticket_id={ticket_counter}")
    
    ticket_counter = ticket_counter+1
    
    return new_ticket     

@router.get('', response_model=list[TicketResponse])
def get_tickets(user = Depends(get_current_user)):
    if user['role'] == 'support':
        return TICKETS
            
    return [
        t for t in TICKETS
        if t['created_by'] == user['username']
    ]
    
@router.get('/{ticket_id}')
def get_ticket_by_id(ticket_id : int, user = Depends(get_current_user)):
    for ticket in TICKETS:
        if ticket['id'] == ticket_id:
            return ticket
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='Ticket not found'
    )
    
@router.put('/{ticket_id}', response_model=TicketResponse)
def update_ticket(
    ticket_id : int,
    ticket : TicketUpdate,
    user = Depends(get_current_user)):
    
    if user["role"] != "support":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only support staff can update tickets"
        )
        
    if ticket.status not in ['Open', 'In Progress', 'Resolved']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Invalid status value'   
        )
        
    logger.info(f"Ticket updated | support={user['username']} | ticket_id={ticket_id} | status={ticket.status}")

    
    for t in TICKETS:
        if t['id'] == ticket_id:
            t['status'] = ticket.status
            logger.info(f"Ticket updated | support={user['username']} | ticket_id={ticket_id} | status={ticket.status}")
            return t
    
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail='Ticket not found'
    )