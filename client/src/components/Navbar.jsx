import { Link, useLocation } from 'react-router-dom';

/**
 * Navigation bar component
 * Shows the app logo and navigation links
 */
function Navbar() {
  const location = useLocation();

  const isActive = (path) => {
    return location.pathname === path;
  };

  return (
    <nav className="bg-slate-900/95 backdrop-blur-md border-b border-slate-800 sticky top-0 z-50 shadow-lg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Logo */}
          <Link to="/" className="flex items-center space-x-3 group">
            <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-xl flex items-center justify-center shadow-lg shadow-blue-500/30 group-hover:scale-110 transition-transform">
              <span className="text-white font-bold text-xl">P</span>
            </div>
            <span className="text-white font-bold text-xl hidden sm:inline-block">PathPilot AI</span>
          </Link>

          {/* Navigation Links */}
          <div className="flex space-x-2">
            <Link
              to="/"
              className={`px-4 py-2 rounded-xl text-sm font-semibold transition-all ${
                isActive('/')
                  ? 'bg-gradient-to-r from-blue-500 to-purple-600 text-white shadow-lg shadow-blue-500/30'
                  : 'text-slate-300 hover:bg-slate-800 hover:text-white'
              }`}
            >
              Home
            </Link>
            <Link
              to="/generate"
              className={`px-4 py-2 rounded-xl text-sm font-semibold transition-all ${
                isActive('/generate')
                  ? 'bg-gradient-to-r from-blue-500 to-purple-600 text-white shadow-lg shadow-blue-500/30'
                  : 'text-slate-300 hover:bg-slate-800 hover:text-white'
              }`}
            >
              Generate
            </Link>
            <Link
              to="/pathway"
              className={`px-4 py-2 rounded-xl text-sm font-semibold transition-all ${
                isActive('/pathway')
                  ? 'bg-gradient-to-r from-blue-500 to-purple-600 text-white shadow-lg shadow-blue-500/30'
                  : 'text-slate-300 hover:bg-slate-800 hover:text-white'
              }`}
            >
              <span className="hidden sm:inline">My Pathway</span>
              <span className="sm:hidden">Pathway</span>
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;

// Made with Bob
