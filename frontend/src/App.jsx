import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import './App.css';
import Homepage from './pages/Homepage';
import RecipePage from './pages/RecipePage';


function App() {
    
    return (
        <Router>
             <Routes>
                <Route path="/" element={<Homepage />} />
                <Route path="/recipe/:postid" element={<RecipePage />} />
                <Route path="*" element={<Homepage />} />
            </Routes>
        </Router>
    );
    
}

export default App;
