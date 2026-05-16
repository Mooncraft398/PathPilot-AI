import { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { getPathway, clearPathway, updatePathway } from '../utils/localStorage';
import { adaptPathway, searchUSAJobs } from '../utils/api';
import WeekCard from '../components/WeekCard';
import ProgressBar from '../components/ProgressBar';
import JobCard from '../components/JobCard';

/**
 * Pathway page - Displays the generated career pathway
 */
function PathwayPage() {
  const navigate = useNavigate();
  // Initialize state directly from localStorage to avoid setState in useEffect
  const [pathway, setPathway] = useState(() => getPathway());
  const [feedback, setFeedback] = useState('');
  const [isAdapting, setIsAdapting] = useState(false);
  const [adaptError, setAdaptError] = useState(null);
  const [showAdaptSection, setShowAdaptSection] = useState(false);
  
  // USAJOBS state
  const [jobsData, setJobsData] = useState(null);
  const [jobsLoading, setJobsLoading] = useState(false);
  const [jobsError, setJobsError] = useState(null);
  const [jobLocation, setJobLocation] = useState('');

  const handleClearPathway = () => {
    if (window.confirm('Are you sure you want to clear your current pathway?')) {
      clearPathway();
      navigate('/');
    }
  };

  const handleToggleWeekComplete = (weekNumber) => {
    if (!pathway) return;

    // Create updated pathway with toggled week completion
    const updatedPathway = {
      ...pathway,
      weeks: pathway.weeks.map(week =>
        week.weekNumber === weekNumber
          ? { ...week, completed: !week.completed }
          : week
      )
    };

    // Update state and localStorage
    setPathway(updatedPathway);
    updatePathway(updatedPathway);
  };

  const handleAdaptPathway = async () => {
    if (!feedback.trim()) {
      setAdaptError('Please enter your feedback');
      return;
    }

    setIsAdapting(true);
    setAdaptError(null);

    try {
      console.log('🔄 Adapting pathway with feedback:', feedback);
      console.log('📋 Current pathway before adaptation:', pathway);
      
      const adaptedPathway = await adaptPathway(pathway, feedback);
      
      console.log('✅ Received adapted pathway from API:', adaptedPathway);
      console.log('⏰ New weeklyTimeCommitment:', adaptedPathway.weeklyTimeCommitment);
      
      setPathway(adaptedPathway);
      updatePathway(adaptedPathway);
      
      console.log('💾 Saved to localStorage and updated state');
      
      setFeedback('');
      setShowAdaptSection(false);
      // Show success message briefly
      alert('Pathway adapted successfully! Check the Time Commitment field.');
    } catch (error) {
      console.error('❌ Error adapting pathway:', error);
      setAdaptError(error.message || 'Failed to adapt pathway');
    } finally {
      setIsAdapting(false);
    }
  };

  const handleSearchJobs = async () => {
    if (!pathway?.goal) return;
    
    setJobsLoading(true);
    setJobsError(null);
    
    try {
      const result = await searchUSAJobs(pathway.goal, jobLocation || null);
      setJobsData(result);
    } catch (error) {
      console.error('Error searching jobs:', error);
      setJobsError(error.message || 'Failed to search jobs');
    } finally {
      setJobsLoading(false);
    }
  };

  // Auto-search jobs when pathway loads
  useEffect(() => {
    if (pathway?.goal && !jobsData) {
      handleSearchJobs();
    }
  }, [pathway?.goal]);

  // If no pathway exists, show message
  if (!pathway) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 flex items-center justify-center">
        <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <div className="bg-slate-900/50 backdrop-blur-sm rounded-3xl border border-slate-800 p-12">
            <div className="w-24 h-24 bg-gradient-to-br from-slate-800 to-slate-900 rounded-2xl flex items-center justify-center mx-auto mb-6 shadow-xl">
              <svg className="w-12 h-12 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <h2 className="text-3xl md:text-4xl font-bold text-white mb-4">No Pathway Yet</h2>
            <p className="text-lg text-slate-400 mb-8 leading-relaxed">
              You haven't generated a career pathway yet. Let's create your personalized learning roadmap!
            </p>
            <Link
              to="/generate"
              className="inline-flex items-center px-8 py-4 bg-gradient-to-r from-blue-500 to-purple-600 text-white font-bold rounded-xl hover:from-blue-600 hover:to-purple-700 transition-all transform hover:scale-105 shadow-xl hover:shadow-2xl hover:shadow-purple-500/30"
            >
              Generate Your Pathway
              <svg className="w-5 h-5 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
              </svg>
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
    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 relative overflow-hidden">
      {/* Animated background */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-1/4 right-1/3 w-96 h-96 bg-blue-500/5 rounded-full blur-3xl"></div>
        <div className="absolute bottom-1/4 left-1/3 w-96 h-96 bg-purple-500/5 rounded-full blur-3xl"></div>
      </div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 relative z-10">
        {/* Header */}
        <div className="mb-10">
          <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-4 mb-6">
            <div className="flex-1">
              <div className="inline-flex items-center px-3 py-1 bg-gradient-to-r from-blue-500/10 to-purple-500/10 border border-blue-500/20 rounded-full mb-4">
                <span className="w-2 h-2 bg-green-500 rounded-full mr-2 animate-pulse"></span>
                <span className="text-green-400 text-xs font-medium">Active Pathway</span>
              </div>
              <h1 className="text-4xl md:text-5xl font-bold text-white mb-3 leading-tight">{pathway.title}</h1>
              <p className="text-lg text-slate-300 leading-relaxed">{pathway.summary}</p>
            </div>
            <button
              onClick={handleClearPathway}
              className="px-5 py-2.5 bg-slate-800/80 backdrop-blur-sm text-slate-300 rounded-xl hover:bg-slate-700 transition-all border border-slate-700 hover:border-slate-600 flex items-center space-x-2 self-start"
            >
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
              </svg>
              <span>Clear</span>
            </button>
          </div>

          {/* Pathway Info Cards */}
          <div className="grid md:grid-cols-3 gap-4 mb-6">
            <div className="group bg-slate-900/50 backdrop-blur-sm rounded-xl p-5 border border-slate-800 hover:border-blue-500/50 transition-all">
              <div className="flex items-center space-x-3 mb-2">
                <div className="w-10 h-10 bg-gradient-to-br from-blue-500 to-blue-600 rounded-lg flex items-center justify-center">
                  <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
                  </svg>
                </div>
                <div className="text-xs font-medium text-slate-400">Career Goal</div>
              </div>
              <div className="text-xl font-bold text-white">{pathway.goal}</div>
            </div>
            
            <div className="group bg-slate-900/50 backdrop-blur-sm rounded-xl p-5 border border-slate-800 hover:border-purple-500/50 transition-all">
              <div className="flex items-center space-x-3 mb-2">
                <div className="w-10 h-10 bg-gradient-to-br from-purple-500 to-purple-600 rounded-lg flex items-center justify-center">
                  <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
                  </svg>
                </div>
                <div className="text-xs font-medium text-slate-400">Skill Level</div>
              </div>
              <div className="text-xl font-bold text-white capitalize">{pathway.level}</div>
            </div>
            
            <div className="group bg-slate-900/50 backdrop-blur-sm rounded-xl p-5 border border-slate-800 hover:border-green-500/50 transition-all">
              <div className="flex items-center space-x-3 mb-2">
                <div className="w-10 h-10 bg-gradient-to-br from-green-500 to-green-600 rounded-lg flex items-center justify-center">
                  <svg className="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                  </svg>
                </div>
                <div className="text-xs font-medium text-slate-400">Time Commitment</div>
              </div>
              <div className="text-xl font-bold text-white">{pathway.weeklyTimeCommitment}</div>
            </div>
          </div>

          {/* Progress Section */}
          <div className="bg-gradient-to-br from-slate-900/80 to-slate-900/50 backdrop-blur-sm rounded-2xl p-6 md:p-8 border border-slate-800 shadow-xl">
            <div className="flex items-center justify-between mb-4">
              <div>
                <h3 className="text-xl font-bold text-white mb-1">Your Progress</h3>
                <p className="text-sm text-slate-400">
                  {completedWeeks} of {totalWeeks} weeks completed
                </p>
              </div>
              <div className="text-right">
                <div className="text-4xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-purple-600">
                  {totalWeeks > 0 ? Math.round((completedWeeks / totalWeeks) * 100) : 0}%
                </div>
                <div className="text-xs text-slate-500 mt-1">Complete</div>
              </div>
            </div>
            <ProgressBar completed={completedWeeks} total={totalWeeks} />
          </div>

          {/* Adapt My Path Section */}
          <div className="bg-gradient-to-br from-slate-900/80 to-slate-900/50 backdrop-blur-sm rounded-2xl border border-slate-800 overflow-hidden shadow-xl">
            <button
              onClick={() => setShowAdaptSection(!showAdaptSection)}
              className="w-full p-6 md:p-8 flex items-center justify-between hover:bg-slate-800/30 transition-all group"
            >
              <div className="flex items-center space-x-4">
                <div className="w-12 h-12 bg-gradient-to-br from-purple-500 to-pink-600 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform shadow-lg shadow-purple-500/30">
                  <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                  </svg>
                </div>
                <div className="text-left">
                  <h3 className="text-xl font-bold text-white mb-1">Adapt My Path</h3>
                  <p className="text-sm text-slate-400">Customize your learning journey based on your needs</p>
                </div>
              </div>
              <div className="flex items-center space-x-3">
                {showAdaptSection && (
                  <span className="hidden md:inline-block px-3 py-1 bg-purple-500/10 text-purple-400 text-xs font-medium rounded-full border border-purple-500/20">
                    Expanded
                  </span>
                )}
                <svg
                  className={`w-6 h-6 text-slate-400 transition-transform ${
                    showAdaptSection ? 'rotate-180' : ''
                  }`}
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
                </svg>
              </div>
            </button>

            {showAdaptSection && (
              <div className="border-t border-slate-800 p-6 md:p-8 space-y-6">
                <div>
                  <label className="block text-sm font-semibold text-slate-200 mb-3">
                    How would you like to adjust your pathway?
                  </label>
                  <textarea
                    value={feedback}
                    onChange={(e) => setFeedback(e.target.value)}
                    placeholder="Examples:&#10;• I only have 1 hour per day now&#10;• I want more project-based learning&#10;• I'm struggling with JavaScript&#10;• I need more beginner-friendly resources"
                    className="w-full px-4 py-3.5 bg-slate-800/50 border border-slate-700 rounded-xl text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-transparent resize-none transition-all"
                    rows="5"
                  />
                  <p className="mt-2 text-xs text-slate-500">Be specific about what you'd like to change</p>
                </div>

                {adaptError && (
                  <div className="p-4 bg-red-500/10 border border-red-500/30 rounded-xl flex items-start space-x-3">
                    <svg className="w-5 h-5 text-red-400 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                      <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                    </svg>
                    <p className="text-red-400 text-sm">{adaptError}</p>
                  </div>
                )}

                <div className="flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
                  <button
                    onClick={handleAdaptPathway}
                    disabled={isAdapting}
                    className="flex-1 sm:flex-none px-6 py-3.5 bg-gradient-to-r from-purple-500 to-pink-600 text-white font-bold rounded-xl hover:from-purple-600 hover:to-pink-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed shadow-lg hover:shadow-xl hover:shadow-purple-500/30 flex items-center justify-center"
                  >
                    {isAdapting ? (
                      <>
                        <svg className="animate-spin -ml-1 mr-2 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                          <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                          <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                        </svg>
                        Adapting...
                      </>
                    ) : (
                      <>
                        <svg className="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
                        </svg>
                        Adapt Pathway
                      </>
                    )}
                  </button>
                  <button
                    onClick={() => {
                      setShowAdaptSection(false);
                      setFeedback('');
                      setAdaptError(null);
                    }}
                    className="px-6 py-3.5 bg-slate-800/80 backdrop-blur-sm text-slate-300 rounded-xl hover:bg-slate-700 transition-all border border-slate-700"
                  >
                    Cancel
                  </button>
                </div>

                {pathway.adaptationHistory && pathway.adaptationHistory.length > 0 && (
                  <div className="pt-6 border-t border-slate-800">
                    <h4 className="text-sm font-bold text-slate-200 mb-4 flex items-center">
                      <svg className="w-4 h-4 mr-2 text-purple-400" fill="currentColor" viewBox="0 0 20 20">
                        <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z" clipRule="evenodd" />
                      </svg>
                      Adaptation History
                    </h4>
                    <div className="space-y-3">
                      {pathway.adaptationHistory.map((note, index) => (
                        <div key={index} className="flex items-start space-x-3 p-3 bg-slate-800/30 rounded-lg">
                          <svg className="w-5 h-5 text-purple-400 mt-0.5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                            <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                          </svg>
                          <span className="text-sm text-slate-300 leading-relaxed">{note}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            )}
          </div>
        </div>

        {/* Weekly Plans */}
        <div className="mb-12">
          <h2 className="text-2xl font-bold text-white mb-6">Weekly Learning Plan</h2>
          <div className="space-y-4">
            {pathway.weeks.map((week) => (
              <WeekCard
                key={week.weekNumber}
                week={week}
                onToggleComplete={handleToggleWeekComplete}
              />
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

        {/* Federal Job Opportunities */}
        <div className="mb-12">
          <h2 className="text-2xl font-bold text-white mb-6">Federal Job Opportunities</h2>
          
          {/* Search Box */}
          <div className="bg-slate-900/50 backdrop-blur-sm rounded-xl border border-slate-800 p-6 mb-6">
            <div className="flex flex-col md:flex-row gap-4">
              <div className="flex-1">
                <label htmlFor="jobLocation" className="block text-sm font-medium text-slate-300 mb-2">
                  Location (optional)
                </label>
                <input
                  type="text"
                  id="jobLocation"
                  value={jobLocation}
                  onChange={(e) => setJobLocation(e.target.value)}
                  placeholder="e.g., Orlando, Florida, or leave empty for nationwide"
                  className="w-full px-4 py-3 bg-slate-800/50 border border-slate-700 rounded-lg text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                />
              </div>
              <div className="flex items-end">
                <button
                  onClick={handleSearchJobs}
                  disabled={jobsLoading}
                  className="px-6 py-3 bg-gradient-to-r from-blue-500 to-purple-600 text-white font-semibold rounded-lg hover:from-blue-600 hover:to-purple-700 transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center space-x-2 shadow-lg hover:shadow-xl hover:shadow-blue-500/30"
                >
                  {jobsLoading ? (
                    <>
                      <svg className="animate-spin h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                        <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                      </svg>
                      <span>Searching...</span>
                    </>
                  ) : (
                    <>
                      <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                      </svg>
                      <span>Search Jobs</span>
                    </>
                  )}
                </button>
              </div>
            </div>
            
            {/* Search Info */}
            {jobsData && (
              <div className="mt-4 flex items-center space-x-2 text-sm text-slate-400">
                <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clipRule="evenodd" />
                </svg>
                <span>
                  Searching for: <strong className="text-white">{jobsData.keyword}</strong>
                  {jobsData.originalLocation && (
                    <> in <strong className="text-white">{jobsData.originalLocation}</strong></>
                  )}
                </span>
              </div>
            )}
          </div>

          {/* Fallback Message */}
          {jobsData?.fallbackMessage && (
            <div className="bg-blue-500/10 border border-blue-500/30 rounded-xl p-4 mb-6 flex items-start space-x-3">
              <svg className="w-5 h-5 text-blue-400 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clipRule="evenodd" />
              </svg>
              <p className="text-blue-300">{jobsData.fallbackMessage}</p>
            </div>
          )}

          {/* Error Message */}
          {jobsError && (
            <div className="bg-red-500/10 border border-red-500/30 rounded-xl p-4 mb-6 flex items-start space-x-3">
              <svg className="w-5 h-5 text-red-400 flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
              </svg>
              <p className="text-red-400">{jobsError}</p>
            </div>
          )}

          {/* Jobs List */}
          {jobsData && jobsData.count > 0 ? (
            <div className="space-y-4">
              <div className="flex items-center justify-between mb-4">
                <p className="text-slate-400">
                  Found <strong className="text-white">{jobsData.count}</strong> job{jobsData.count !== 1 ? 's' : ''}
                </p>
                <span className="px-3 py-1 bg-slate-800 text-slate-300 text-xs font-medium rounded-full border border-slate-700">
                  {jobsData.searchLevel === 'city' ? '📍 City' : jobsData.searchLevel === 'state' ? '🗺️ State' : '🌎 Nationwide'}
                </span>
              </div>
              {jobsData.jobs.map((job, index) => (
                <JobCard key={index} job={job} />
              ))}
            </div>
          ) : jobsData && jobsData.count === 0 ? (
            <div className="bg-slate-900/50 backdrop-blur-sm rounded-xl border border-slate-800 p-8 text-center">
              <div className="w-16 h-16 bg-slate-800 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg className="w-8 h-8 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
              </div>
              <h3 className="text-xl font-bold text-white mb-2">No Jobs Found</h3>
              <p className="text-slate-400">
                Try adjusting your search location or check back later for new postings.
              </p>
            </div>
          ) : !jobsLoading && !jobsData && (
            <div className="bg-slate-900/50 backdrop-blur-sm rounded-xl border border-slate-800 p-8 text-center">
              <div className="w-16 h-16 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center mx-auto mb-4">
                <svg className="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                </svg>
              </div>
              <h3 className="text-xl font-bold text-white mb-2">Discover Federal Opportunities</h3>
              <p className="text-slate-400">
                Click "Search Jobs" to find federal positions related to your career goal.
              </p>
            </div>
          )}
        </div>

        {/* Recommended Certifications */}
        {pathway.recommendedCertifications && pathway.recommendedCertifications.length > 0 && (
          <div className="mb-12">
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
