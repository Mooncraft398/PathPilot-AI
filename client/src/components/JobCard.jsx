/**
 * JobCard Component
 * Displays a single job posting in a readable card format
 */
function JobCard({ job }) {
  const formatSalary = (min, max) => {
    if (!min && !max) return 'Not specified';
    
    const formatNumber = (num) => {
      if (!num) return null;
      return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0,
      }).format(num);
    };
    
    const minFormatted = formatNumber(min);
    const maxFormatted = formatNumber(max);
    
    if (minFormatted && maxFormatted) {
      return `${minFormatted} - ${maxFormatted}`;
    }
    return minFormatted || maxFormatted || 'Not specified';
  };

  return (
    <div className="bg-slate-900/50 backdrop-blur-sm rounded-xl border border-slate-800 hover:border-blue-500/50 transition-all p-6 group">
      {/* Job Title */}
      <h3 className="text-xl font-bold text-white mb-2 group-hover:text-blue-400 transition-colors">
        {job.title}
      </h3>
      
      {/* Organization */}
      <div className="flex items-center space-x-2 mb-3">
        <svg className="w-4 h-4 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
        </svg>
        <span className="text-slate-300 font-medium">{job.organization}</span>
      </div>
      
      {/* Location and Salary */}
      <div className="flex flex-wrap items-center gap-4 mb-4">
        <div className="flex items-center space-x-2">
          <svg className="w-4 h-4 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
          </svg>
          <span className="text-slate-400 text-sm">{job.location}</span>
        </div>
        
        <div className="flex items-center space-x-2">
          <svg className="w-4 h-4 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <span className="text-slate-400 text-sm">{formatSalary(job.minimumSalary, job.maximumSalary)}</span>
        </div>
      </div>
      
      {/* Summary */}
      {job.summary && (
        <p className="text-slate-400 text-sm mb-4 line-clamp-3 leading-relaxed">
          {job.summary}
        </p>
      )}
      
      {/* View Job Button */}
      <a
        href={job.url}
        target="_blank"
        rel="noopener noreferrer"
        className="inline-flex items-center px-4 py-2 bg-gradient-to-r from-blue-500 to-purple-600 text-white text-sm font-semibold rounded-lg hover:from-blue-600 hover:to-purple-700 transition-all shadow-lg hover:shadow-xl hover:shadow-blue-500/30"
      >
        View Job Details
        <svg className="w-4 h-4 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
        </svg>
      </a>
    </div>
  );
}

export default JobCard;

// Made with Bob