from fastapi import FastAPI
from app.routes import auth,tickets

app = FastAPI(title='Student Support Ticket API', version='1.0.0')

app.include_router(auth.router)
app.include_router(tickets.router)

@app.get('/')
def check():
    return {
        'success' : True,
        'message' : 'Student support api is running'
    }