import '../css/Homepage.css';
import PostCard from '../components/PostCard';
import Navbar from '../components/Navbar';
import SideMenu from '../components/SideMenu';
import { useState, useEffect } from 'react';
import { supabase } from '../util/supabaseConn';

const API_URL = import.meta.env.VITE_API_URL;

export default function MexicanPage() {
    const [posts, setPosts] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function loadPosts(){
            const res = await fetch(`${API_URL}/posts/cuisine/chinese?limit=30`);
            const feed = await res.json();
            setPosts(feed);
            setLoading(false);
        }
        loadPosts();
    }, []);

    return (
        <div className="body">
            <Navbar/>

            <div className="page-layout">
                <SideMenu/>

                <div className="main-feed-container">
                    <header className="feed-header">
                        <h1>Chinese</h1>
                    </header>
                    <hr />

                    <main className="content">
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
            </div>
        </div>
    );
}