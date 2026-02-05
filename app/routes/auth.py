from fastapi import APIRouter
from app.schemas.user import UserLogin

router = APIRouter()

@router.get('/login')
def login(user : UserLogin):
    return{
        'success' : True,
        'data' : {
            'token' : 'dummy-token'
        },
        'message':'Successfully Logged in' 
    }
    