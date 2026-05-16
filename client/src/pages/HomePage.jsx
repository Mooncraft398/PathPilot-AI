import { Link } from 'react-router-dom';
import { hasPathway } from '../utils/localStorage';

/**
 * Home page - Landing page for PathPilot AI
 */
function HomePage() {
  const pathwayExists = hasPathway();

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 relative overflow-hidden">
      {/* Animated background elements */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-blue-500/5 rounded-full blur-3xl animate-pulse"></div>
        <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-purple-500/5 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '1s' }}></div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 md:py-24 relative z-10">
        {/* Hero Section */}
        <div className="text-center mb-20">
          <div className="inline-flex items-center px-4 py-2 bg-blue-500/10 border border-blue-500/20 rounded-full mb-8">
            <span className="w-2 h-2 bg-blue-500 rounded-full mr-2 animate-pulse"></span>
            <span className="text-blue-400 text-sm font-medium">AI-Powered Career Planning</span>
          </div>
          
          <h1 className="text-5xl md:text-7xl font-bold text-white mb-6 leading-tight">
            Your Personalized
            <span className="block text-transparent bg-clip-text bg-gradient-to-r from-blue-400 via-purple-500 to-pink-500 animate-gradient">
              Career Roadmap
            </span>
          </h1>
          
          <p className="text-xl md:text-2xl text-slate-300 mb-8 max-w-3xl mx-auto leading-relaxed">
            Transform your career goals into actionable learning paths. Get a
            <span className="text-white font-semibold"> personalized, week-by-week roadmap </span>
            tailored to your timeline and learning style.
          </p>

          <p className="text-base text-slate-400 mb-12 max-w-2xl mx-auto">
            From zero to resume-ready in weeks, not years. Build real projects, master in-demand skills, and land your dream job.
          </p>

          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-12">
            <Link
              to="/generate"
              className="group px-8 py-4 bg-gradient-to-r from-blue-500 to-purple-600 text-white font-semibold rounded-xl hover:from-blue-600 hover:to-purple-700 transition-all transform hover:scale-105 shadow-xl hover:shadow-2xl hover:shadow-purple-500/20"
            >
              <span className="flex items-center">
                Generate My Pathway
                <svg className="w-5 h-5 ml-2 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                </svg>
              </span>
            </Link>
            {pathwayExists && (
              <Link
                to="/pathway"
                className="px-8 py-4 bg-slate-800/80 backdrop-blur-sm text-white font-semibold rounded-xl hover:bg-slate-700 transition-all border border-slate-700 hover:border-slate-600 shadow-lg"
              >
                Continue My Journey →
              </Link>
            )}
          </div>

          {/* Trust indicators */}
          <div className="flex flex-wrap justify-center items-center gap-6 text-sm text-slate-400">
            <div className="flex items-center">
              <svg className="w-5 h-5 text-green-500 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
              </svg>
              <span>100% Free to Start</span>
            </div>
            <div className="flex items-center">
              <svg className="w-5 h-5 text-blue-500 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z" />
              </svg>
              <span>Personalized for You</span>
            </div>
            <div className="flex items-center">
              <svg className="w-5 h-5 text-purple-500 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clipRule="evenodd" />
              </svg>
              <span>Results in Weeks</span>
            </div>
          </div>
        </div>

        {/* Features Section */}
        <div className="grid md:grid-cols-3 gap-6 mb-24">
          <div className="group bg-slate-900/50 backdrop-blur-sm p-8 rounded-2xl border border-slate-800 hover:border-blue-500/50 transition-all hover:shadow-xl hover:shadow-blue-500/10 hover:-translate-y-1">
            <div className="w-14 h-14 bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl flex items-center justify-center mb-5 group-hover:scale-110 transition-transform shadow-lg shadow-blue-500/20">
              <svg className="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
              </svg>
            </div>
            <h3 className="text-xl font-bold text-white mb-3">Personalized Plans</h3>
            <p className="text-slate-400 leading-relaxed">
              AI-tailored learning paths based on your career goals, skill level, and available time commitment.
            </p>
          </div>

          <div className="group bg-slate-900/50 backdrop-blur-sm p-8 rounded-2xl border border-slate-800 hover:border-purple-500/50 transition-all hover:shadow-xl hover:shadow-purple-500/10 hover:-translate-y-1">
            <div className="w-14 h-14 bg-gradient-to-br from-purple-500 to-purple-600 rounded-xl flex items-center justify-center mb-5 group-hover:scale-110 transition-transform shadow-lg shadow-purple-500/20">
              <svg className="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
              </svg>
            </div>
            <h3 className="text-xl font-bold text-white mb-3">Curated Resources</h3>
            <p className="text-slate-400 leading-relaxed">
              Access hand-picked learning materials, tutorials, and projects for each step of your journey.
            </p>
          </div>

          <div className="group bg-slate-900/50 backdrop-blur-sm p-8 rounded-2xl border border-slate-800 hover:border-green-500/50 transition-all hover:shadow-xl hover:shadow-green-500/10 hover:-translate-y-1">
            <div className="w-14 h-14 bg-gradient-to-br from-green-500 to-green-600 rounded-xl flex items-center justify-center mb-5 group-hover:scale-110 transition-transform shadow-lg shadow-green-500/20">
              <svg className="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <h3 className="text-xl font-bold text-white mb-3">Track Progress</h3>
            <p className="text-slate-400 leading-relaxed">
              Monitor your learning journey with weekly milestones and build portfolio-ready projects.
            </p>
          </div>
        </div>

        {/* How It Works */}
        <div className="bg-slate-900/30 backdrop-blur-sm rounded-3xl border border-slate-800 p-8 md:p-12">
          <h2 className="text-3xl md:text-4xl font-bold text-white text-center mb-4">How It Works</h2>
          <p className="text-slate-400 text-center mb-12 max-w-2xl mx-auto">
            Get started in minutes with our simple 4-step process
          </p>
          
          <div className="grid md:grid-cols-4 gap-8 relative">
            {/* Connection lines for desktop */}
            <div className="hidden md:block absolute top-8 left-0 right-0 h-0.5 bg-gradient-to-r from-blue-500 via-purple-500 via-green-500 to-orange-500 opacity-20"></div>
            
            <div className="text-center relative">
              <div className="w-16 h-16 bg-gradient-to-br from-blue-500 to-blue-600 text-white rounded-2xl flex items-center justify-center text-2xl font-bold mx-auto mb-4 shadow-lg shadow-blue-500/30 relative z-10">
                1
              </div>
              <h3 className="text-lg font-bold text-white mb-2">Set Your Goal</h3>
              <p className="text-slate-400 text-sm leading-relaxed">Tell us your career target and current skill level</p>
            </div>
            
            <div className="text-center relative">
              <div className="w-16 h-16 bg-gradient-to-br from-purple-500 to-purple-600 text-white rounded-2xl flex items-center justify-center text-2xl font-bold mx-auto mb-4 shadow-lg shadow-purple-500/30 relative z-10">
                2
              </div>
              <h3 className="text-lg font-bold text-white mb-2">Choose Timeline</h3>
              <p className="text-slate-400 text-sm leading-relaxed">Select your available time and learning preferences</p>
            </div>
            
            <div className="text-center relative">
              <div className="w-16 h-16 bg-gradient-to-br from-green-500 to-green-600 text-white rounded-2xl flex items-center justify-center text-2xl font-bold mx-auto mb-4 shadow-lg shadow-green-500/30 relative z-10">
                3
              </div>
              <h3 className="text-lg font-bold text-white mb-2">Get Your Path</h3>
              <p className="text-slate-400 text-sm leading-relaxed">Receive a personalized week-by-week roadmap</p>
            </div>
            
            <div className="text-center relative">
              <div className="w-16 h-16 bg-gradient-to-br from-orange-500 to-orange-600 text-white rounded-2xl flex items-center justify-center text-2xl font-bold mx-auto mb-4 shadow-lg shadow-orange-500/30 relative z-10">
                4
              </div>
              <h3 className="text-lg font-bold text-white mb-2">Start Learning</h3>
              <p className="text-slate-400 text-sm leading-relaxed">Follow your roadmap and build your portfolio</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default HomePage;

// Made with Bob
