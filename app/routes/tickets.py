from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.ticket import TicketCreation , TicketUpdate
from app.utils.jwt_handler import decode_access_token
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


router = APIRouter(prefix='/tickets')
security = HTTPBearer()

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
    return {
        'success' : True,
        'data' : {
            'title': ticket.title,
            'created_by':user['username']
            },
        'message' : 'Ticket created successfully'        
    }

@router.get('')
def get_tickets(user = Depends[get_current_user]):
    return {
        'success' : True,
        'data' : [],
        'message' : 'Ticket Fetched Successfully'
    }
    
@router.get('/{ticket_id}')
def get_ticket_by_id(ticket_id : int, user = Depends(get_current_user)):
    return {
        'success' : True,
        'data' : {
            'ticket_id' : ticket_id
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
        
    return {
        'success' : True,
        'data' : {
            'ticket_id' : ticket_id,
            'status' : ticket.status
        },
        'message':'Ticket updated Successfully'
    }