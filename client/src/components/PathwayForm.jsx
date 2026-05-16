import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { generateRoadmap, transformRoadmapToPathway } from '../utils/api';
import { savePathway } from '../utils/localStorage';

/**
 * Form component for generating a career pathway
 */
function PathwayForm() {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const [formData, setFormData] = useState({
    goal: '',
    level: 'beginner',
    weeks: 6,
    daysPerWeek: 5,
    hoursPerDay: 2,
    preferences: [],
    budget: 'free-first',
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;

    if (type === 'checkbox') {
      // Handle checkbox for preferences
      setFormData((prev) => ({
        ...prev,
        preferences: checked
          ? [...prev.preferences, value]
          : prev.preferences.filter((pref) => pref !== value),
      }));
    } else {
      setFormData((prev) => ({
        ...prev,
        [name]: type === 'number' ? parseInt(value) : value,
      }));
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      // Validate form
      if (!formData.goal.trim()) {
        throw new Error('Please enter a career goal');
      }

      console.log('🚀 Starting pathway generation with Watsonx.ai...');
      console.log('📋 Form data:', formData);

      // Normalize timeframe to weeks for consistency
      // Backend expects weeks format for accurate planning
      const timeframe = `${formData.weeks} weeks`;

      // Prepare request for Watsonx.ai roadmap endpoint
      const roadmapRequest = {
        careerGoal: formData.goal,
        currentSkills: [], // User hasn't specified current skills in this form
        timeframe: timeframe,
        weeks: formData.weeks  // Send explicit weeks to backend
      };

      console.log('📡 Calling Watsonx.ai roadmap API...');
      console.log('Request:', roadmapRequest);

      // Generate roadmap using Watsonx.ai
      const roadmapResponse = await generateRoadmap(roadmapRequest);

      console.log('=' .repeat(80));
      console.log('✅ RECEIVED ROADMAP FROM BACKEND');
      console.log('=' .repeat(80));
      console.log('📦 Full response:', roadmapResponse);
      console.log('🔑 Response keys:', Object.keys(roadmapResponse));
      console.log('🗺️  Roadmap keys:', Object.keys(roadmapResponse.roadmap || {}));
      console.log('🐙 GitHub projects in response:', roadmapResponse.roadmap?.githubProjects?.length || 0);
      if (roadmapResponse.roadmap?.githubProjects && roadmapResponse.roadmap.githubProjects.length > 0) {
        console.log('🐙 GitHub projects:', roadmapResponse.roadmap.githubProjects);
      }
      console.log('📚 Resources in response:', roadmapResponse.roadmap?.resources?.length || 0);
      console.log('📅 Weekly plans in response:', roadmapResponse.roadmap?.weeklyPlan?.length || 0);
      console.log('=' .repeat(80));

      // Transform the Watsonx.ai response to match frontend expectations
      const pathway = transformRoadmapToPathway(roadmapResponse, {
        ...formData,
        timeframe
      });

      console.log('=' .repeat(80));
      console.log('✅ PATHWAY TRANSFORMATION COMPLETE');
      console.log('=' .repeat(80));
      console.log('📦 Final pathway object:', pathway);
      console.log('🔑 Pathway keys:', Object.keys(pathway));
      console.log('🐙 GitHub projects in pathway:', pathway.githubProjects?.length || 0);
      if (pathway.githubProjects && pathway.githubProjects.length > 0) {
        console.log('🐙 GitHub projects:', pathway.githubProjects);
      }
      console.log('📚 Total resources across weeks:', pathway.weeks?.reduce((sum, w) => sum + (w.resources?.length || 0), 0) || 0);
      console.log('📅 Weeks:', pathway.weeks?.length || 0);
      console.log('=' .repeat(80));

      // Save to localStorage
      savePathway(pathway);
      console.log('💾 Saved pathway to localStorage');
      
      // CRITICAL FIX: Use correct localStorage key 'generatedPathway'
      const savedPathway = JSON.parse(localStorage.getItem('generatedPathway') || '{}');
      console.log('🔍 LOCALSTORAGE VERIFICATION:');
      console.log('   Saved pathway keys:', Object.keys(savedPathway));
      console.log('   githubProjects in saved:', savedPathway.githubProjects?.length || 0);
      console.log('   weeks in saved:', savedPathway.weeks?.length || 0);
      
      if (savedPathway.githubProjects && savedPathway.githubProjects.length > 0) {
        console.log('   First GitHub project:', savedPathway.githubProjects[0]);
      }
      
      // Verify it matches what we tried to save
      if (savedPathway.githubProjects?.length !== pathway.githubProjects?.length) {
        console.error('❌ MISMATCH: Tried to save', pathway.githubProjects?.length, 'but localStorage has', savedPathway.githubProjects?.length);
      } else {
        console.log('✅ localStorage verification passed');
      }

      // Redirect to pathway page
      navigate('/pathway');
    } catch (err) {
      console.error('❌ Error generating pathway:', err);
      console.error('Error details:', {
        message: err.message,
        cause: err.cause,
        stack: err.stack
      });
      setError(err.message || 'Failed to generate pathway. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-8">
      {/* Error Message */}
      {error && (
        <div className="bg-red-500/10 border border-red-500/50 text-red-400 px-5 py-4 rounded-xl flex items-start space-x-3 animate-in fade-in slide-in-from-top-2 duration-300">
          <svg className="w-5 h-5 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
            <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
          </svg>
          <span>{error}</span>
        </div>
      )}

      {/* Career Goal */}
      <div>
        <label htmlFor="goal" className="block text-sm font-semibold text-slate-200 mb-3">
          Career Goal *
        </label>
        <input
          type="text"
          id="goal"
          name="goal"
          value={formData.goal}
          onChange={handleChange}
          placeholder="e.g., Junior Web Developer, Data Analyst, UX Designer"
          className="w-full px-4 py-3.5 bg-slate-800/50 border border-slate-700 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
          required
        />
        <p className="mt-2 text-xs text-slate-500">What role are you aiming for?</p>
      </div>

      {/* Skill Level */}
      <div>
        <label htmlFor="level" className="block text-sm font-semibold text-slate-200 mb-3">
          Current Skill Level *
        </label>
        <select
          id="level"
          name="level"
          value={formData.level}
          onChange={handleChange}
          className="w-full px-4 py-3.5 bg-slate-800/50 border border-slate-700 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all cursor-pointer"
          required
        >
          <option value="beginner">🌱 Beginner - Just starting out</option>
          <option value="intermediate">🚀 Intermediate - Some experience</option>
          <option value="advanced">⭐ Advanced - Experienced learner</option>
        </select>
      </div>

      {/* Timeline */}
      <div>
        <h3 className="text-sm font-semibold text-slate-200 mb-4">Time Commitment *</h3>
        <div className="grid md:grid-cols-3 gap-4">
          <div>
            <label htmlFor="weeks" className="block text-xs font-medium text-slate-400 mb-2">
              Number of Weeks
            </label>
            <input
              type="number"
              id="weeks"
              name="weeks"
              value={formData.weeks}
              onChange={handleChange}
              min="1"
              max="52"
              className="w-full px-4 py-3.5 bg-slate-800/50 border border-slate-700 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-center font-semibold"
              required
            />
          </div>

          <div>
            <label htmlFor="daysPerWeek" className="block text-xs font-medium text-slate-400 mb-2">
              Days per Week
            </label>
            <input
              type="number"
              id="daysPerWeek"
              name="daysPerWeek"
              value={formData.daysPerWeek}
              onChange={handleChange}
              min="1"
              max="7"
              className="w-full px-4 py-3.5 bg-slate-800/50 border border-slate-700 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-center font-semibold"
              required
            />
          </div>

          <div>
            <label htmlFor="hoursPerDay" className="block text-xs font-medium text-slate-400 mb-2">
              Hours per Day
            </label>
            <input
              type="number"
              id="hoursPerDay"
              name="hoursPerDay"
              value={formData.hoursPerDay}
              onChange={handleChange}
              min="1"
              max="24"
              className="w-full px-4 py-3.5 bg-slate-800/50 border border-slate-700 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-center font-semibold"
              required
            />
          </div>
        </div>
        <p className="mt-3 text-xs text-slate-500">
          Total: {formData.weeks * formData.daysPerWeek * formData.hoursPerDay} hours of learning
        </p>
      </div>

      {/* Learning Preferences */}
      <div>
        <label className="block text-sm font-semibold text-slate-200 mb-3">
          Learning Preferences
        </label>
        <p className="text-xs text-slate-500 mb-4">Select all that apply</p>
        <div className="grid md:grid-cols-2 gap-3">
          {[
            { value: 'projects', label: 'Project-Based', icon: '🛠️' },
            { value: 'videos', label: 'Video Tutorials', icon: '🎥' },
            { value: 'reading', label: 'Reading & Docs', icon: '📚' },
            { value: 'interactive', label: 'Interactive', icon: '💻' }
          ].map((pref) => (
            <label
              key={pref.value}
              className={`flex items-center space-x-3 bg-slate-800/50 border rounded-xl px-4 py-3.5 cursor-pointer transition-all ${
                formData.preferences.includes(pref.value)
                  ? 'border-blue-500 bg-blue-500/10'
                  : 'border-slate-700 hover:border-slate-600 hover:bg-slate-800'
              }`}
            >
              <input
                type="checkbox"
                name="preferences"
                value={pref.value}
                checked={formData.preferences.includes(pref.value)}
                onChange={handleChange}
                className="w-5 h-5 text-blue-500 bg-slate-700 border-slate-600 rounded focus:ring-2 focus:ring-blue-500"
              />
              <span className="text-xl">{pref.icon}</span>
              <span className="text-white font-medium">{pref.label}</span>
            </label>
          ))}
        </div>
      </div>

      {/* Budget */}
      <div>
        <label htmlFor="budget" className="block text-sm font-semibold text-slate-200 mb-3">
          Budget Preference *
        </label>
        <select
          id="budget"
          name="budget"
          value={formData.budget}
          onChange={handleChange}
          className="w-full px-4 py-3.5 bg-slate-800/50 border border-slate-700 rounded-xl text-white focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all cursor-pointer"
          required
        >
          <option value="free-first">💚 Free resources first</option>
          <option value="paid-ok">💙 Paid resources OK</option>
          <option value="premium">💎 Premium resources preferred</option>
        </select>
      </div>

      {/* Submit Button */}
      <div className="pt-4">
        <button
          type="submit"
          disabled={loading}
          className="w-full px-6 py-4 bg-gradient-to-r from-blue-500 to-purple-600 text-white font-bold rounded-xl hover:from-blue-600 hover:to-purple-700 transition-all transform hover:scale-[1.02] disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none shadow-xl hover:shadow-2xl hover:shadow-purple-500/30"
        >
          {loading ? (
            <span className="flex items-center justify-center">
              <svg className="animate-spin -ml-1 mr-3 h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              <span className="text-lg">Generating Your Pathway...</span>
            </span>
          ) : (
            <span className="flex items-center justify-center text-lg">
              Generate My Pathway
              <svg className="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
              </svg>
            </span>
          )}
        </button>

        {loading && (
          <p className="text-sm text-slate-400 text-center mt-4 animate-pulse">
            ✨ Creating your personalized learning path... This may take a few seconds.
          </p>
        )}
      </div>
    </form>
  );
}

export default PathwayForm;

// Made with Bob
