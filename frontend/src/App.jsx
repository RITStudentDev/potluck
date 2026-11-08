import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import './App.css';
import Homepage from './pages/Homepage';
import RecipePage from './pages/RecipePage';
import Chinesepage from './pages/ChinesePage';
import Mexicanpage from './pages/MexicanPage';
import Indianpage from './pages/IndianPage';


function App() {
    
    return (
        <Router>
             <Routes>
                <Route path="/" element={<Homepage />} />
                <Route path="/cuisine/chinese" element={<Chinesepage />} />
                <Route path="/cuisine/mexican" element={<Mexicanpage />} />
                <Route path="/cuisine/indian" element={<Indianpage />} />
                <Route path="/recipe/:postId" element={<RecipePage />} />
                <Route path="*" element={<Homepage />} />
            </Routes>
        </Router>
    );
    
}

export default App;
