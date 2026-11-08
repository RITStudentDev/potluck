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
    "Sunday breakfast: fluffy pancakes topped with blueberries.",
    "Nothing beats a warm bowl of homemade chicken noodle soup.",
    "Grilled salmon with lemon butter and roasted asparagus.",
    "My first attempt at making authentic Japanese sushi rolls.",
    "Freshly baked chocolate chip cookies straight from the oven.",
    "Creamy garlic parmesan pasta with grilled chicken.",
    "A colorful poke bowl packed with fresh vegetables and tuna.",
    "Homemade tacos with slow-cooked beef and fresh cilantro.",
    "The perfect iced caramel latte for a busy morning.",
    "Crispy Korean fried chicken coated in sweet and spicy sauce.",
    "Made a classic Caesar salad with homemade dressing.",
    "Fresh mango sticky rice is my favorite Thai dessert.",
    "A delicious bowl of pho with tender beef and fresh herbs.",
    "Weekend baking project: homemade cinnamon rolls.",
    "Grilled steak cooked medium rare with garlic mashed potatoes.",
    "Avocado toast topped with poached eggs and chili flakes.",
    "Made some delicious vegetable dumplings from scratch.",
    "Trying a new recipe for creamy mushroom risotto.",
    "Fresh homemade guacamole with crispy tortilla chips.",
    "A beautiful charcuterie board for a weekend gathering.",
    "Spicy buffalo wings with homemade ranch dipping sauce.",
    "Classic tiramisu with layers of espresso-soaked ladyfingers.",
    "Homemade fried rice with shrimp, eggs, and vegetables.",
    "Freshly baked sourdough bread with a golden crispy crust.",
    "A refreshing watermelon and feta salad for summer.",
    "Ending the day with a warm chocolate lava cake."
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