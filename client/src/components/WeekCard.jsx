import { useState } from 'react';
import ResourceCard from './ResourceCard';
import ProjectCard from './ProjectCard';

/**
 * Week card component - Displays a single week's learning plan
 */
function WeekCard({ week, onToggleComplete }) {
  const [isExpanded, setIsExpanded] = useState(false);

  const handleCheckboxClick = (e) => {
    e.stopPropagation(); // Prevent expanding/collapsing when clicking checkbox
    onToggleComplete(week.weekNumber);
  };

  return (
    <div className="bg-slate-900 rounded-xl border border-slate-800 overflow-hidden">
      {/* Week Header */}
      <div
        className="p-6 cursor-pointer hover:bg-slate-800/50 transition-colors"
        onClick={() => setIsExpanded(!isExpanded)}
      >
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            {/* Checkbox */}
            <div
              className="flex-shrink-0"
              onClick={handleCheckboxClick}
            >
              <div className={`w-6 h-6 rounded border-2 flex items-center justify-center cursor-pointer transition-all ${
                week.completed
                  ? 'bg-green-500 border-green-500'
                  : 'border-slate-600 hover:border-slate-500'
              }`}>
                {week.completed && (
                  <svg className="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
                  </svg>
                )}
              </div>
            </div>
            <div className="w-12 h-12 bg-gradient-to-br from-blue-500 to-purple-600 rounded-lg flex items-center justify-center">
              <span className="text-white font-bold text-lg">{week.weekNumber}</span>
            </div>
            <div>
              <h3 className="text-xl font-semibold text-white">{week.title}</h3>
              <p className="text-sm text-slate-400">Week {week.weekNumber}</p>
            </div>
          </div>
          <div className="flex items-center space-x-4">
            {week.completed && (
              <span className="px-3 py-1 bg-green-500/10 text-green-500 text-sm font-medium rounded-full border border-green-500/20">
                Completed
              </span>
            )}
            <svg
              className={`w-6 h-6 text-slate-400 transition-transform ${
                isExpanded ? 'rotate-180' : ''
              }`}
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
            </svg>
          </div>
        </div>
      </div>

      {/* Week Content (Expandable) */}
      {isExpanded && (
        <div className="border-t border-slate-800 p-6 space-y-6">
          {/* Objectives */}
          <div>
            <h4 className="text-lg font-semibold text-white mb-3">Learning Objectives</h4>
            <ul className="space-y-2">
              {week.objectives.map((objective, index) => (
                <li key={index} className="flex items-start space-x-2 text-slate-300">
                  <svg className="w-5 h-5 text-blue-500 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                  </svg>
                  <span>{objective}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* Daily Plan */}
          <div>
            <h4 className="text-lg font-semibold text-white mb-3">Daily Plan</h4>
            <div className="space-y-3">
              {week.dailyPlan.map((day) => (
                <div key={day.day} className="bg-slate-800 rounded-lg p-4">
                  <div className="flex items-center justify-between mb-2">
                    <span className="font-medium text-white">Day {day.day}: {day.focus}</span>
                    <span className="text-sm text-slate-400">{day.estimatedHours}h</span>
                  </div>
                  <ul className="space-y-1 text-sm text-slate-300">
                    {day.tasks.map((task, index) => (
                      <li key={index} className="flex items-start space-x-2">
                        <span className="text-slate-500">•</span>
                        <span>{task}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              ))}
            </div>
          </div>

          {/* Resources */}
          <div>
            <h4 className="text-lg font-semibold text-white mb-3">Learning Resources</h4>
            <div className="grid md:grid-cols-2 gap-4">
              {week.resources.map((resource, index) => (
                <ResourceCard key={index} resource={resource} />
              ))}
            </div>
          </div>

          {/* Guided Project */}
          <div>
            <h4 className="text-lg font-semibold text-white mb-3">Guided Project</h4>
            <ProjectCard project={week.guidedProject} />
          </div>

          {/* Resume Bullet */}
          <div className="bg-gradient-to-r from-blue-500/10 to-purple-600/10 border border-blue-500/20 rounded-lg p-4">
            <h4 className="text-sm font-semibold text-blue-400 mb-2">Resume Bullet Point</h4>
            <p className="text-white">{week.resumeBullet}</p>
          </div>
        </div>
      )}
    </div>
  );
}

export default WeekCard;

// Made with Bob
