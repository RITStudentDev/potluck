import os
from sqlalchemy import create_engine

DB_URL = os.getenv("DB_URL") # Change to reference real env variable
engine = create_engine(DB_URL)