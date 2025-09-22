from sqlalchemy.orm import sessionmaker, Session
from backend.app.models.db import db


def get_session_db():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()