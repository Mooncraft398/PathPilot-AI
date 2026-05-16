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
    <div className={`bg-slate-900/50 backdrop-blur-sm rounded-2xl border overflow-hidden transition-all ${
      week.completed
        ? 'border-green-500/30 shadow-lg shadow-green-500/10'
        : 'border-slate-800 hover:border-slate-700'
    }`}>
      {/* Week Header */}
      <div
        className="p-6 cursor-pointer hover:bg-slate-800/30 transition-all group"
        onClick={() => setIsExpanded(!isExpanded)}
      >
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4 flex-1">
            {/* Checkbox */}
            <div
              className="flex-shrink-0"
              onClick={handleCheckboxClick}
            >
              <div className={`w-7 h-7 rounded-lg border-2 flex items-center justify-center cursor-pointer transition-all ${
                week.completed
                  ? 'bg-gradient-to-br from-green-500 to-green-600 border-green-500 shadow-lg shadow-green-500/30'
                  : 'border-slate-600 hover:border-slate-500 hover:bg-slate-800'
              }`}>
                {week.completed && (
                  <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={3} d="M5 13l4 4L19 7" />
                  </svg>
                )}
              </div>
            </div>
            
            <div className="w-14 h-14 bg-gradient-to-br from-blue-500 to-purple-600 rounded-xl flex items-center justify-center shadow-lg shadow-blue-500/20 group-hover:scale-105 transition-transform">
              <span className="text-white font-bold text-xl">{week.weekNumber}</span>
            </div>
            
            <div className="flex-1 min-w-0">
              <h3 className="text-xl font-bold text-white mb-1 truncate">{week.title}</h3>
              <p className="text-sm text-slate-400">Week {week.weekNumber} • {week.objectives.length} objectives</p>
            </div>
          </div>
          
          <div className="flex items-center space-x-3 ml-4">
            {week.completed && (
              <span className="hidden sm:inline-flex px-3 py-1.5 bg-green-500/10 text-green-400 text-xs font-bold rounded-full border border-green-500/30">
                ✓ Completed
              </span>
            )}
            {isExpanded && (
              <span className="hidden md:inline-flex px-3 py-1.5 bg-blue-500/10 text-blue-400 text-xs font-medium rounded-full border border-blue-500/20">
                Expanded
              </span>
            )}
            <svg
              className={`w-6 h-6 text-slate-400 transition-transform flex-shrink-0 ${
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
        <div className="border-t border-slate-800 p-6 space-y-8 bg-slate-900/30">
          {/* Objectives */}
          <div>
            <h4 className="text-lg font-bold text-white mb-4 flex items-center">
              <div className="w-8 h-8 bg-blue-500/10 rounded-lg flex items-center justify-center mr-3">
                <svg className="w-4 h-4 text-blue-400" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z" />
                  <path fillRule="evenodd" d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z" clipRule="evenodd" />
                </svg>
              </div>
              Learning Objectives
            </h4>
            <ul className="space-y-3">
              {week.objectives.map((objective, index) => (
                <li key={index} className="flex items-start space-x-3 p-3 bg-slate-800/50 rounded-xl hover:bg-slate-800 transition-colors">
                  <svg className="w-5 h-5 text-blue-400 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                  </svg>
                  <span className="text-slate-200 leading-relaxed">{objective}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* Daily Plan */}
          <div>
            <h4 className="text-lg font-bold text-white mb-4 flex items-center">
              <div className="w-8 h-8 bg-purple-500/10 rounded-lg flex items-center justify-center mr-3">
                <svg className="w-4 h-4 text-purple-400" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clipRule="evenodd" />
                </svg>
              </div>
              Daily Plan
            </h4>
            <div className="space-y-3">
              {week.dailyPlan.map((day) => (
                <div key={day.day} className="bg-slate-800/50 backdrop-blur-sm rounded-xl p-5 border border-slate-700 hover:border-slate-600 transition-all">
                  <div className="flex items-center justify-between mb-3">
                    <span className="font-bold text-white flex items-center">
                      <span className="w-8 h-8 bg-gradient-to-br from-purple-500 to-purple-600 rounded-lg flex items-center justify-center text-sm mr-3">
                        {day.day}
                      </span>
                      {day.focus}
                    </span>
                    <span className="px-3 py-1 bg-purple-500/10 text-purple-400 text-xs font-bold rounded-full border border-purple-500/20">
                      {day.estimatedHours}h
                    </span>
                  </div>
                  <ul className="space-y-2 text-sm text-slate-300">
                    {day.tasks.map((task, index) => (
                      <li key={index} className="flex items-start space-x-2 pl-11">
                        <span className="text-purple-400 font-bold">•</span>
                        <span className="leading-relaxed">{task}</span>
                      </li>
                    ))}
                  </ul>
                </div>
              ))}
            </div>
          </div>

          {/* Resources */}
          <div>
            <h4 className="text-lg font-bold text-white mb-4 flex items-center">
              <div className="w-8 h-8 bg-green-500/10 rounded-lg flex items-center justify-center mr-3">
                <svg className="w-4 h-4 text-green-400" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M9 4.804A7.968 7.968 0 005.5 4c-1.255 0-2.443.29-3.5.804v10A7.969 7.969 0 015.5 14c1.669 0 3.218.51 4.5 1.385A7.962 7.962 0 0114.5 14c1.255 0 2.443.29 3.5.804v-10A7.968 7.968 0 0014.5 4c-1.255 0-2.443.29-3.5.804V12a1 1 0 11-2 0V4.804z" />
                </svg>
              </div>
              Learning Resources
            </h4>
            <div className="grid md:grid-cols-2 gap-4">
              {week.resources.map((resource, index) => (
                <ResourceCard key={index} resource={resource} />
              ))}
            </div>
          </div>

          {/* Guided Project */}
          <div>
            <h4 className="text-lg font-bold text-white mb-4 flex items-center">
              <div className="w-8 h-8 bg-orange-500/10 rounded-lg flex items-center justify-center mr-3">
                <svg className="w-4 h-4 text-orange-400" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M12.316 3.051a1 1 0 01.633 1.265l-4 12a1 1 0 11-1.898-.632l4-12a1 1 0 011.265-.633zM5.707 6.293a1 1 0 010 1.414L3.414 10l2.293 2.293a1 1 0 11-1.414 1.414l-3-3a1 1 0 010-1.414l3-3a1 1 0 011.414 0zm8.586 0a1 1 0 011.414 0l3 3a1 1 0 010 1.414l-3 3a1 1 0 11-1.414-1.414L16.586 10l-2.293-2.293a1 1 0 010-1.414z" clipRule="evenodd" />
                </svg>
              </div>
              Guided Project
            </h4>
            <ProjectCard project={week.guidedProject} />
          </div>

          {/* Resume Bullet */}
          <div className="bg-gradient-to-r from-blue-500/10 via-purple-500/10 to-pink-500/10 border border-blue-500/30 rounded-xl p-5">
            <div className="flex items-start space-x-3">
              <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-lg flex items-center justify-center flex-shrink-0">
                <svg className="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clipRule="evenodd" />
                </svg>
              </div>
              <div className="flex-1">
                <h4 className="text-sm font-bold text-blue-400 mb-2">Resume Bullet Point</h4>
                <p className="text-white leading-relaxed">{week.resumeBullet}</p>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default WeekCard;

// Made with Bob
