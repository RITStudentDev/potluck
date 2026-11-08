import os
from sqlalchemy import create_engine

user = os.getenv("POSTGRES_USER")
passwd = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
port = os.getenv("POSTGRES_PORT")
ghost = os.getenv("PGHOST")
ssl = os.getenv("PGSSLMODE")

POSTGRES_URL = f"postgresql+psycopg://{user}:{passwd}@{ghost}:{port}/{db_name}?sslmode=require"

engine = create_engine(POSTGRES_URL)