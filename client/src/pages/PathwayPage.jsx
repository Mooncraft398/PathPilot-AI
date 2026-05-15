import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { getPathway, clearPathway } from '../utils/localStorage';
import WeekCard from '../components/WeekCard';
import ProgressBar from '../components/ProgressBar';

/**
 * Pathway page - Displays the generated career pathway
 */
function PathwayPage() {
  const navigate = useNavigate();
  // Initialize state directly from localStorage to avoid setState in useEffect
  const [pathway] = useState(() => getPathway());

  const handleClearPathway = () => {
    if (window.confirm('Are you sure you want to clear your current pathway?')) {
      clearPathway();
      navigate('/');
    }
  };

  // If no pathway exists, show message
  if (!pathway) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
          <div className="text-center">
            <div className="w-20 h-20 bg-slate-800 rounded-full flex items-center justify-center mx-auto mb-6">
              <svg className="w-10 h-10 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <h2 className="text-3xl font-bold text-white mb-4">No Pathway Found</h2>
            <p className="text-slate-400 mb-8">
              You haven't generated a career pathway yet.
            </p>
            <Link
              to="/generate"
              className="inline-block px-8 py-4 bg-gradient-to-r from-blue-500 to-purple-600 text-white font-semibold rounded-lg hover:from-blue-600 hover:to-purple-700 transition-all transform hover:scale-105 shadow-lg"
            >
              Generate Your Pathway
            </Link>
          </div>
        </div>
      </div>
    );
  }

  // Calculate progress
  const completedWeeks = pathway.weeks.filter((week) => week.completed).length;
  const totalWeeks = pathway.weeks.length;

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        {/* Header */}
        <div className="mb-8">
          <div className="flex items-start justify-between mb-4">
            <div>
              <h1 className="text-4xl font-bold text-white mb-2">{pathway.title}</h1>
              <p className="text-lg text-slate-300">{pathway.summary}</p>
            </div>
            <button
              onClick={handleClearPathway}
              className="px-4 py-2 bg-slate-800 text-slate-300 rounded-lg hover:bg-slate-700 transition-colors border border-slate-700"
            >
              Clear Pathway
            </button>
          </div>

          {/* Pathway Info */}
          <div className="grid md:grid-cols-3 gap-4 mb-6">
            <div className="bg-slate-900 rounded-lg p-4 border border-slate-800">
              <div className="text-sm text-slate-400 mb-1">Career Goal</div>
              <div className="text-lg font-semibold text-white">{pathway.goal}</div>
            </div>
            <div className="bg-slate-900 rounded-lg p-4 border border-slate-800">
              <div className="text-sm text-slate-400 mb-1">Skill Level</div>
              <div className="text-lg font-semibold text-white capitalize">{pathway.level}</div>
            </div>
            <div className="bg-slate-900 rounded-lg p-4 border border-slate-800">
              <div className="text-sm text-slate-400 mb-1">Time Commitment</div>
              <div className="text-lg font-semibold text-white">{pathway.weeklyTimeCommitment}</div>
            </div>
          </div>

          {/* Progress Bar */}
          <div className="bg-slate-900 rounded-lg p-6 border border-slate-800">
            <ProgressBar completed={completedWeeks} total={totalWeeks} />
          </div>
        </div>

        {/* Weekly Plans */}
        <div className="mb-12">
          <h2 className="text-2xl font-bold text-white mb-6">Weekly Learning Plan</h2>
          <div className="space-y-4">
            {pathway.weeks.map((week) => (
              <WeekCard key={week.weekNumber} week={week} />
            ))}
          </div>
        </div>

        {/* Portfolio Checklist */}
        <div className="mb-12">
          <h2 className="text-2xl font-bold text-white mb-6">Final Portfolio Checklist</h2>
          <div className="bg-slate-900 rounded-xl border border-slate-800 p-6">
            <ul className="space-y-3">
              {pathway.finalPortfolioChecklist.map((item, index) => (
                <li key={index} className="flex items-start space-x-3">
                  <div className="w-6 h-6 bg-slate-800 rounded border border-slate-700 flex items-center justify-center flex-shrink-0 mt-0.5">
                    <svg className="w-4 h-4 text-slate-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                    </svg>
                  </div>
                  <span className="text-slate-300">{item}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>

        {/* Recommended Certifications */}
        {pathway.recommendedCertifications && pathway.recommendedCertifications.length > 0 && (
          <div>
            <h2 className="text-2xl font-bold text-white mb-6">Recommended Certifications</h2>
            <div className="grid md:grid-cols-2 gap-4">
              {pathway.recommendedCertifications.map((cert, index) => (
                <div
                  key={index}
                  className="bg-slate-900 rounded-xl border border-slate-800 p-6"
                >
                  <div className="flex items-start justify-between mb-3">
                    <h3 className="text-lg font-semibold text-white">{cert.name}</h3>
                    <span className={`px-3 py-1 rounded-full text-xs font-medium ${
                      cert.priority === 'essential'
                        ? 'bg-red-500/10 text-red-500 border border-red-500/20'
                        : cert.priority === 'recommended'
                        ? 'bg-yellow-500/10 text-yellow-500 border border-yellow-500/20'
                        : 'bg-blue-500/10 text-blue-500 border border-blue-500/20'
                    }`}>
                      {cert.priority}
                    </span>
                  </div>
                  <p className="text-slate-400 text-sm mb-4">{cert.provider}</p>
                  <div className="flex items-center justify-between text-sm">
                    <span className="text-slate-500">Cost: {cert.cost}</span>
                    <span className="text-slate-500">{cert.timeToComplete}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Action Buttons */}
        <div className="mt-12 flex justify-center space-x-4">
          <Link
            to="/generate"
            className="px-6 py-3 bg-slate-800 text-white font-semibold rounded-lg hover:bg-slate-700 transition-colors border border-slate-700"
          >
            Generate New Pathway
          </Link>
        </div>
      </div>
    </div>
  );
}

export default PathwayPage;

// Made with Bob
