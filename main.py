from fastapi import FastAPI
from interfaces.api import main

app = FastAPI()

app.include_router(main.router)

if __name__ == "__main__":
    from infrastructure.db.config.config import create_db_and_tables
    create_db_and_tables()
