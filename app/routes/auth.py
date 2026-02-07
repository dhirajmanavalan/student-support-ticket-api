from fastapi import APIRouter, HTTPException , status
from app.schemas.user import UserLogin
from app.utils.jwt_handler import create_access_token

from app.utils.logger import logger

router = APIRouter()

# Temporary users DB
USERS = {
    "snakendran":{
        "password" : "snake@123",
        "role" : "support"
    },
    
    "nafisa" : {
        "password" : 'nafisa@123',
        "role" : 'support'
    },
    
    "dhirajkumar": {
        "password": "Dhiraj@123",
        "role": "student"
    },
    "rushikesh": {
        "password": "Rushi@123",
        "role": "student"
    },
    "brijesh": {
        "password": "Brijesh@123",
        "role": "student"
    },
    "dev": {
        "password": "Dev@123",
        "role": "student"
    },
    "sudharshan": {
        "password": "sudha@123",
        "role": "student"
    }
}


@router.post("/login")
def login(user: UserLogin):
    if user.username not in USERS:
        logger.warning(f"Login failed | username = {user.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid username or password'
        )    
        
        
    if user.password != USERS[user.username]["password"]:
        logger.warning(f"Login failed | username = {user.username, user.password}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
        
             
    logger.info(f"Login Successful | username={user.username}")
    access_token = create_access_token(
        data={
            'username':user.username,
            'role':USERS[user.username]['role']
        }
    )

    return {
        "sucess": True, 
        'data':{
            'access_token':access_token,
            'token_type':'bearer'
        },
        "message": 'Login Successfull'
    }
