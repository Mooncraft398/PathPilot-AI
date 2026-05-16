/**
 * Resource card component - Displays a learning resource
 */
function ResourceCard({ resource }) {
  console.log('📚 ResourceCard rendering:', resource);
  
  const getTypeIcon = (type) => {
    switch (type) {
      case 'video':
        return (
          <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path d="M2 6a2 2 0 012-2h6a2 2 0 012 2v8a2 2 0 01-2 2H4a2 2 0 01-2-2V6zM14.553 7.106A1 1 0 0014 8v4a1 1 0 00.553.894l2 1A1 1 0 0018 13V7a1 1 0 00-1.447-.894l-2 1z" />
          </svg>
        );
      case 'article':
      case 'reading':
        return (
          <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path d="M9 4.804A7.968 7.968 0 005.5 4c-1.255 0-2.443.29-3.5.804v10A7.969 7.969 0 015.5 14c1.669 0 3.218.51 4.5 1.385A7.962 7.962 0 0114.5 14c1.255 0 2.443.29 3.5.804v-10A7.968 7.968 0 0014.5 4c-1.255 0-2.443.29-3.5.804V12a1 1 0 11-2 0V4.804z" />
          </svg>
        );
      case 'course':
        return (
          <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path d="M10.394 2.08a1 1 0 00-.788 0l-7 3a1 1 0 000 1.84L5.25 8.051a.999.999 0 01.356-.257l4-1.714a1 1 0 11.788 1.838L7.667 9.088l1.94.831a1 1 0 00.787 0l7-3a1 1 0 000-1.838l-7-3zM3.31 9.397L5 10.12v4.102a8.969 8.969 0 00-1.05-.174 1 1 0 01-.89-.89 11.115 11.115 0 01.25-3.762zM9.3 16.573A9.026 9.026 0 007 14.935v-3.957l1.818.78a3 3 0 002.364 0l5.508-2.361a11.026 11.026 0 01.25 3.762 1 1 0 01-.89.89 8.968 8.968 0 00-5.35 2.524 1 1 0 01-1.4 0zM6 18a1 1 0 001-1v-2.065a8.935 8.935 0 00-2-.712V17a1 1 0 001 1z" />
          </svg>
        );
      case 'documentation':
        return (
          <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path fillRule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" clipRule="evenodd" />
          </svg>
        );
      case 'interactive':
        return (
          <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path fillRule="evenodd" d="M3 5a2 2 0 012-2h10a2 2 0 012 2v8a2 2 0 01-2 2h-2.22l.123.489.804.804A1 1 0 0113 18H7a1 1 0 01-.707-1.707l.804-.804L7.22 15H5a2 2 0 01-2-2V5zm5.771 7H5V5h10v7H8.771z" clipRule="evenodd" />
          </svg>
        );
      default:
        return (
          <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clipRule="evenodd" />
          </svg>
        );
    }
  };

  const getTypeColor = (type) => {
    switch (type) {
      case 'video':
        return 'text-red-400 bg-red-500/10';
      case 'article':
      case 'reading':
        return 'text-blue-400 bg-blue-500/10';
      case 'course':
        return 'text-purple-400 bg-purple-500/10';
      case 'documentation':
        return 'text-green-400 bg-green-500/10';
      case 'interactive':
        return 'text-yellow-400 bg-yellow-500/10';
      default:
        return 'text-slate-400 bg-slate-500/10';
    }
  };

  // Check if URL is valid
  const hasValidUrl = resource.url && resource.url !== '#' && resource.url !== '';
  
  // Get verification status
  const isVerified = resource.urlVerified === true;
  const source = resource.source || 'unknown';
  const isReplacement = source === 'local_verified_replacement';
  const isWatsonxVerified = source === 'watsonx_verified';
  const isWatsonxUnverified = source === 'watsonx_unverified';
  
  const cardContent = (
    <>
      <div className="flex items-start justify-between mb-3">
        <div className={`p-2.5 rounded-xl ${getTypeColor(resource.type)} group-hover:scale-110 transition-transform`}>
          {getTypeIcon(resource.type)}
        </div>
        <div className="flex items-center space-x-2">
          {resource.isFree && (
            <span className="px-2.5 py-1 bg-green-500/10 text-green-400 text-xs font-bold rounded-full border border-green-500/30 flex items-center">
              <svg className="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
              </svg>
              Free
            </span>
          )}
          {isVerified && isWatsonxVerified && (
            <span className="px-2.5 py-1 bg-blue-500/10 text-blue-400 text-xs font-bold rounded-full border border-blue-500/30 flex items-center" title="AI-generated URL verified">
              <svg className="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M6.267 3.455a3.066 3.066 0 001.745-.723 3.066 3.066 0 013.976 0 3.066 3.066 0 001.745.723 3.066 3.066 0 012.812 2.812c.051.643.304 1.254.723 1.745a3.066 3.066 0 010 3.976 3.066 3.066 0 00-.723 1.745 3.066 3.066 0 01-2.812 2.812 3.066 3.066 0 00-1.745.723 3.066 3.066 0 01-3.976 0 3.066 3.066 0 00-1.745-.723 3.066 3.066 0 01-2.812-2.812 3.066 3.066 0 00-.723-1.745 3.066 3.066 0 010-3.976 3.066 3.066 0 00.723-1.745 3.066 3.066 0 012.812-2.812zm7.44 5.252a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
              </svg>
              Verified
            </span>
          )}
          {isReplacement && (
            <span className="px-2.5 py-1 bg-amber-500/10 text-amber-400 text-xs font-bold rounded-full border border-amber-500/30 flex items-center" title="Curated verified resource">
              <svg className="w-3 h-3 mr-1" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
              </svg>
              Curated
            </span>
          )}
          {isWatsonxUnverified && (
            <span className="px-2.5 py-1 bg-slate-700/50 text-slate-400 text-xs font-medium rounded-full border border-slate-600" title="URL not verified">
              <svg className="w-3 h-3 mr-1 inline" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
              </svg>
              Unverified
            </span>
          )}
          {!hasValidUrl && (
            <span className="px-2.5 py-1 bg-slate-700/50 text-slate-400 text-xs font-medium rounded-full border border-slate-600">
              No link
            </span>
          )}
        </div>
      </div>
      <h5 className="font-bold text-white mb-2 group-hover:text-blue-400 transition-colors leading-snug">{resource.title}</h5>
      <div className="flex items-center justify-between text-sm">
        <span className="text-slate-400 capitalize font-medium">{resource.type}</span>
        <span className="text-slate-500 flex items-center">
          <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          {resource.duration}
        </span>
      </div>
    </>
  );
  
  // If no valid URL, render as div instead of link
  if (!hasValidUrl) {
    return (
      <div className="block bg-slate-800/50 backdrop-blur-sm rounded-xl p-5 border border-slate-700 opacity-75">
        {cardContent}
      </div>
    );
  }
  
  // Render as clickable link
  return (
    <a
      href={resource.url}
      target="_blank"
      rel="noopener noreferrer"
      className="group block bg-slate-800/50 backdrop-blur-sm rounded-xl p-5 hover:bg-slate-800 transition-all border border-slate-700 hover:border-slate-600 hover:shadow-lg hover:-translate-y-0.5"
    >
      {cardContent}
    </a>
  );
}

export default ResourceCard;

// Made with Bob
