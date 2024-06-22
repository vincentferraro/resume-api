from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends 
from..utils import jwt_utils

auth_scheme = HTTPBearer()

def token_check(token : HTTPAuthorizationCredentials = Depends(auth_scheme)):
    username = jwt_utils.check_token(token.credentials)
    return username