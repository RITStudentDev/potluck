"""
This script seeds hard coded data that is defined here.
"""

import os
from dotenv import load_dotenv
from hashlib import sha256
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

from backend.src.models import Post, User, PostImages

load_dotenv()

user = os.getenv("POSTGRES_USER")
passwd = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")

POSTGRES_URL = f"postgresql+psycopg://{user}:{passwd}@localhost:5432/{db_name}"
engine = create_engine(POSTGRES_URL)
SessionLocal = sessionmaker(bind=engine)

USERNAMES = (
    "foodlover",
    "chefmaster",
    "pizza_fan",
    "burgerking",
    "tastytreats",
    "cookbook",
    "foodexplorer",
    "sweettooth",
    "spicyfood",
    "hungrywolf",
    "pastalover",
    "sushifan",
    "baker123",
    "foodcritic",
    "grillmaster",
    "veganlife",
    "snacktime",
    "coffeeaddict",
    "dessertking",
    "foodie101",
)

LANGUAGES = (
    "English",
    "Spanish",
    "French",
    "German",
    "Japanese",
    "Chinese",
)

DESCRIPTIONS = (
    "Homemade margherita pizza with fresh basil and mozzarella.",
    "Made the juiciest smash burgers for dinner tonight!",
    "Fresh strawberry cheesecake with a buttery graham cracker crust.",
    "Trying out a new spicy ramen recipe with soft-boiled eggs.",
    "Sunday breakfast: fluffy pancakes topped with berries.",
    "Nothing beats a warm bowl of homemade chicken noodle soup.",
    "Grilled salmon with lemon butter and roasted asparagus.",
    "My first attempt at making authentic Japanese sushi rolls.",
    "Freshly baked chocolate chip cookies straight from the oven.",
    "Mouthwatering Caesar salad topped with grilled chicken and freshly grated Parmesan cheese.",
    "A colorful poke bowl packed with fresh vegetables and tuna.",
    "Homemade tacos with slow-cooked beef and fresh cilantro.",
    "The perfect iced caramel latte for a busy morning.",
    "Crispy Korean fried chicken glazed with a sesame sauce.",
    "Homemade Indian butter chicken served with fluffy basmati rice and garlic naan.",
    "Fresh Thai mango sticky rice drizzled with sweet coconut milk.",
    "A steaming bowl of Vietnamese pho with tender beef, rice noodles, and fresh herbs.",
    "Indonesian golden potato fritters with spicy sauce on a white plate.",
    "Lebanese chicken shawarma wrapped in warm pita with garlic sauce and pickles.",
    "Homemade Filipino chicken adobo simmered in soy sauce, vinegar, and garlic.",
    "Spicy Nigerian jollof rice served with a crispy chicken thigh.",
    "Peruvian lomo saltado with stir-fried beef, tomatoes, onions, and golden fries.",
    "Freshly made Chinese soup dumplings filled with savory pork and rich broth.",
    "Delicious Moroccan chicken tagine with steamed rolls and preserved fruit bowl, perfect for a cultural feast.",
    "Delicious Brazilian feijoada with rice, orange, beans, and salad served on a wooden table.",
    "Turkish baklava layered with pistachios, flaky pastry, and sweet syrup.",
    "Homemade Jamaican jerk chicken with rice and plantains.",
    "Spanish seafood paella loaded with shrimp, mussels, and saffron-infused rice.",
    "Fresh Greek spanakopita filled with spinach, feta, and crispy phyllo pastry.",
    "Ending the day with homemade Argentine empanadas stuffed with seasoned beef."
)

# helper function to seed post images, used by seed_posts()
def seed_post_image(index):
    with SessionLocal.begin() as db:
        image_url_string = f"posts/{index}"
        image_object = PostImages(
            post_id=index,
            image_url=image_url_string
        )

        db.add(image_object)

def seed_users():
    password_hash = sha256(
        "TestPassword123!".encode()
    ).hexdigest()

    with SessionLocal.begin() as db:
        existing = set(
            db.execute(select(User.username)).scalars().all()
        )

        users = []

        for i, username in enumerate(USERNAMES):
            if username in existing:
                continue

            users.append(
                User(
                    username=username,
                    password=password_hash,
                    language=LANGUAGES[i % len(LANGUAGES)]
                )
            )

        db.add_all(users)

    print(f"Successfully seeded {len(users)} new users!")

def seed_posts():
    with SessionLocal.begin() as db:
        users_by_name = {
            user.username: user.id
            for user in db.execute(select(User)).scalars()
        }

        user_ids = [
            users_by_name[name]
            for name in USERNAMES
            if name in users_by_name
        ]

        if not user_ids:
            print("No users found. Seed users first.")
            return

        existing_posts = {
            post.description: post
            for post in db.execute(select(Post)).scalars()
        }

        new_posts = 0
        new_images = 0

        for i, description in enumerate(DESCRIPTIONS):
            post = existing_posts.get(description)

            if post is None:
                post = Post(
                    owner=user_ids[i % len(user_ids)],
                    like_num=(i * 7) % 101,
                    description=description,
                )

                db.add(post)
                db.flush()

                new_posts += 1

            image_url = f"posts/{i + 1}"

            existing_image = db.scalar(
                select(PostImages.id)
                .where(PostImages.post_id == post.id)
                .where(PostImages.image_url == image_url)
            )

            if existing_image is None:
                db.add(
                    PostImages(
                        post_id=post.id,
                        image_url=image_url,
                    )
                )
                new_images += 1

    print(f"Successfully seeded {new_posts} new posts!")
    print(f"Successfully seeded {new_images} new images!")

if __name__ == "__main__":
    try:
        seed_users()
        seed_posts()
    finally:
        engine.dispose()