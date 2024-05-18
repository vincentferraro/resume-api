from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def initializing_db():
    SQLALCHEMY_DATABASE_URL="postgresql://admin:admin@127.0.0.1:5433/resume-api"

    engine = create_engine(SQLALCHEMY_DATABASE_URL)

    SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

    Base = declarative_base()

    Base.metadata.create_all(bind=engine)

    return  SessionLocal