import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import './App.css';
import Homepage from './pages/Homepage';
import RecipePage from './pages/RecipePage';
import UploadPage from './pages/UploadPage';


function App() {
    
    return (
        <Router>
             <Routes>
                <Route path="/" element={<Homepage />} />
                <Route path="/recipe/:postId" element={<RecipePage />} />
                <Route path="*" element={<Homepage />} />
                <Route path="/upload/" element={<UploadPage />} />
            </Routes>
        </Router>
    );
    
}

export default App;
