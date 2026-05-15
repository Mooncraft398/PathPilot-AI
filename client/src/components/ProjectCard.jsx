/**
 * Project card component - Displays a guided project
 */
function ProjectCard({ project }) {
  return (
    <div className="bg-gradient-to-br from-slate-800 to-slate-900 rounded-lg p-6 border border-slate-700">
      <div className="flex items-start justify-between mb-4">
        <div className="flex-1">
          <h5 className="text-lg font-semibold text-white mb-2">{project.title}</h5>
          <p className="text-slate-300 text-sm mb-4">{project.description}</p>
        </div>
        <span className={`px-3 py-1 rounded-full text-xs font-medium ${
          project.difficulty === 'beginner' 
            ? 'bg-green-500/10 text-green-500 border border-green-500/20'
            : project.difficulty === 'intermediate'
            ? 'bg-yellow-500/10 text-yellow-500 border border-yellow-500/20'
            : 'bg-red-500/10 text-red-500 border border-red-500/20'
        }`}>
          {project.difficulty}
        </span>
      </div>

      {/* Skills */}
      <div className="mb-4">
        <p className="text-sm text-slate-400 mb-2">Skills you'll practice:</p>
        <div className="flex flex-wrap gap-2">
          {project.skills.map((skill, index) => (
            <span
              key={index}
              className="px-3 py-1 bg-blue-500/10 text-blue-400 text-xs font-medium rounded-full border border-blue-500/20"
            >
              {skill}
            </span>
          ))}
        </div>
      </div>

      {/* Time Estimate */}
      <div className="flex items-center text-sm text-slate-400">
        <svg className="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <span>Estimated time: {project.estimatedHours} hours</span>
      </div>
    </div>
  );
}

export default ProjectCard;

// Made with Bob
