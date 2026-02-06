from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.ticket import TicketCreation , TicketUpdate
from app.utils.jwt_handler import decode_access_token
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


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

@router.post('')
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
    ticket_counter = ticket_counter+1
    
    return {
        'success' : True,
        'data' : new_ticket,
        'message' : 'Ticket created successfully'        
    }

@router.get('')
def get_tickets(user = Depends(get_current_user)):
    if user['role'] == 'support':
        visible_ticket = TICKETS
    else:
        visible_ticket = [
            ticket for ticket in TICKETS
            if ticket['created_by'] == user['username']
        ]
        
    return {
        'success' : True,
        'data' : visible_ticket,
        'message' : 'Ticket Fetched Successfully'
    }
    
@router.get('/{ticket_id}')
def get_ticket_by_id(ticket_id : int, user = Depends(get_current_user)):
    visible_ticket = [
            ticket for ticket in TICKETS
            if ticket['created_by'] == user['username']
        ]
    return {
        'success' : True,
        'data' : {
            'data' : visible_ticket
            },
        'message' : 'Ticket Fetched Successfully'
    }
    
@router.put('/{ticket_id}')
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
    
    for t in TICKETS:
        if t['id'] == ticket_id:
            t['status'] == ticket.status
        
            return {
                'success' : True,
                'data' : t,
                'message':'Ticket updated Successfully'
            }
    
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail='Ticket not found'
    )