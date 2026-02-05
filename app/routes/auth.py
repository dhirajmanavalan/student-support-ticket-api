from fastapi import APIRouter

router = APIRouter()

@router.get('/login')
def login():
    return{
        'success' : True,
        'data' : {
            'token' : 'dummy-token'
        },
        'message':'Successfully Logged in' 
    }
    