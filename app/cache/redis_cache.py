import json
import redis
from app.core.config import settings

redis_client=redis.Redis.from_url(settings.REDIS_URL)

def get_cached_prediction(key:str):
    value=redis_client.get(key)
    if value:
        json.loads(value)
        
    return None

def set_cache_prediction(key:str,value:dict,expiry:int=3600):
    redis_client.setex(key,expiry,json.dumps(value))
    
    