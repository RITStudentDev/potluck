import '../css/RecipePage.css';
import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

export default function RecipePage() {
    const { postId } = useParams();
    const viewerLang = (navigator.language || 'en').slice(0, 2); // switch to the current user's language

    const [recipe, setRecipe] = useState(null);
    const [loading, setLoading] = useState(true);
    const [translation, setTranslation] = useState(null);
    const [showOriginal, setShowOriginal] = useState(false);

    useEffect(() => {
        setLoading(true);

        async function loadPost() {
            const res = await fetch(`/api/post/${postId}`);
            if (res.ok) setRecipe(await res.json());
            setLoading(false);
        }
        loadPost();
    }, [postId]);

    useEffect(() => {
        setTranslation(null);
        setShowOriginal(false);

        fetch(`/api/post/${postId}/translation?lang=${viewerLang}`)
            .then((res) => (res.ok ? res.json() : null))
            .then((data) => data && setTranslation(data))
            .catch(() => {});
    }, [postId, viewerLang]);

    if (loading) return <p>Loading...</p>;
    if (!recipe) return <p>Post not found.</p>;

    const showTranslated = translation && !showOriginal;
    const description = showTranslated ? translation.description : recipe.description;
    const instructions = showTranslated ? translation.instructions : recipe.instructions;

    return (
        <div className="recipe-container">
            <div className="postImage">
                <img src={recipe.image_url} alt="MainPhoto" />
            </div>

            <div className="descriptionOfPost">
                <p>{description}</p>

                <section className="recipeDetails">
                    <h2>Recipe Details</h2>

                    <h3>Instructions</h3>
                    <p style={{ whiteSpace: 'pre-line' }}>{instructions}</p>

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