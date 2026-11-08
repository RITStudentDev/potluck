
import "../css/SideMenu.css";
import { useNavigate, useLocation } from "react-router-dom";

export default function SideMenu() {
    const navigate = useNavigate();
    const location = useLocation();

    const cuisines = [
        { name: "Chinese", icon: "🥢", path: "/cuisine/chinese" },
        { name: "Indian", icon: "🍛", path: "/cuisine/indian" },
        { name: "Mexican", icon: "🌮", path: "/cuisine/mexican" }
    ];

    const exploreItems = [
        { name: "Breakfast", icon: "🍳" },
        { name: "Street Food", icon: "🥙" },
        { name: "Desserts", icon: "🍰" },
        { name: "Vegetarian", icon: "🥑" },
    ];

    const popularTags = [
        "Homemade",
        "Traditional",
        "Spicy",
        "Comfort Food",
    ];

    return (
        <aside className="side-menu">
            <div className="side-menu-header">
                <span className="side-menu-eyebrow">DISCOVER THE WORLD</span>
                <h2>Food & Culture</h2>
            </div>

            <hr />

            <section className="side-menu-section">
                <div className="side-menu-section-heading">
                    <h3>Featured Cuisines</h3>
                </div>

                <ul className="side-menu-list">
                    {cuisines.map((cuisine) => (
                        <li key={cuisine.name}>
                            <button
                                className={
                                    location.pathname === cuisine.path
                                        ? "side-menu-button active"
                                        : "side-menu-button"
                                }
                                onClick={() => navigate(cuisine.path)}
                            >
                                <span className="side-menu-icon">
                                    {cuisine.icon}
                                </span>
                                <span>{cuisine.name}</span>
                                <span className="side-menu-arrow">›</span>
                            </button>
                        </li>
                    ))}
                </ul>
            </section>

            <hr />
            <section className="side-menu-section">
                <div className="side-menu-section-heading">
                    <h3>Explore Food</h3>
                </div>

                <ul className="side-menu-list">
                    {exploreItems.map((item) => (
                        <li key={item.name}>
                            <button
                                className="side-menu-button"
                                onClick={() =>
                                    navigate(
                                        `/explore/${item.name.toLowerCase().replace(" ", "-")}`
                                    )
                                }
                            >
                                <span className="side-menu-icon">
                                    {item.icon}
                                </span>
                                <span>{item.name}</span>
                                <span className="side-menu-arrow">›</span>
                            </button>
                        </li>
                    ))}
                </ul>
            </section>

            <hr />

            <section className="side-menu-community">
                <div className="community-icon">🌍</div>
                <h3>Share Your Culture</h3>
                <p>
                    Have a family recipe or a dish worth sharing?
                    Let the world discover it.
                </p>
                <button
                    onClick={() => navigate("/create-recipe")}
                >
                    Share a Recipe +
                </button>
            </section>
        </aside>
    );
}
