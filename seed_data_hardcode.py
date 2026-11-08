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
    "Xx_shadow_xX",
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
    "en",
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


RECIPES = (
    """Ingredients: Pizza dough, tomato sauce, fresh mozzarella, basil, olive oil, salt.
    1. Preheat oven to 475°F (245°C).
    2. Stretch pizza dough into a round shape.
    3. Spread tomato sauce evenly over the dough.
    4. Add sliced mozzarella and a drizzle of olive oil.
    5. Bake for 10-15 minutes until the crust is golden.
    6. Top with fresh basil leaves and serve.""",

    """Ingredients: Ground beef, burger buns, American cheese, onions, pickles, salt, pepper, burger sauce.
    1. Divide ground beef into small balls.
    2. Heat a cast-iron skillet over high heat.
    3. Place beef balls onto the skillet and smash them flat.
    4. Season with salt and pepper.
    5. Cook for 2-3 minutes, then flip and add cheese.
    6. Cook until the beef reaches 160°F (71°C).
    7. Assemble burgers with buns, onions, pickles, and sauce.""",

    """Ingredients: Cream cheese, strawberries, graham crackers, butter, sugar, eggs, vanilla extract.
    1. Preheat oven to 325°F (165°C).
    2. Crush graham crackers and mix with melted butter.
    3. Press the mixture into a springform pan.
    4. Beat cream cheese, sugar, eggs, and vanilla until smooth.
    5. Pour filling over the crust.
    6. Bake for 50-60 minutes until the edges are set.
    7. Cool completely and refrigerate for at least 4 hours.
    8. Top with sliced strawberries before serving.""",

    """Ingredients: Ramen noodles, chicken broth, soy sauce, chili paste, eggs, garlic, green onions.
    1. Boil eggs for 6-7 minutes, then transfer to ice water.
    2. Heat broth with garlic, soy sauce, and chili paste.
    3. Simmer for 10 minutes to develop flavor.
    4. Cook ramen noodles according to package instructions.
    5. Divide noodles into serving bowls.
    6. Pour hot broth over noodles.
    7. Add halved eggs, green onions, and chili oil.""",

    """Ingredients: Flour, baking powder, milk, eggs, sugar, butter, blueberries, strawberries, maple syrup.
    1. Mix flour, baking powder, and sugar in a bowl.
    2. Whisk milk, eggs, and melted butter separately.
    3. Combine wet and dry ingredients until just mixed.
    4. Heat a lightly buttered skillet over medium heat.
    5. Pour batter into small circles.
    6. Flip when bubbles form and cook until golden.
    7. Serve with fresh berries and maple syrup.""",

    """Ingredients: Chicken breast, carrots, celery, onion, egg noodles, chicken broth, garlic, parsley.
    1. Dice carrots, celery, onion, and garlic.
    2. Saute vegetables in a large pot until softened.
    3. Add chicken and chicken broth.
    4. Simmer until chicken reaches 165°F (74°C).
    5. Remove chicken, shred it, and return it to the pot.
    6. Add egg noodles and cook until tender.
    7. Season with salt, pepper, and parsley.""",

    """Ingredients: Salmon fillets, asparagus, butter, lemon, garlic, olive oil, salt, pepper.
    1. Preheat oven to 400°F (200°C).
    2. Arrange salmon and asparagus on a baking sheet.
    3. Drizzle with olive oil and season with salt and pepper.
    4. Melt butter with minced garlic and lemon juice.
    5. Brush lemon butter over the salmon.
    6. Roast until salmon reaches 145°F (63°C).
    7. Serve with roasted asparagus and lemon wedges.""",

    """Ingredients: Sushi rice, nori sheets, cucumber, avocado, sushi-grade fish, rice vinegar, sugar.
    1. Rinse sushi rice until the water runs clear.
    2. Cook rice according to package instructions.
    3. Mix rice vinegar and sugar into the cooked rice.
    4. Spread a thin layer of rice onto a nori sheet.
    5. Arrange cucumber, avocado, and fish in the center.
    6. Roll tightly using a bamboo sushi mat.
    7. Slice into bite-sized pieces and serve with soy sauce.""",

    """Ingredients: Flour, butter, brown sugar, white sugar, eggs, vanilla extract, baking soda, chocolate chips.
    1. Preheat oven to 350°F (175°C).
    2. Cream butter and both sugars until fluffy.
    3. Beat in eggs and vanilla extract.
    4. Mix flour and baking soda separately.
    5. Combine dry ingredients with the butter mixture.
    6. Fold in chocolate chips.
    7. Scoop dough onto a lined baking sheet.
    8. Bake for 10-12 minutes until edges are golden.""",

    """Ingredients: Romaine lettuce, chicken breast, Parmesan cheese, croutons, Caesar dressing, olive oil.
    1. Season chicken breast with salt and pepper.
    2. Grill chicken until it reaches 165°F (74°C).
    3. Allow chicken to rest before slicing.
    4. Wash and chop romaine lettuce.
    5. Toss lettuce with Caesar dressing.
    6. Add sliced chicken, croutons, and Parmesan.
    7. Serve immediately.""",

    """Ingredients: Sushi-grade tuna, sushi rice, cucumber, avocado, edamame, carrots, soy sauce, sesame seeds.
    1. Cook sushi rice and allow it to cool slightly.
    2. Dice tuna into bite-sized cubes.
    3. Mix tuna with soy sauce and sesame oil.
    4. Slice cucumber, avocado, and carrots.
    5. Add rice to the bottom of a serving bowl.
    6. Arrange tuna and vegetables over the rice.
    7. Sprinkle sesame seeds on top and serve chilled.""",

    """Ingredients: Beef chuck roast, tortillas, onion, cilantro, garlic, cumin, chili powder, beef broth, lime.
    1. Season beef with cumin, chili powder, salt, and pepper.
    2. Sear beef in a large pot until browned.
    3. Add onion, garlic, and beef broth.
    4. Cover and simmer for 3-4 hours until tender.
    5. Shred beef using two forks.
    6. Warm tortillas in a skillet.
    7. Fill tortillas with beef, cilantro, and diced onion.
    8. Serve with lime wedges.""",

    """Ingredients: Espresso, milk, caramel syrup, ice cubes, whipped cream.
    1. Brew two shots of espresso.
    2. Allow espresso to cool slightly.
    3. Fill a tall glass with ice cubes.
    4. Add caramel syrup and cold milk.
    5. Pour espresso over the milk.
    6. Stir gently until combined.
    7. Top with whipped cream and caramel drizzle.""",

    """Ingredients: Chicken wings, flour, cornstarch, soy sauce, garlic, ginger, honey, gochujang, sesame seeds.
    1. Pat chicken wings dry and coat with flour and cornstarch.
    2. Heat frying oil to 350°F (175°C).
    3. Fry chicken in batches until golden and cooked through to 165°F (74°C).
    4. Mix soy sauce, garlic, ginger, honey, and gochujang in a saucepan.
    5. Simmer sauce until slightly thickened.
    6. Toss fried chicken in the glaze.
    7. Garnish with sesame seeds and green onions.""",

    """Ingredients: Chicken thighs, butter, tomato puree, heavy cream, yogurt, garlic, ginger, garam masala, basmati rice.
    1. Marinate chicken in yogurt, garlic, ginger, and spices.
    2. Cook chicken in a skillet until lightly browned.
    3. Melt butter in a saucepan and add tomato puree.
    4. Stir in garam masala and simmer for 10 minutes.
    5. Add chicken and cook until it reaches 165°F (74°C).
    6. Stir in heavy cream and simmer gently.
    7. Serve over fluffy basmati rice with garlic naan.""",

    """Ingredients: Glutinous rice, ripe mangoes, coconut milk, sugar, salt, sesame seeds.
    1. Soak glutinous rice in water for at least 4 hours.
    2. Drain and steam rice until tender.
    3. Heat coconut milk with sugar and a pinch of salt.
    4. Reserve some coconut sauce for serving.
    5. Mix most of the warm coconut sauce into the rice.
    6. Let rice absorb the sauce for 15 minutes.
    7. Slice ripe mangoes and arrange beside the rice.
    8. Drizzle with remaining coconut sauce and garnish.""",

    """Ingredients: Beef bones, thinly sliced beef, rice noodles, onion, ginger, star anise, cinnamon, fish sauce, fresh herbs.
    1. Char onion and ginger in a hot skillet.
    2. Simmer beef bones with onion, ginger, and spices for several hours.
    3. Strain broth and season with fish sauce.
    4. Cook rice noodles according to package directions.
    5. Divide noodles into serving bowls.
    6. Add thinly sliced beef and pour boiling broth over it.
    7. Ensure beef is fully cooked before eating.
    8. Garnish with Thai basil, cilantro, lime, and bean sprouts.""",

    """Ingredients: Potatoes, garlic, shallots, eggs, flour, coriander, salt, pepper, chili sauce.
    1. Peel and boil potatoes until fork-tender.
    2. Mash potatoes and allow them to cool.
    3. Saute minced garlic and shallots until fragrant.
    4. Combine potatoes, garlic, shallots, coriander, and seasoning.
    5. Shape mixture into small round patties.
    6. Lightly coat each patty with beaten egg.
    7. Pan-fry until golden brown on both sides.
    8. Serve Indonesian perkedel with spicy chili sauce.""",

    """Ingredients: Chicken thighs, pita bread, garlic, lemon juice, yogurt, cumin, paprika, turmeric, pickles, garlic sauce.
    1. Mix yogurt, garlic, lemon juice, cumin, paprika, and turmeric.
    2. Marinate chicken for at least 2 hours.
    3. Grill or roast chicken until it reaches 165°F (74°C).
    4. Allow chicken to rest before slicing thinly.
    5. Warm pita bread in a skillet.
    6. Spread garlic sauce over each pita.
    7. Add chicken, pickles, and fresh vegetables.
    8. Wrap tightly and serve.""",

    """Ingredients: Chicken thighs, soy sauce, vinegar, garlic, bay leaves, black peppercorns, onion, cooking oil.
    1. Combine chicken, soy sauce, vinegar, garlic, and peppercorns.
    2. Marinate for at least 30 minutes.
    3. Heat oil in a pot and brown chicken pieces.
    4. Add marinade, bay leaves, and sliced onion.
    5. Bring to a simmer and cover.
    6. Cook for 30-40 minutes until chicken reaches 165°F (74°C).
    7. Reduce sauce slightly until rich and savory.
    8. Serve with steamed white rice.""",

    """Ingredients: Long-grain rice, tomatoes, red bell peppers, onions, scotch bonnet pepper, tomato paste, chicken stock, thyme, curry powder, chicken thighs.
    1. Blend tomatoes, bell peppers, onions, and scotch bonnet.
    2. Heat oil in a large pot and fry tomato paste.
    3. Add blended pepper mixture and simmer until reduced.
    4. Season with thyme, curry powder, and salt.
    5. Stir in washed rice and chicken stock.
    6. Cover tightly and cook over low heat until rice is tender.
    7. Season chicken thighs and roast until they reach 165°F (74°C).
    8. Serve jollof rice with roasted chicken.""",

    """Ingredients: Beef sirloin, red onions, tomatoes, potatoes, soy sauce, vinegar, garlic, cilantro, rice.
    1. Cut potatoes into fries and cook until golden.
    2. Slice beef into thin strips.
    3. Heat a wok or skillet over high heat.
    4. Sear beef until browned and cooked to your preference.
    5. Add red onions, tomatoes, and garlic.
    6. Stir-fry briefly to keep vegetables slightly crisp.
    7. Add soy sauce and a splash of vinegar.
    8. Toss with fries and serve over rice with cilantro.""",

    """Ingredients: Dumpling wrappers, ground pork, ginger, scallions, soy sauce, sesame oil, chicken stock, gelatin.
    1. Prepare concentrated chicken stock and set with gelatin.
    2. Refrigerate until firm, then finely dice.
    3. Mix ground pork with ginger, scallions, soy sauce, and sesame oil.
    4. Fold diced stock jelly into the pork mixture.
    5. Place a small portion of filling onto each wrapper.
    6. Pleat and seal wrappers carefully.
    7. Steam dumplings for 8-12 minutes until pork reaches 160°F (71°C).
    8. Serve hot with black vinegar and ginger.""",

    """Ingredients: Chicken thighs, onion, garlic, ginger, preserved lemon, green olives, turmeric, cumin, cinnamon, chicken broth.
    1. Season chicken with turmeric, cumin, cinnamon, and salt.
    2. Brown chicken in a tagine or heavy pot.
    3. Add chopped onion, garlic, and ginger.
    4. Pour in chicken broth and bring to a gentle simmer.
    5. Add preserved lemon and green olives.
    6. Cover and cook for 40-50 minutes until chicken reaches 165°F (74°C).
    7. Reduce sauce slightly and adjust seasoning.
    8. Serve with couscous or warm bread.""",

    """Ingredients: Black beans, beef, pork shoulder, smoked sausage, onion, garlic, bay leaves, white rice, oranges.
    1. Soak dried black beans overnight.
    2. Drain beans and place in a large pot with fresh water.
    3. Add bay leaves and simmer until beans begin to soften.
    4. Brown beef, pork shoulder, and sausage separately.
    5. Add meats, sauteed onion, and garlic to the beans.
    6. Simmer until beans are creamy and all meats are fully cooked and tender.
    7. Season with salt and pepper.
    8. Serve with white rice, orange slices, and greens.""",

    """Ingredients: Phyllo pastry, pistachios, butter, sugar, water, lemon juice, cinnamon.
    1. Preheat oven to 350°F (175°C).
    2. Finely chop pistachios and mix with cinnamon.
    3. Brush a baking dish with melted butter.
    4. Layer phyllo sheets, brushing each with butter.
    5. Sprinkle pistachio mixture between groups of layers.
    6. Cut assembled pastry into diamond shapes.
    7. Bake for 35-45 minutes until golden and crisp.
    8. Simmer sugar, water, and lemon juice into a syrup.
    9. Pour cooled syrup over hot baklava and let it absorb.""",

    """Ingredients: Chicken thighs, allspice, thyme, scotch bonnet pepper, garlic, ginger, brown sugar, soy sauce, lime juice, rice, plantains.
    1. Blend allspice, thyme, pepper, garlic, ginger, sugar, soy sauce, and lime.
    2. Coat chicken in jerk marinade.
    3. Refrigerate for at least 4 hours or overnight.
    4. Grill or roast chicken until it reaches 165°F (74°C).
    5. Allow chicken to rest before serving.
    6. Cook rice according to package instructions.
    7. Slice ripe plantains and fry until golden.
    8. Serve jerk chicken with rice and plantains.""",

    """Ingredients: Spanish rice, shrimp, mussels, chicken stock, saffron, tomatoes, garlic, onion, smoked paprika, olive oil.
    1. Heat olive oil in a wide paella pan.
    2. Saute onion, garlic, and grated tomatoes.
    3. Stir in smoked paprika and Spanish rice.
    4. Add warm chicken stock infused with saffron.
    5. Spread rice evenly and simmer without stirring.
    6. Arrange shrimp and cleaned mussels over the rice.
    7. Cook until rice is tender, shrimp are opaque, and mussels open.
    8. Discard mussels that remain closed after cooking.
    9. Rest for 5 minutes and serve with lemon wedges.""",

    """Ingredients: Phyllo pastry, spinach, feta cheese, onion, garlic, eggs, dill, olive oil, butter.
    1. Preheat oven to 375°F (190°C).
    2. Saute onion and garlic in olive oil.
    3. Add spinach and cook until wilted.
    4. Squeeze out excess liquid and allow spinach to cool.
    5. Mix spinach with feta, beaten eggs, and fresh dill.
    6. Layer buttered phyllo sheets in a baking dish.
    7. Spread spinach filling evenly over the pastry.
    8. Cover with additional buttered phyllo layers.
    9. Bake for 35-45 minutes until golden brown.""",

    """Ingredients: Empanada dough, ground beef, onion, garlic, cumin, paprika, hard-boiled eggs, green olives, olive oil.
    1. Preheat oven to 400°F (200°C).
    2. Saute diced onion and garlic in olive oil.
    3. Add ground beef, cumin, paprika, salt, and pepper.
    4. Cook beef until it reaches 160°F (71°C).
    5. Remove from heat and mix in chopped eggs and olives.
    6. Place filling onto circles of empanada dough.
    7. Fold dough over filling and crimp edges to seal.
    8. Brush empanadas with beaten egg.
    9. Bake for 20-25 minutes until golden brown."""
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
        existing = {
            user.username: user
            for user in db.execute(
                select(User).where(User.username.in_(USERNAMES))
            ).scalars()
        }

        users = []
        updated_users = 0

        for i, username in enumerate(USERNAMES):
            language = LANGUAGES[i % len(LANGUAGES)]
            if username in existing:
                if existing[username].language != language:
                    existing[username].language = language
                    updated_users += 1
                continue

            users.append(
                User(
                    username=username,
                    password=password_hash,
                    language=language
                )
            )

        db.add_all(users)

    print(f"Successfully seeded {len(users)} new users!")
    print(f"Successfully updated {updated_users} existing user languages!")


def seed_posts():
    if len(DESCRIPTIONS) != len(RECIPES):
        raise ValueError(
            "Number of descriptions and recipes must match!"
        )

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
        updated_posts = 0
        new_images = 0

        for i, description in enumerate(DESCRIPTIONS):
            post = existing_posts.get(description)
            recipe = RECIPES[i]

            if post is None:
                post = Post(
                    owner=user_ids[i % len(user_ids)],
                    like_num=(i * 7) % 101,
                    description=description,
                    instructions=recipe,
                )

                db.add(post)
                db.flush()

                new_posts += 1

            else:
                # Update instructions on existing posts
                if post.instructions != recipe:
                    post.instructions = recipe
                    updated_posts += 1

            image_url = f"posts/{i + 1}.jpg"

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
    print(f"Successfully updated {updated_posts} existing posts!")
    print(f"Successfully seeded {new_images} new images!")


if __name__ == "__main__":
    try:
        seed_users()
        seed_posts()
    finally:
        engine.dispose()
