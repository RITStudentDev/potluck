import '../css/PostCard.css'
import { useNavigate } from 'react-router-dom';
import { useState } from 'react';

function PostCard({ username, likenum, url, id }) {

    const API_URL = import.meta.env.VITE_API_URL;

    const navigate = useNavigate();
    const [likes, setLikes] = useState(likenum);
    const [liked, setLiked] = useState(false);

    const doReroute = () => {
        navigate(`/recipe/${id}`);
    };

    const handleLike = async (e) => {
        if (liked) return;

        setLiked(true);
        setLikes((n) => n + 1);

        try {
            const res = await fetch(`${API_URL}/post/${id}/like`, { method: 'POST' });
            if (!res.ok) throw new Error(`Request failed: ${res.status}`);
        } catch {
            console.error('Like failed:', err);
            setLiked(false);
            setLikes((n) => n - 1);
        }
    };

    return (
        <div className="post-container">
            <img src={url} alt="food" onClick={doReroute}></img>
            <div className="post-data">
                <p>{username}</p>
                <div className="likes">
                    <p>{likes}</p>
                    <label className="heart-btn">
                        <input
                            type="checkbox"
                            checked={liked}
                            onChange={handleLike}
                        />
                        <svg className="heart-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                            <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                        </svg>
                    </label>
                </div>
            </div>
        </div>
    );
}

export default PostCard;