import '../css/Homepage.css';
import PostCard from '../components/PostCard';
import veggiePizza from '../images/Veggie-Pizza-12.jpg';

export default function Homepage() {

    return (
        <div className="body">
            <h1 id="main-header">Project Food</h1>
            <div className = "main-feed-container">
                <header className = "feed-header">

                </header>
                
                <main className = "content">
                    <PostCard
                        username={"Xx_shadow_xX"}
                        likenum={2}
                        url={veggiePizza}
                    />
                </main>

                <nav className="bottom-nav">
                    Bottom Nav

                </nav>
            </div>
        </div>
        
    );
}