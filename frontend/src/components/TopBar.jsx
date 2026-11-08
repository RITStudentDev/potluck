
import '../css/TopBar.css';

function TopBar({ searchQuery, setSearchQuery }) {
    return (
        <header className="top-bar">
            <div className="search-container">
                <span className="search-icon">⌕</span>
                <input
                    type="text"
                    placeholder="Search recipes, people, cuisines..."
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                />
            </div>

            <button className="notification-button">
                🔔
            </button>
        </header>
    );
}

export default TopBar;
