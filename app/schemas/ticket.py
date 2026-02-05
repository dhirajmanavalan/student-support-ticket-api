from pydantic import BaseModel

class TicketCreation(BaseModel):
    title : str
    description : str
    priority : str
    

class TicketUpdate(BaseModel):
    status : str
    