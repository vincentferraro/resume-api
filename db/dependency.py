from .db import SessionLocal

#Dependency
def get_db(session_local):
    db = session_local
    try: 
        yield db
    finally:
        db.close()
