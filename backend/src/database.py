import os
from sqlalchemy import create_engine

user = os.getenv("POSTGRES_USER")
passwd = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")

POSTGRES_URL = f"postgresql+psycopg://{user}:{passwd}@db:5432/{db_name}"

engine = create_engine(POSTGRES_URL)