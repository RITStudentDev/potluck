import '../css/Homepage.css';
import PostCard from '../components/PostCard';
import Navbar from '../components/Navbar';
import SideMenu from '../components/SideMenu';
import veggiePizza from '../images/Veggie-Pizza-12.jpg';
import { useState, useEffect } from 'react';
import { supabase } from '../util/supabaseConn';

const API_URL = import.meta.env.VITE_API_URL;

export default function Homepage() {
    const [posts, setPosts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [searchQuery, setSearchQuery] = useState('');

    useEffect(() => {
        async function loadPosts(){
            const res = await fetch(`${API_URL}/posts/?limit=50&offset=0`);
            const feed = await res.json();
            setPosts(feed);
            setLoading(false);
        }
        loadPosts();
    }, []);

    // Filter posts based on username
    const filteredPosts = posts.filter((post) =>
        (post.username ?? '').toLowerCase().includes(searchQuery.toLowerCase())
    );

    return (
        <div className="body">
            <Navbar
                searchQuery={searchQuery}
                setSearchQuery={setSearchQuery}
            />

            <div className="page-layout">
                <SideMenu/>

                <div className="main-feed-container">
                    <header className="feed-header">
                        <h1>Potluck</h1>
                    </header>
                    <hr />
                    <h1 id="featured-recipe-text">Featured Recipe Of The Day!</h1>

                    <main className="content">
                        <div id="featured-post">
                            <img src={veggiePizza} alt="MainPhoto" />
                            <div className="recipeInfo">
                                <h3>Recipe Title: Veggie Pizza</h3>
                                <p>By: @jakebolton</p>
                                <p id="description"> A delicious recipe for making a veggie pizza</p>
                            </div>
                        </div>

                        <hr className="feed-divider" />

                        {loading ? (
                            <p>Loading...</p>
                        ) : filteredPosts.length === 0 ? (
                            <p>No posts found</p>
                        ) : (
                            filteredPosts.map((post) => (
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