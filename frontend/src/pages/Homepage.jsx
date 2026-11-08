import '../css/Homepage.css';
import PostCard from '../components/PostCard';
import veggiePizza from '../images/Veggie-Pizza-12.jpg';
import { useState, useEffect } from 'react';

export default function Homepage() {
        const [posts, setPosts] = useState([]);
        const [loading, setLoading] = useState(true);

        useEffect(() => {
            async function loadPosts(){
                const res = await fetch(`/api/posts/?limit=50&offet=0`);
                const feed = await res.json();
                setPosts(feed);
                setLoading(false);
            }
            loadPosts();
        }, []);

    return (
        <div className="body">
            <h1 id="main-header">Project Food</h1>
            <div className = "main-feed-container">
                <header className = "feed-header">

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
                                    roomId={room.like_num}
                                    roomName={room.image_url}
                                />
                            ))
                        )}
                </main>

                <nav className="bottom-nav">
                    Bottom Nav

                </nav>
            </div>
        </div>
        
    );
}