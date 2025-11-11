from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.core.security import decode_access_token
from app.schemas.auth import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    print ("Token payload in dependency:", payload)
    
    try:
        token_data = TokenData(user_id=int(payload.get("sub")))
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Invalid token payload: {e}")
    
    return token_data