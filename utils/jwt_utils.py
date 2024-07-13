import jwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status

# TOKEN
SECRET_KEY = "864183de98efa7ffdac3cce9ebf1b4e4dcaa6d41d35139a333ffdcf4a369671a"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10

fake_data={
    "username":'test'
}


def create_token(username:str, username_id:str)-> str:
    duration_access_token = timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        'username':username,
        'username_id':username_id,
        'exp': datetime.now(timezone.utc)+duration_access_token
    }
    token = jwt.encode(payload=payload,key= SECRET_KEY,algorithm=ALGORITHM)
    return token


def refresh_token(token: str):
    payload = jwt.decode(jwt=token, key = SECRET_KEY, algorithms=ALGORITHM)
    if payload["username"]:
        refresh_token = create_token(payload["username"],payload["username_id"])
    else:
        raise Exception("token invalid")

    return refresh_token

def check_token(token):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token = jwt.decode(jwt=token,key=SECRET_KEY, algorithms=ALGORITHM)
        username : str = token.get("username")
        if username is None :
            raise credentials_exception
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"}
        )
    except jwt.PyJWTError:
        raise credentials_exception
    return username