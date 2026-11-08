import '../css/Homepage.css';
import PostCard from '../components/PostCard';
import veggiePizza from '../images/Veggie-Pizza-12.jpg';
import { useState, useEffect } from 'react';
import { supabase } from '../util/supabaseConn';

export default function Homepage() {
    const [posts, setPosts] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function loadPosts(){
            const res = await fetch("/api/posts/?limit=50&offet=0");
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
                    <h1>Project Food</h1>
                    
                </header>
                
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
                                />
                            ))
                        )}
                </main>

                <nav className="bottom-nav">
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
                </nav>
            </div>
        </div>
        
    );
}