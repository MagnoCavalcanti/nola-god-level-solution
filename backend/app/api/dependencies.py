from app.core import Session as sessionmaker

def get_db_session():
    try:
        session = sessionmaker()
        yield session
    finally:
        session.close()  