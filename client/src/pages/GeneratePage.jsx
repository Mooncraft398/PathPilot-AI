import PathwayForm from '../components/PathwayForm';

/**
 * Generate page - Contains the pathway generation form
 */
function GeneratePage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-4xl md:text-5xl font-bold text-white mb-4">
            Generate Your Career Pathway
          </h1>
          <p className="text-lg text-slate-300 max-w-2xl mx-auto">
            Tell us about your goals and preferences, and we'll create a personalized
            learning roadmap just for you.
          </p>
        </div>

        {/* Form */}
        <div className="bg-slate-900 rounded-xl border border-slate-800 p-8 shadow-2xl">
          <PathwayForm />
        </div>

        {/* Info Section */}
        <div className="mt-12 grid md:grid-cols-3 gap-6 text-center">
          <div className="bg-slate-900/50 p-6 rounded-lg border border-slate-800">
            <div className="text-3xl font-bold text-blue-500 mb-2">AI-Powered</div>
            <p className="text-slate-400 text-sm">
              Intelligent pathway generation based on your unique profile
            </p>
          </div>
          <div className="bg-slate-900/50 p-6 rounded-lg border border-slate-800">
            <div className="text-3xl font-bold text-purple-500 mb-2">Personalized</div>
            <p className="text-slate-400 text-sm">
              Tailored to your timeline, budget, and learning style
            </p>
          </div>
          <div className="bg-slate-900/50 p-6 rounded-lg border border-slate-800">
            <div className="text-3xl font-bold text-green-500 mb-2">Actionable</div>
            <p className="text-slate-400 text-sm">
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
