from pydantic import BaseModel, Field

class TicketCreation(BaseModel):
    title : str = Field(...,min_length=3)
    description : str = Field(...,min_length=5)
    priority : str
    

class TicketUpdate(BaseModel):
    status : str
    