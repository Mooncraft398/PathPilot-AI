import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import GeneratePage from './pages/GeneratePage';
import PathwayPage from './pages/PathwayPage';

/**
 * Main App component with routing
 */
function App() {
  return (
    <Router>
      <div className="min-h-screen bg-slate-950">
        <Navbar />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/generate" element={<GeneratePage />} />
          <Route path="/pathway" element={<PathwayPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

// Made with Bob
