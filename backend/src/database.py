import os
from sqlalchemy import create_engine

POSTGRES_URL = os.getenv("PURL")

engine = create_engine(POSTGRES_URL)