import '../css/Homepage.css';
import PostCard from '../components/PostCard';
import veggiePizza from '../images/Veggie-Pizza-12.jpg';
import { useState, useEffect } from 'react';
import { supabase } from '../util/supabaseConn';

const API_URL = import.meta.env.VITE_API_URL;

console.log(`ENV: ${API_URL}`);

export default function Chinesepage() {
    const [posts, setPosts] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function loadPosts(){
            const res = await fetch(`/api/posts/cuisine/chinese?limit=30`);
            const feed = await res.json();
            setPosts(feed);
            setLoading(false);
        }
        loadPosts();
    }, []);

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
                    {loading ? (
                            <p>Loading...</p>
                        ) : posts.length === 0 ? (
                            <p>No posts found</p>
                        ) : (
                            posts.map((post) => (
                                <PostCard
                                    username={post.username}
                                    likenum={post.like_num}
                                    url={supabase.storage.from("food-images").getPublicUrl(post.image_url).data.publicUrl}
                                    id={post.id}
                                    key={post.id}
                                />
                            ))
                        )}
                </main>

                <aside className="side-nav">
                    Filter By Country!
                    <button className="country-filter" type="button" href="/cuisine/mexican">
                        <span className="icon">🌮</span>
                        <span>Mexico</span>
                    </button>

                    <button className="country-filter" type="button" href="/cuisine/chinese">
                        <span className="icon">🏮</span>
                        <span>China</span>
                    </button>

                    <button className="country-filter" type="button" href="/cuisine/indian">
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