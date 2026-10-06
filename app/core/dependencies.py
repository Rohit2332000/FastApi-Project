from fastapi import Header,HTTPException
from app.core.config import settings
from app.core.security import verify_token



def get_api_key(api_key:str=Header(...)):
    if api_key!=settings.API_KEY:
        raise HTTPException(status_code=403,detail="Invalid API key")
    
def get_current_user(token:str=Header(...)):
    payload=verify_token(token=token)
    if not payload:
        raise HTTPException(status_code=401,detail="Invalid JWT token")  
    return payload      