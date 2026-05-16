/**
 * Progress bar component - Shows pathway completion progress
 */
function ProgressBar({ completed, total }) {
  const percentage = total > 0 ? Math.round((completed / total) * 100) : 0;

  return (
    <div className="w-full">
      <div className="relative w-full bg-slate-800/50 rounded-full h-4 overflow-hidden border border-slate-700">
        {/* Background pattern */}
        <div className="absolute inset-0 opacity-10">
          <div className="h-full w-full" style={{
            backgroundImage: 'repeating-linear-gradient(90deg, transparent, transparent 10px, rgba(255,255,255,0.1) 10px, rgba(255,255,255,0.1) 20px)'
          }}></div>
        </div>
        
        {/* Progress fill */}
        <div
          className="relative h-full bg-gradient-to-r from-blue-500 via-purple-500 to-purple-600 rounded-full transition-all duration-700 ease-out shadow-lg"
          style={{
            width: `${percentage}%`,
            boxShadow: percentage > 0 ? '0 0 20px rgba(139, 92, 246, 0.5)' : 'none'
          }}
        >
          {/* Shine effect */}
          {percentage > 0 && (
            <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white to-transparent opacity-20 animate-pulse"></div>
          )}
        </div>
      </div>
      
      {/* Progress text */}
      <div className="flex items-center justify-between mt-3 text-xs">
        <span className="text-slate-400 font-medium">
          {completed} of {total} weeks
        </span>
        {percentage === 100 && (
          <span className="flex items-center text-green-400 font-bold">
            <svg className="w-4 h-4 mr-1" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
            </svg>
            Complete!
          </span>
        )}
      </div>
    </div>
  );
}

export default ProgressBar;

// Made with Bob
