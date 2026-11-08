import '../css/Homepage.css';
import PostCard from '../components/PostCard';
import veggiePizza from '../images/Veggie-Pizza-12.jpg';
import quesadilla from '../images/quesadillas-2.jpg';
import { Link } from 'react-router-dom';

export default function Homepage() {

    return (
        <div className="body">
            <div className = "main-feed-container">
                <header className = "feed-header">
                    <div className="profile-picture">
                        👨🏻‍💼
                    </div>
                    <h1>Potluck</h1>
                    <h2>"Many Cultures, One Home"</h2>
                </header>
                <hr />
                
                <main className = "content">
                    <div id="featured-post">
                        <img src={veggiePizza} alt="MainPhoto" />
                        <div className="recipeInfo">
                                    <h3>Recipe Title: Veggie Pizza</h3> 
                                    <p>By: @jakebolton</p>
                                    <p id="description"> A delicious recipe for making a veggie pizza</p>
                        </div>
                    </div>

                    {/* <div className="post-grid">
                        <div className="post">
                            <Link className="post" to="/recipe/veggie-pizza">
                                <img src={veggiePizza} alt="Pizza" />
                                <div className="recipeInfo">
                                    <h3>Recipe Title: Veggie Pizza</h3> 
                                    <p>@jakebolton</p>
                                </div>
                            </Link>
                         </div>

                        <div className="post">
                            <Link className="post" to="/recipe/veggie-pizza">
                                <img src={quesadilla} alt="Quesadilla" />
                                <div className="recipeInfo">
                                    <h3>Recipe Title: Cheese Quesadillas</h3> 
                                    <p>@vincent-vue</p>
                                </div>
                            </Link>
                            
                        </div>

                    </div> */}
                    
                    <PostCard
                        username={"@Xx_shadow_xX"}
                        likenum={2}
                        url={veggiePizza}
                    />

                    <PostCard
                        username={"@jake-bolton"}
                        likenum={2}
                        url={quesadilla}
                    />

                </main>

                <aside className="side-nav">
                    Filter By Country!
                    <button className="country-filter" type="button">
                        <span className="icon">🌮</span>
                        <span>Mexico</span>
                    </button>

                    <button className="country-filter" type="button">
                        <span className="icon">🏮</span>
                        <span>China</span>
                    </button>

                    <button className="country-filter" type="button">
                        <span className="icon">🪔</span>
                        <span>India</span>
                    </button>
                </aside>
            </div>

            <footer>
                <h3>Potluck! Many cultures, One Home</h3>
                <h4>Share your culture amongst many others! At home, any recipe deserves to be shared.</h4>

            </footer>
        </div>
        
    );
}