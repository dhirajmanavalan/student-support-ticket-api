from fastapi import FastAPI, Request
from app.routes import auth,tickets
from app.utils.logger import logger

app = FastAPI(title='Student Support Ticket API', 
              version='1.0.0')

app.include_router(auth.router)
app.include_router(tickets.router)

@app.get('/')
def check():
    return {
        'success' : True,
        'message' : 'Student support api is running'
    }
    
@app.middleware("http")
async def log_requests(request: Request, call_next):
    response = await call_next(request)

    logger.info(f"{request.method} {request.url.path} | status={response.status_code}")

    return response