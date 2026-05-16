/**
 * Project card component - Displays a guided project
 */
function ProjectCard({ project }) {
  // Debug logging
  console.log('🎯 ProjectCard rendering with project:', project);
  console.log('   Title:', project?.title);
  console.log('   Description:', project?.description);
  console.log('   Skills:', project?.skills);
  console.log('   Skills type:', typeof project?.skills);
  console.log('   Skills is array:', Array.isArray(project?.skills));
  console.log('   Skills length:', project?.skills?.length);
  console.log('   Difficulty:', project?.difficulty);
  console.log('   Estimated hours:', project?.estimatedHours);
  console.log('   URL:', project?.url || project?.link || project?.githubUrl || 'none');
  
  const getDifficultyColor = (difficulty) => {
    switch (difficulty) {
      case 'beginner':
        return 'bg-green-500/10 text-green-400 border-green-500/30';
      case 'intermediate':
        return 'bg-yellow-500/10 text-yellow-400 border-yellow-500/30';
      case 'advanced':
        return 'bg-red-500/10 text-red-400 border-red-500/30';
      default:
        return 'bg-blue-500/10 text-blue-400 border-blue-500/30';
    }
  };
  
  // Ensure skills is always an array
  const skills = Array.isArray(project?.skills) ? project.skills : [];
  const hasSkills = skills.length > 0;
  
  // Check for project URL
  const projectUrl = project?.url || project?.link || project?.githubUrl || project?.sourceUrl;
  const hasUrl = projectUrl && projectUrl !== '#' && projectUrl !== '';
  
  console.log('   Processed skills:', skills);
  console.log('   Has skills:', hasSkills);
  console.log('   Has URL:', hasUrl);

  return (
    <div className="bg-gradient-to-br from-slate-800/80 to-slate-900/80 backdrop-blur-sm rounded-xl p-6 border border-slate-700 hover:border-orange-500/50 transition-all hover:shadow-xl hover:shadow-orange-500/10">
      <div className="flex items-start justify-between gap-4 mb-4">
        <div className="flex-1">
          <div className="flex items-center space-x-3 mb-3">
            <div className="w-10 h-10 bg-gradient-to-br from-orange-500 to-orange-600 rounded-lg flex items-center justify-center shadow-lg shadow-orange-500/20">
              <svg className="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M12.316 3.051a1 1 0 01.633 1.265l-4 12a1 1 0 11-1.898-.632l4-12a1 1 0 011.265-.633zM5.707 6.293a1 1 0 010 1.414L3.414 10l2.293 2.293a1 1 0 11-1.414 1.414l-3-3a1 1 0 010-1.414l3-3a1 1 0 011.414 0zm8.586 0a1 1 0 011.414 0l3 3a1 1 0 010 1.414l-3 3a1 1 0 11-1.414-1.414L16.586 10l-2.293-2.293a1 1 0 010-1.414z" clipRule="evenodd" />
              </svg>
            </div>
            <h5 className="text-xl font-bold text-white">{project.title}</h5>
          </div>
          <p className="text-slate-300 text-sm leading-relaxed mb-4">{project.description}</p>
        </div>
        <span className={`px-3 py-1.5 rounded-full text-xs font-bold border flex-shrink-0 ${getDifficultyColor(project.difficulty)}`}>
          {project.difficulty}
        </span>
      </div>

      {/* Skills */}
      <div className="mb-4 pb-4 border-b border-slate-700">
        <p className="text-xs font-semibold text-slate-400 mb-3 uppercase tracking-wide">Skills you'll practice</p>
        {hasSkills ? (
          <div className="flex flex-wrap gap-2">
            {skills.map((skill, index) => (
              <span
                key={index}
                className="px-3 py-1.5 bg-blue-500/10 text-blue-400 text-xs font-bold rounded-lg border border-blue-500/30 hover:bg-blue-500/20 transition-colors"
              >
                {skill}
              </span>
            ))}
          </div>
        ) : (
          <div className="text-slate-500 text-sm italic">
            No specific skills listed for this project
          </div>
        )}
      </div>

      {/* Time Estimate and Link */}
      <div className="flex items-center justify-between">
        <div className="flex items-center text-sm text-slate-400">
          <div className="w-8 h-8 bg-slate-700/50 rounded-lg flex items-center justify-center mr-2">
            <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
          <span className="font-medium">{project.estimatedHours} hours</span>
        </div>
        <div className="flex items-center space-x-2">
          {hasUrl ? (
            <a
              href={projectUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="px-3 py-1.5 bg-orange-500/10 text-orange-400 text-xs font-bold rounded-lg border border-orange-500/20 hover:bg-orange-500/20 transition-colors flex items-center space-x-1"
            >
              <svg className="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
              </svg>
              <span>View Project</span>
            </a>
          ) : (
            <div className="px-3 py-1.5 bg-orange-500/10 text-orange-400 text-xs font-bold rounded-lg border border-orange-500/20">
              Portfolio Project
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default ProjectCard;

// Made with Bob
