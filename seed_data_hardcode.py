"""
This script seeds hard coded data that is defined here.
"""

from backend.src.models import Post, User
from hashlib import sha256
import random
import os
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DB_URL = (
    f"postgresql+psycopg://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@localhost:5432/"
    f"{os.getenv('POSTGRES_DB')}"
)

engine = create_engine(DB_URL)

SessionLocal = sessionmaker(bind=engine)

def seed_users():

    usernames = [
        "foodlover", "chefmaster", "pizza_fan", "burgerking",
        "tastytreats", "cookbook", "foodexplorer", "sweettooth",
        "spicyfood", "hungrywolf", "pastalover", "sushifan",
        "baker123", "foodcritic", "grillmaster", "veganlife",
        "snacktime", "coffeeaddict", "dessertking", "foodie101"
    ]

    languages = [
        "English", "Spanish", "French",
        "German", "Japanese", "Chinese"
    ]

    try:
        with SessionLocal() as db:

            users = []

            for username in usernames:
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

    descriptions = [
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
    ]

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
                    description=random.choice(descriptions)
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

