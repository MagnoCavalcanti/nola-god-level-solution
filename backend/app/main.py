from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError
from .api import get_db_session
from app.services import QueryService

app = FastAPI(title="Solution")

@app.get("/{table}")
def home(table: str, db: Session = Depends(get_db_session)):
    try:
        query_service = QueryService(db)
        results = query_service.select_all(table)
        print(results)

        return results

    except OperationalError:
        return "Database connection failed"