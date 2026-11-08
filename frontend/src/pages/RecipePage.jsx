import '../css/RecipePage.css';
import veggiePizza from '../images/Veggie-Pizza-12.jpg';
import PostCard from '../components/PostCard';
import { useState, useEffect } from 'react';

export default function RecipePage() {

    const [recipe, setRecipe] = useState(true);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function loadPosts(){
            const res = await fetch(`/api/post/?limit=50&offet=0`);
            const restaurant = await res.json();
            setRecipe(restaurant);
            setLoading(false);
        }
        loadPosts();
    }, []);

    return(
        <div className="recipe-container">
            <div className="postImage">
                <img src={recipe.image_url} alt="MainPhoto" />
            </div>

            <div className="descriptionOfPost">
                <p>{recipe.description}</p>
                <section className="recipeDetails">
                    <h2>Recipe Details</h2>
                    <p>{recipe.description}</p>
                </section>
            </div>
        </div>
    );
}
