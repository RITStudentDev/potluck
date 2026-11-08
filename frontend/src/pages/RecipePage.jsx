import '../css/RecipePage.css';
import veggiePizza from '../images/Veggie-Pizza-12.jpg';
import PostCard from '../components/PostCard';
import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

export default function RecipePage() {

    const [recipe, setRecipe] = useState(true);
    const [loading, setLoading] = useState(true);
    const { postId } = useParams();
    const [isSaved, setIsSaved] = useState(false);

    useEffect(() => {
        async function loadPosts(){
            const res = await fetch(`/api/post/${postId}`);
            const restaurant = await res.json();
            setRecipe(restaurant);
            setLoading(false);
        }
        loadPosts();
    }, []);
    
    let bookmarkIcon;

    if (isSaved === true) {
        bookmarkIcon = "⛊";
    }
    else {
        bookmarkIcon = "⛉";
    }

    return(
        <div className="recipe-container">
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
                <p>{recipe.description}</p>
                <section className="recipeDetails">
                    <h2>Recipe Details</h2>
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
