from fastapi import APIRouter
from app.schemas.ticket import TicketCreation , TicketUpdate


router = APIRouter(prefix='/tickets')

@router.post('')
def create_ticket(ticket_creation : TicketCreation):
    return {
        'success' : True,
        'data' : {},
        'message' : 'Ticket created successfully'        
    }

@router.get('')
def get_all_tickets():
    return {
        'success' : True,
        'data' : [],
        'message' : 'Ticket Fetched Successfully'
    }
    
@router.get('/{ticket_id}')
def get_ticket_by_id(ticket_id : int):
    return {
        'success' : True,
        'data' : {
            'ticket_id' : ticket_id
            },
        'message' : 'Ticket Fetched by id is Successfull'
    }
    
@router.put('/{ticket_id}')
def update_ticket(ticket_id : int, ticket_update : TicketUpdate):
    return {
        'success' : True,
        'data' : {
            'ticket_id' : ticket_id,
            'status' : 'In Progress'
        },
        'message':'Ticket updates Successfully'
    }