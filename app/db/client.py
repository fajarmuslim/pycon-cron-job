from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings

def get_engine():
    return create_engine(url=f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}")

def get_db():
    try:
        engine = get_engine()
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        print(f"Connection to the {settings.POSTGRES_HOST} for user {settings.POSTGRES_USER} created successfully.")

        return SessionLocal()   
    except Exception as e:
        print(f'Connection could not be made due to the following error: \n, {e}')

engine = get_engine()
db = get_db()