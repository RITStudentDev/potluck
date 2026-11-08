"""
This script seeds hard coded data that is defined here.
"""

import os
from dotenv import load_dotenv
import random
from hashlib import sha256
from backend.src.models import Post, User
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

load_dotenv()

user = os.getenv("POSTGRES_USER")
passwd = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")

POSTGRES_URL = f"postgresql+psycopg://{user}:{passwd}@db:5432/{db_name}"
engine = create_engine(POSTGRES_URL)
SessionLocal = sessionmaker(bind=engine)

USERNAMES = (
    "foodlover", "chefmaster", "pizza_fan", "burgerking",
    "tastytreats", "cookbook", "foodexplorer", "sweettooth",
    "spicyfood", "hungrywolf", "pastalover", "sushifan",
    "baker123", "foodcritic", "grillmaster", "veganlife",
    "snacktime", "coffeeaddict", "dessertking", "foodie101"
)

DESCRIPTIONS = (
    "Just enjoying the weather today!",
    "Check out this amazing photo.",
    "Anyone have recommendations for good restaurants?",
    "Had a great time with friends today.",
    "Working on a new project!",
    "What's everyone's favorite movie?",
    "Beautiful sunset tonight.",
    "Finally finished my homework!",
    "Does anyone have any gaming recommendations?",
    "Hope everyone is having a great day!"
)

def seed_users():

    languages = [
        "English", "Spanish", "French",
        "German", "Japanese", "Chinese"
    ]

    try:
        with SessionLocal() as db:

            users = []

            for username in USERNAMES:
                user = User(
                    username=username,
                    password=sha256(
                        "TestPassword123!".encode()
                    ).hexdigest(),
                    language=random.choice(languages)
                )

                users.append(user)

            db.add_all(users)
            db.commit()

        print(f"Successfully seeded {len(users)} users!")

    except Exception as e:
        print(f"Error seeding users: {e}")


def seed_posts():

    try:
        with SessionLocal() as db:

            users = db.execute(select(User.id)).scalars().all()

            if not users:
                print("No users found. Seed users first.")
                return

            posts = []

            for i in range(30):
                post = Post(
                    owner=random.choice(users),
                    like_num=random.randint(0, 100),
                    description=random.choice(DESCRIPTIONS)
                )

                posts.append(post)

            db.add_all(posts)
            db.commit()

        print(f"Successfully seeded {len(posts)} posts!")

    except Exception as e:
        print(f"Error seeding posts: {e}")

if __name__ == "__main__":
    seed_users()
    seed_posts()

    engine.dispose()