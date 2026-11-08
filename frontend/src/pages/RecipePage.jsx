import '../css/RecipePage.css';
import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import LangSelect, { getInitialLanguage } from '../components/LangSelect';

export default function RecipePage() {
    const { postId } = useParams();
    const [viewerLang, setViewerLang] = useState(getInitialLanguage);

    const [recipe, setRecipe] = useState(null);
    const [loading, setLoading] = useState(true);
    const [translation, setTranslation] = useState(null);
    const [showOriginal, setShowOriginal] = useState(false);
    const { postId } = useParams();
    const [isSaved, setIsSaved] = useState(false);

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
        loadPosts();
    }, []);
    
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

    return (
        <div className="recipe-container">
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
                <img src={recipe.image_url} alt="MainPhoto" />
               
            </div>

            <div className="informationLine">
                <span id="userNameID">
                    Username: @jakebolton
                </span>
                <button className="like-button" type="button">
                    <span>🧡 300</span>
                    {/* <span>300</span> */}
                </button>
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
                
                <section className="instructions">
                    <h2>Recipe Instructions: </h2>
                    <ol>
                        <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</li>
                        <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</li>
                        <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</li>

                    </ol>
                </section>
            </div>
        </div>
    );
}