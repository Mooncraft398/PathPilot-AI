import PathwayForm from '../components/PathwayForm';

/**
 * Generate page - Contains the pathway generation form
 */
function GeneratePage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 relative overflow-hidden">
      {/* Animated background elements */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-1/3 right-1/4 w-96 h-96 bg-blue-500/5 rounded-full blur-3xl"></div>
        <div className="absolute bottom-1/3 left-1/4 w-96 h-96 bg-purple-500/5 rounded-full blur-3xl"></div>
      </div>

      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12 relative z-10">
        {/* Header */}
        <div className="text-center mb-12">
          <div className="inline-flex items-center px-4 py-2 bg-gradient-to-r from-blue-500/10 to-purple-500/10 border border-blue-500/20 rounded-full mb-6">
            <svg className="w-4 h-4 text-blue-400 mr-2" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clipRule="evenodd" />
            </svg>
            <span className="text-blue-400 text-sm font-medium">Powered by AI</span>
          </div>
          
          <h1 className="text-4xl md:text-5xl font-bold text-white mb-4">
            Generate Your
            <span className="block text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-600">
              Career Pathway
            </span>
          </h1>
          
          <p className="text-lg text-slate-300 max-w-2xl mx-auto leading-relaxed">
            Tell us about your goals and preferences, and we'll create a personalized
            learning roadmap tailored just for you.
          </p>
        </div>

        {/* Form */}
        <div className="bg-slate-900/80 backdrop-blur-sm rounded-2xl border border-slate-800 p-8 md:p-10 shadow-2xl">
          <PathwayForm />
        </div>

        {/* Info Section */}
        <div className="mt-12 grid md:grid-cols-3 gap-6">
          <div className="group bg-slate-900/50 backdrop-blur-sm p-6 rounded-xl border border-slate-800 hover:border-blue-500/50 transition-all text-center">
            <div className="w-12 h-12 bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform shadow-lg shadow-blue-500/20">
              <svg className="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M11.3 1.046A1 1 0 0112 2v5h4a1 1 0 01.82 1.573l-7 10A1 1 0 018 18v-5H4a1 1 0 01-.82-1.573l7-10a1 1 0 011.12-.38z" clipRule="evenodd" />
              </svg>
            </div>
            <div className="text-2xl font-bold text-white mb-2">AI-Powered</div>
            <p className="text-slate-400 text-sm leading-relaxed">
              Intelligent pathway generation based on your unique profile
            </p>
          </div>
          
          <div className="group bg-slate-900/50 backdrop-blur-sm p-6 rounded-xl border border-slate-800 hover:border-purple-500/50 transition-all text-center">
            <div className="w-12 h-12 bg-gradient-to-br from-purple-500 to-purple-600 rounded-xl flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform shadow-lg shadow-purple-500/20">
              <svg className="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20">
                <path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z" />
              </svg>
            </div>
            <div className="text-2xl font-bold text-white mb-2">Personalized</div>
            <p className="text-slate-400 text-sm leading-relaxed">
              Tailored to your timeline, budget, and learning style
            </p>
          </div>
          
          <div className="group bg-slate-900/50 backdrop-blur-sm p-6 rounded-xl border border-slate-800 hover:border-green-500/50 transition-all text-center">
            <div className="w-12 h-12 bg-gradient-to-br from-green-500 to-green-600 rounded-xl flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform shadow-lg shadow-green-500/20">
              <svg className="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clipRule="evenodd" />
              </svg>
            </div>
            <div className="text-2xl font-bold text-white mb-2">Actionable</div>
            <p className="text-slate-400 text-sm leading-relaxed">
              Week-by-week plans with resources and projects
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default GeneratePage;

// Made with Bob
