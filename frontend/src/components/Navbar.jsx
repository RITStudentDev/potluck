import "../css/Navbar.css"
import TopBar from '../components/TopBar';
import { useNavigate } from "react-router-dom";

export default function Navbar({searchQuery, setSearchQuery}) {
    const navigate = useNavigate();

    return (
        <div className="nav">
            <button onClick={() => navigate('/')}>🏠</button>
             <TopBar
                searchQuery={searchQuery}
                setSearchQuery={setSearchQuery}
            />
            <div className="profile-picture">
                👨🏻‍💼
            </div>
        </div>
    )
}