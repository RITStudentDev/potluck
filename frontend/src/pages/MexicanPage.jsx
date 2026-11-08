import '../css/Homepage.css';
import PostCard from '../components/PostCard';
import { useState, useEffect } from 'react';
import { supabase } from '../util/supabaseConn';
import Navbar from '../components/Navbar';

const API_URL = import.meta.env.VITE_API_URL;


export default function Mexicanpage() {
    const [posts, setPosts] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function loadPosts(){
            const res = await fetch(`${API_URL}/posts/cuisine/mexican?limit=30`);
            const feed = await res.json();
            setPosts(feed);
            setLoading(false);
        }
        loadPosts();
    }, []);

    return (
        <div className="body">
            <Navbar/>
            <div className = "main-feed-container">
                <header className = "feed-header">
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
            </div>

            <footer>
                <h3>Potluck! Many cultures, One Home</h3>
                <h4>Share your culture amongst many others! At home, any recipe deserves to be shared.</h4>

            </footer>
        </div>
        
    );
}