
import '../css/TopBar.css';

function TopBar() {
    return (
        <header className="top-bar">
            <div className="search-container">
                <span className="search-icon">⌕</span>
                <input
                    type="text"
                    placeholder="Search recipes, people, cuisines..."
                />
            </div>

            <button className="notification-button">
                🔔
            </button>
        </header>
    );
}

export default TopBar;
