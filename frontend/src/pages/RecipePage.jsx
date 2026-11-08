import '../css/RecipePage.css';
import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import LangSelect, { getInitialLanguage } from '../components/LangSelect';
import { supabase } from '../util/supabaseConn';
import{useNavigate} from 'react-router-dom';

const API_URL = import.meta.env.VITE_API_URL;

export default function RecipePage() {
    const [viewerLang, setViewerLang] = useState(getInitialLanguage);
    const navigate = useNavigate();
    const [recipe, setRecipe] = useState(null);
    const [loading, setLoading] = useState(true);
    const [translation, setTranslation] = useState(null);
    const [showOriginal, setShowOriginal] = useState(false);
    const { postId } = useParams();
    const [isSaved, setIsSaved] = useState(false);

    useEffect(() => {
        const controller = new AbortController();
        setRecipe(null);
        setLoading(true);

        async function loadPost() {
            try {
                const res = await fetch(`${API_URL}/post/${postId}`, { signal: controller.signal });
                if (res.ok) setRecipe(await res.json());
            } catch (error) {
                if (error.name !== 'AbortError') setRecipe(null);
            } finally {
                if (!controller.signal.aborted) setLoading(false);
            }
        }
        loadPost();
        return () => controller.abort();
    }, [postId]);

    useEffect(() => {
        const controller = new AbortController();
        setTranslation(null);
        setShowOriginal(false);

        fetch(`${API_URL}/post/${postId}/translation?lang=${encodeURIComponent(viewerLang)}`, { signal: controller.signal })
            .then((res) => (res.ok ? res.json() : null))
            .then((data) => {
                if (data && !controller.signal.aborted) setTranslation(data);
            })
            .catch(() => {});
        return () => controller.abort();
    }, [postId, viewerLang]);

    let bookmarkIcon;

    if (isSaved === true) {
        bookmarkIcon = "⛊";
    }
    else {
        bookmarkIcon = "⛉";
    }

    if (loading) return <p>Loading...</p>;
    if (!recipe) return <p>Post not found.</p>;

    const showTranslated = translation && !showOriginal;
    const description = showTranslated ? translation.description : recipe.description;
    const instructions = showTranslated ? translation.instructions : recipe.instructions;
    const imageUrl = recipe.image_url && (
        /^https?:\/\//i.test(recipe.image_url)
            ? recipe.image_url
            : supabase.storage.from('food-images').getPublicUrl(recipe.image_url).data.publicUrl
    );

    return (
        <div className="recipe-container">
            <button
                className="back-button"
                onClick={() => navigate('/')}
            >
                ← Back to Home
            </button>
            <LangSelect value={viewerLang} onChange={setViewerLang}/>
            <div id="save">
                <button
                    className="save-button"
                    type="button"
                    onClick={() => setIsSaved(!isSaved)}
                >
                   {bookmarkIcon}
                </button>
                    
            </div>
            <div className="postImage">
                {imageUrl && <img src={imageUrl} alt="MainPhoto" />}
               
            </div>

            <div className="informationLine">
                <span id="userNameID">
                    Username: @{recipe.username}
                </span>
                <div className='likes'>
                    <p>{recipe.like_num}</p>
                    <label className="heart-btn">
                    <input type="checkbox" />
                    <svg className="heart-icon" viewBox="0 0 24 24" xmlns="http://w3.org">
                        <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                    </svg>
                    </label>
                </div>
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
                    <div className ="detailsLayout">
                        <div className = "detailLayoutItem">
                            <span>Preparation Time</span>
                            <strong> 20 minutes</strong>
                        </div>

                        <div className = "detailLayoutItem">
                            <span>Cooking Time</span>
                            <strong> 20 minutes</strong>
                        </div>

                        <div className = "detailLayoutItem">
                            <span>Total Time</span>
                            <strong> 40 minutes</strong>
                        </div>

                        <div className = "detailLayoutItem">
                            <span>Difficulty</span>
                            <strong> Easy</strong>
                        </div>

                        <div className = "detailLayoutItem">
                            <span>Servings</span>
                            <strong> 4</strong>
                        </div>

                        <div className = "detailLayoutItem">
                            <span>Country of Origin: </span>
                            <strong> United States</strong>
                        </div>
                    </div>
                    <hr />
                </section>
                
                {/* <section className="instructions">
                    <h2>Recipe Ingredients: </h2>
                    <p>{instructions}</p>
                </section> */}
            </div>
        </div>
    );
}
