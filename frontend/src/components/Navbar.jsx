import "../css/Navbar.css"
import { useNavigate } from "react-router-dom";

export default function Navbar() {
    const navigate = useNavigate();

    return (
        <div className="nav">
            <ul>
                <li><button onClick={() => navigate('/cuisine/chinese')}>Chinese</button></li>
                <li><button onClick={() => navigate('/cuisine/indian')}>Indian</button></li>
                <li><button onClick={() => navigate('/cuisine/mexican')}>Mexican</button></li>
            </ul>
            <div className="profile-picture">
                👨🏻‍💼
            </div>
        </div>
    )
}