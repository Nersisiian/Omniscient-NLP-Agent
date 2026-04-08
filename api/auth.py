from fastapi import HTTPException, Header

def authorize(token: str = Header(...)):
    if token != 'SECRET_TOKEN':
        raise HTTPException(status_code=401, detail='Unauthorized')