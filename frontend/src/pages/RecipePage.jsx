import '../css/RecipePage.css';
import veggiePizza from '../images/Veggie-Pizza-12.jpg';
import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

export default function RecipePage() {

    const [recipe, setRecipe] = useState(true);
    const [loading, setLoading] = useState(true);
    const { postId } = useParams();

    const viewerLang = (navigator.language || 'en').slice(0, 2); // switch to get current users language
    const [translation, setTranslation] = useState(null);
    const [showOriginal, setShowOriginal] = useState(false);

    useEffect(() => {
        async function loadPost(){
            const res = await fetch(`/api/post/${postId}`);
            const restaurant = await res.json();
            setRecipe(restaurant);
            setLoading(false);
        }
        loadPost();
    }, []);

    useEffect(() => {
        setTranslation(null);

        fetch(`/api/post/${postId}/translation?lang=${viewerLang}`)
            .then((res) => (res.ok ? res.json() : null))
            .then((data) => data && setTranslation(data))
            .catch(() => {});
    }, [postId, viewerLang]);

    return(
        <div className="recipe-container">
            <div className="postImage">
                <img src={recipe.image_url} alt="MainPhoto" />
            </div>

            <div className="descriptionOfPost">
                <p>{recipe.description}</p>
                <section className="recipeDetails">
                    <h2>Recipe Details</h2>
                    <p>
                        {translation && !showOriginal ? translation.description : recipe.description}
                    </p>
                    {translation?.translated && (
                        <button onClick={() => setShowOriginal((v) => !v)}>
                            {showOriginal ? 'Show translation' : 'Show original'}
                        </button>
                    )}
                </section>
            </div>
        </div>
    );
}
