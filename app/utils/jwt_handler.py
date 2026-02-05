from jose import jwt, JWTError
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY  = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

def create_access_token(data : dict):
    to_encode = data.copy()
    to_encode["exp"] = datetime.now() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode(to_encode, SECRET_KEY , algorithm=ALGORITHM)
    

def decode_access_token(token : str):
    try:
        return jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])        
    except JWTError:
        return None
    
    

# if __name__ == "__main__":
#     print("hi, test")
#     print(SECRET_KEY)
#     print(ALGORITHM)
#     print(type(ACCESS_TOKEN_EXPIRE_MINUTES))
    