from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends 
import token_management

auth_scheme = HTTPBearer()

def token_check(token : HTTPAuthorizationCredentials = Depends(auth_scheme)):
    username = token_management.check_token(token.credentials)
    return username