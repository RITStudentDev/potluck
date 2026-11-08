"""
This script seeds CSV data from the assets/ folder
"""
import csv
import os
import secrets
from pathlib import Path
from datetime import datetime
from hashlib import sha256
from dotenv import load_dotenv
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import sessionmaker

from backend.src.models import User, Post

load_dotenv()

DB_URL = (
    f"postgresql+psycopg://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@localhost:5432/"
    f"{os.getenv('POSTGRES_DB')}"
)

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)

CSV_FILE = (
    Path(__file__).parent.parent
    /"project-food"
    / "assets"
    / "dataform.csv"
)

def import_recipes():
    imported = 0
    created_users = 0

    try:
        with SessionLocal() as db:
            with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    username = (row["Name/Username"] or "").strip()
                    dish_name = (row["Dish name"] or "").strip()
                    recipe = (row["Recipe (optional) "] or "").strip()
                    if not username or not dish_name:
                        print("Skipping row with missing username or dish name.")
                        continue
                    user = db.execute(
                        select(User).where(
                            func.lower(User.username) == username.lower()
                        )
                    ).scalar_one_or_none()
                    if user is None:
                        random_password = secrets.token_urlsafe(32)
                        user = User(
                            username=username,
                            password=sha256(
                                random_password.encode()
                            ).hexdigest(),
                            language="English"
                        )
                        db.add(user)
                        db.flush() 
                        created_users += 1
                    description = (
                        f"Dish: {dish_name}\n\n"
                        f"Recipe:\n"
                        f"{recipe if recipe else 'Not provided.'}"
                    )
                    post_time = datetime.strptime(
                        row["Timestamp"].strip(),
                        "%m/%d/%Y %H:%M:%S"
                    )
                    post = Post(
                        owner=user.id,
                        like_num=0,
                        description=description,
                        post_time=post_time
                    )
                    db.add(post)
                    imported += 1

            db.commit()

        print(f"Successfully imported {imported} recipes!")
        print(f"Created {created_users} new users.")

    except Exception as e:
        print(f"Error importing recipes: {e}")
        
    finally:
        engine.dispose()

if __name__ == "__main__":
    import_recipes()

