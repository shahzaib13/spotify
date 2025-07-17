from secret_keys import DatbaseUrl
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine(DatbaseUrl)

SessionLocal = sessionmaker(bind=engine, autoflush= False, autocommit = False)

def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close