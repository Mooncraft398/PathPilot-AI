import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { generatePathway } from '../utils/api';
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

      // Generate pathway
      const pathway = await generatePathway(formData);

      // Save to localStorage
      savePathway(pathway);

      // Redirect to pathway page
      navigate('/pathway');
    } catch (err) {
      setError(err.message || 'Failed to generate pathway. Please try again.');
      console.error('Error generating pathway:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-2xl mx-auto space-y-6">
      {/* Error Message */}
      {error && (
        <div className="bg-red-500/10 border border-red-500 text-red-500 px-4 py-3 rounded-lg">
          {error}
        </div>
      )}

      {/* Career Goal */}
      <div>
        <label htmlFor="goal" className="block text-sm font-medium text-slate-300 mb-2">
          Career Goal *
        </label>
        <input
          type="text"
          id="goal"
          name="goal"
          value={formData.goal}
          onChange={handleChange}
          placeholder="e.g., Junior Web Developer, Data Analyst, UX Designer"
          className="w-full px-4 py-3 bg-slate-800 border border-slate-700 rounded-lg text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        />
      </div>

      {/* Skill Level */}
      <div>
        <label htmlFor="level" className="block text-sm font-medium text-slate-300 mb-2">
          Current Skill Level *
        </label>
        <select
          id="level"
          name="level"
          value={formData.level}
          onChange={handleChange}
          className="w-full px-4 py-3 bg-slate-800 border border-slate-700 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        >
          <option value="beginner">Beginner - Just starting out</option>
          <option value="intermediate">Intermediate - Some experience</option>
          <option value="advanced">Advanced - Experienced learner</option>
        </select>
      </div>

      {/* Timeline */}
      <div className="grid md:grid-cols-3 gap-4">
        <div>
          <label htmlFor="weeks" className="block text-sm font-medium text-slate-300 mb-2">
            Number of Weeks *
          </label>
          <input
            type="number"
            id="weeks"
            name="weeks"
            value={formData.weeks}
            onChange={handleChange}
            min="1"
            max="52"
            className="w-full px-4 py-3 bg-slate-800 border border-slate-700 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        <div>
          <label htmlFor="daysPerWeek" className="block text-sm font-medium text-slate-300 mb-2">
            Days per Week *
          </label>
          <input
            type="number"
            id="daysPerWeek"
            name="daysPerWeek"
            value={formData.daysPerWeek}
            onChange={handleChange}
            min="1"
            max="7"
            className="w-full px-4 py-3 bg-slate-800 border border-slate-700 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>

        <div>
          <label htmlFor="hoursPerDay" className="block text-sm font-medium text-slate-300 mb-2">
            Hours per Day *
          </label>
          <input
            type="number"
            id="hoursPerDay"
            name="hoursPerDay"
            value={formData.hoursPerDay}
            onChange={handleChange}
            min="1"
            max="24"
            className="w-full px-4 py-3 bg-slate-800 border border-slate-700 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
        </div>
      </div>

      {/* Learning Preferences */}
      <div>
        <label className="block text-sm font-medium text-slate-300 mb-3">
          Learning Preferences (select all that apply)
        </label>
        <div className="grid md:grid-cols-2 gap-3">
          {['projects', 'videos', 'reading', 'interactive'].map((pref) => (
            <label
              key={pref}
              className="flex items-center space-x-3 bg-slate-800 border border-slate-700 rounded-lg px-4 py-3 cursor-pointer hover:bg-slate-750 transition-colors"
            >
              <input
                type="checkbox"
                name="preferences"
                value={pref}
                checked={formData.preferences.includes(pref)}
                onChange={handleChange}
                className="w-4 h-4 text-blue-500 bg-slate-700 border-slate-600 rounded focus:ring-blue-500"
              />
              <span className="text-white capitalize">{pref}</span>
            </label>
          ))}
        </div>
      </div>

      {/* Budget */}
      <div>
        <label htmlFor="budget" className="block text-sm font-medium text-slate-300 mb-2">
          Budget Preference *
        </label>
        <select
          id="budget"
          name="budget"
          value={formData.budget}
          onChange={handleChange}
          className="w-full px-4 py-3 bg-slate-800 border border-slate-700 rounded-lg text-white focus:outline-none focus:ring-2 focus:ring-blue-500"
          required
        >
          <option value="free-first">Free resources first</option>
          <option value="paid-ok">Paid resources OK</option>
          <option value="premium">Premium resources preferred</option>
        </select>
      </div>

      {/* Submit Button */}
      <button
        type="submit"
        disabled={loading}
        className="w-full px-6 py-4 bg-gradient-to-r from-blue-500 to-purple-600 text-white font-semibold rounded-lg hover:from-blue-600 hover:to-purple-700 transition-all transform hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none shadow-lg"
      >
        {loading ? (
          <span className="flex items-center justify-center">
            <svg className="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            Generating Your Pathway...
          </span>
        ) : (
          'Generate My Pathway'
        )}
      </button>

      <p className="text-sm text-slate-400 text-center">
        This may take a few seconds. Please don't close this page.
      </p>
    </form>
  );
}

export default PathwayForm;

// Made with Bob
