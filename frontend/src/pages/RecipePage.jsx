import '../css/RecipePage.css';
import veggiePizza from '../images/Veggie-Pizza-12.jpg';

export default function RecipePage() {
    return(
        <div className="recipe-container">
            <div className="postImage">
                <img src={veggiePizza} alt="MainPhoto" />
            </div>

            <div className="informationLine">
                <span id="userNameID">
                    Username: @jakebolton
                </span>
                <button className="like-button" type="button">
                    <span>🤍 300</span>
                    {/* <span>300</span> */}
                </button>
                <button className="save-button" type="button" aria-label="Save recipe">
                    <span>📌</span>
                </button>

            </div>

            <div className="descriptionOfPost">
                <h1>Recipe Title</h1>
                <h2></h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
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
                </section>
                <hr></hr>
                <section className="instructions">
                    <h2>Recipe Instructions: </h2>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                </section>
            </div>
        </div>
    );
}
