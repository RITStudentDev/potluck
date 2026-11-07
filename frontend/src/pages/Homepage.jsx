import '../css/Homepage.css';
import veggiePizza from '../images/Veggie-Pizza-12.jpg';

export default function Homepage() {

    return (
        <div className="body">
            <h1 id="main-header">Project Food</h1>
            <div className = "main-feed-container">
                <header className = "feed-header">

                </header>
                
                <main className = "content">
                    <div id="featured-post">
                        <img src={veggiePizza} alt="MainPhoto" />
                         <div className="recipeInfo">
                                    <h3>Recipe Title: Veggie Pizza</h3> 
                                    <p>By: @jakebolton</p>
                                    <p id="description"> A delicious recipe for making a veggie pizza</p>
                        </div>

                    </div>

                    <div className="post-grid">
                        <div className="post">
                            <a>
                                <img src={veggiePizza} alt="Pizza" />
                                <div className="recipeInfo">
                                    <h3>Recipe Title: Veggie Pizza</h3> 
                                    <p>@jakebolton</p>
                                </div>
                            </a>
                         </div>

                        <div className="post">
                            Post 2
                            
                        </div>

                    </div>
                </main>

                <nav className="bottom-nav">
                    Bottom Nav

                </nav>
            </div>
        </div>
        
        
    
        
    );
}