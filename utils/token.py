import jwt
from datetime import datetime, timedelta, timezone

# TOKEN
SECRET_KEY = "864183de98efa7ffdac3cce9ebf1b4e4dcaa6d41d35139a333ffdcf4a369671a"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 3

fake_data={
    "username":'test'
}


def create_token(data:dict)-> str:
    duration_access_token = timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        'username':data.username,
        'exp': datetime.now(timezone.utc)+duration_access_token
    }
    token = jwt.encode(payload=payload,key= SECRET_KEY,algorithm=ALGORITHM)
    return token

def verify_valid_token(token:str,data:dict)-> bool:
    token = jwt.decode(jwt=token,key=SECRET_KEY, algorithms=ALGORITHM)
    now = int(datetime.now(timezone.utc).timestamp())

    if token["username"]==data["username"] and now < token["exp"] :
        return True
    else: 
        return False

def refresh_token(token: str,data:dict):
    tok_user = jwt.decode(jwt=token, key = SECRET_KEY, algorithms=ALGORITHM)
    if tok_user["username"] == data["username"]:
        refresh_token = create_token(data)
    else:
        raise Exception("token invalid")

    return refresh_token
