import axios from 'axios';

/**
 * API utility functions for PathPilot AI
 * Handles communication with the FastAPI backend
 */

// Base URL for the API
const API_BASE_URL = 'http://localhost:8000';

/**
 * Create an axios instance with default config
 */
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 30000, // 30 seconds timeout
});

/**
 * Check if the API is healthy
 * @returns {Promise<Object>} Health status
 */
export const checkHealth = async () => {
  try {
    const response = await api.get('/');
    return response.data;
  } catch (error) {
    console.error('Health check failed:', error);
    throw error;
  }
};

/**
 * Generate a career pathway
 * @param {Object} formData - The form data from the user
 * @param {string} formData.goal - Career goal
 * @param {string} formData.level - Skill level (beginner, intermediate, advanced)
 * @param {number} formData.weeks - Number of weeks
 * @param {number} formData.daysPerWeek - Days per week
 * @param {number} formData.hoursPerDay - Hours per day
 * @param {Array<string>} formData.preferences - Learning preferences
 * @param {string} formData.budget - Budget preference
 * @returns {Promise<Object>} Generated pathway
 */
export const generatePathway = async (formData) => {
  try {
    const response = await api.post('/api/pathways/generate', formData);
    return response.data;
  } catch (error) {
    console.error('Failed to generate pathway:', error);
    
    // Provide more detailed error message
    if (error.response) {
      // Server responded with error
      throw new Error(error.response.data.detail || 'Failed to generate pathway', { cause: error });
    } else if (error.request) {
      // Request made but no response
      throw new Error('Cannot connect to server. Make sure the backend is running at http://localhost:8000', { cause: error });
    } else {
      // Something else happened
      throw new Error('An unexpected error occurred', { cause: error });
    }
  }
};

/**
 * Adapt an existing pathway based on user feedback
 * @param {Object} pathway - The current pathway object
 * @param {string} feedback - User feedback for adaptation
 * @returns {Promise<Object>} Adapted pathway
 */
export const adaptPathway = async (pathway, feedback) => {
  try {
    console.log('📡 Sending adapt request to API...');
    console.log('Request payload:', { pathway, feedback });
    
    const response = await api.post('/api/pathways/adapt', {
      pathway,
      feedback,
    });
    
    console.log('📡 API Response received:', response.data);
    return response.data;
  } catch (error) {
    console.error('❌ API Error:', error);
    console.error('Error response:', error.response?.data);
    
    // Provide more detailed error message
    if (error.response) {
      throw new Error(error.response.data.detail || 'Failed to adapt pathway', { cause: error });
    } else if (error.request) {
      throw new Error('Cannot connect to server. Make sure the backend is running at http://localhost:8000', { cause: error });
    } else {
      throw new Error('An unexpected error occurred', { cause: error });
    }
  }
};

/**
 * Generate an AI-powered career roadmap using IBM watsonx.ai
 * @param {Object} requestData - The roadmap request data
 * @param {string} requestData.careerGoal - Target career role (e.g., "SOC Analyst")
 * @param {Array<string>} requestData.currentSkills - List of current skills
 * @param {string} requestData.timeframe - Available timeframe (e.g., "3 months")
 * @returns {Promise<Object>} AI-generated roadmap with metadata
 */
export const generateRoadmap = async (requestData) => {
  try {
    console.log('🤖 Generating AI roadmap with watsonx.ai...');
    console.log('Request data:', requestData);
    
    const response = await api.post('/api/generate-roadmap', requestData, {
      timeout: 90000, // 90 seconds for AI generation
    });
    
    console.log('✅ Roadmap generated successfully');
    console.log('📦 Raw response from backend:', response.data);
    return response.data;
  } catch (error) {
    console.error('❌ Failed to generate roadmap:', error);
    
    if (error.response) {
      throw new Error(error.response.data.detail || 'Failed to generate roadmap', { cause: error });
    } else if (error.request) {
      throw new Error('Cannot connect to server. Make sure the backend is running at http://localhost:8000', { cause: error });
    } else {
      throw new Error('An unexpected error occurred', { cause: error });
    }
  }
};

/**
 * Transform Watsonx.ai roadmap response to match frontend PathwayResponse format
 * @param {Object} roadmapResponse - Response from /api/generate-roadmap
 * @param {Object} formData - Original form data from user
 * @returns {Object} Transformed pathway object for frontend
 */
export const transformRoadmapToPathway = (roadmapResponse, formData) => {
  console.log('=' * 80);
  console.log('🔄 TRANSFORMING ROADMAP TO PATHWAY FORMAT');
  console.log('=' * 80);
  console.log('📦 Raw backend response:', JSON.stringify(roadmapResponse, null, 2));
  console.log('📋 Form data:', formData);
  
  const roadmap = roadmapResponse.roadmap || {};
  const metadata = roadmapResponse.metadata || {};
  
  // Log whether WatsonX was used
  console.log('\n' + '=' * 80);
  if (metadata.usedWatsonx === true) {
    console.log('✅ USING WATSONX.AI GENERATED ROADMAP');
    console.log(`   Model: ${metadata.model || 'unknown'}`);
    console.log(`   Tokens: ${metadata.tokens || 0}`);
    console.log(`   GitHub Projects: ${metadata.usedGitHub ? 'Yes' : 'No'}`);
    console.log(`   Local Resources: ${metadata.matchedLocalResources || 0}`);
  } else {
    console.warn('⚠️  USING FALLBACK TEMPLATE DATA (WatsonX unavailable)');
    console.warn(`   Reason: ${metadata.fallbackReason || 'unknown'}`);
  }
  console.log('=' * 80 + '\n');
  
  // Log roadmap structure
  console.log('📊 Roadmap structure:');
  console.log(`   Phases: ${roadmap.phases?.length || 0}`);
  console.log(`   Weekly Plans: ${roadmap.weeklyPlan?.length || 0}`);
  console.log(`   Skills: ${roadmap.skills?.length || 0}`);
  console.log(`   Resources: ${roadmap.resources?.length || 0}`);
  console.log(`   GitHub Projects: ${roadmap.githubProjects?.length || 0}`);
  console.log(`   Portfolio Projects: ${roadmap.portfolioProjects?.length || 0}`);
  
  // Transform phases into weeks
  const weeks = [];
  const phases = roadmap.phases || [];
  const weeklyPlan = roadmap.weeklyPlan || [];
  
  // Use the actual number of weeks from weeklyPlan if available, otherwise calculate
  let totalWeeks = weeklyPlan.length > 0 ? weeklyPlan.length : (formData.weeks || 12);
  
  console.log(`\n📅 Creating ${totalWeeks} weeks from ${weeklyPlan.length} weekly plans`);
  
  // Create weeks from weekly plan (use actual AI-generated weekly data)
  for (let i = 0; i < totalWeeks; i++) {
    const weekNum = i + 1;
    const phaseIndex = Math.floor(i / Math.ceil(totalWeeks / Math.max(phases.length, 1)));
    const phase = phases[phaseIndex] || phases[0] || {};
    const weekPlan = weeklyPlan[i] || weeklyPlan[weeklyPlan.length - 1] || {};
    
    console.log(`\n📆 Week ${weekNum}:`, {
      focus: weekPlan.focus,
      topics: weekPlan.topics,
      dailyTasks: weekPlan.dailyTasks,
      phase: phase.title
    });
    
    // Generate daily plan using AI-provided data
    const dailyPlan = [];
    const daysPerWeek = formData.daysPerWeek || 5;
    const hoursPerDay = formData.hoursPerDay || 2;
    
    // Use AI-generated daily tasks and topics
    const aiDailyTasks = weekPlan.dailyTasks || [];
    const aiTopics = weekPlan.topics || [];
    const weekFocus = weekPlan.focus || phase.focus || phase.title || `Week ${weekNum} Learning`;
    
    console.log(`   Daily tasks (${aiDailyTasks.length}):`, aiDailyTasks);
    console.log(`   Topics (${aiTopics.length}):`, aiTopics);
    
    // Create daily plan cards - one card per day showing the week's focus
    for (let day = 1; day <= daysPerWeek; day++) {
      const dayTasks = [];
      
      // Use AI-generated tasks, distributed across days
      if (aiDailyTasks.length > 0) {
        // Distribute tasks across days
        const tasksPerDay = Math.ceil(aiDailyTasks.length / daysPerWeek);
        const startIdx = (day - 1) * tasksPerDay;
        const endIdx = Math.min(startIdx + tasksPerDay, aiDailyTasks.length);
        
        for (let t = startIdx; t < endIdx; t++) {
          if (aiDailyTasks[t]) {
            dayTasks.push(aiDailyTasks[t]);
          }
        }
      }
      
      // Add topics as tasks if we don't have enough tasks
      if (dayTasks.length === 0 && aiTopics.length > 0) {
        const topicIdx = (day - 1) % aiTopics.length;
        if (aiTopics[topicIdx]) {
          dayTasks.push(`Study: ${aiTopics[topicIdx]}`);
        }
      }
      
      // Add practice task
      if (aiTopics.length > 0) {
        const practiceTopicIdx = day % aiTopics.length;
        if (aiTopics[practiceTopicIdx]) {
          dayTasks.push(`Practice: ${aiTopics[practiceTopicIdx]}`);
        }
      }
      
      // Ensure at least one task
      if (dayTasks.length === 0) {
        dayTasks.push(`Work on ${weekFocus}`);
      }
      
      dailyPlan.push({
        day,
        focus: `${weekFocus} - Day ${day}`,
        tasks: dayTasks,
        estimatedHours: hoursPerDay
      });
    }
    
    // Use week-specific resources if provided by AI, or distribute all resources across weeks
    const allResources = roadmap.resources || [];
    const resourcesPerWeek = Math.ceil(allResources.length / totalWeeks) || 2;
    const startIdx = i * resourcesPerWeek;
    const endIdx = Math.min(startIdx + resourcesPerWeek, allResources.length);
    const resourcesForWeek = allResources.slice(startIdx, endIdx);
    
    console.log(`\n📚 Week ${weekNum} resources (${resourcesForWeek.length}):`, resourcesForWeek);
    
    // Map resources with proper field handling and URL validation
    const mappedResources = resourcesForWeek.map((r, idx) => {
      // Extract provider from URL if not provided
      let provider = r.provider || '';
      const url = r.url || r.link || r.href || '#';
      
      if (!provider && url !== '#') {
        try {
          const urlObj = new URL(url);
          const hostname = urlObj.hostname.replace('www.', '');
          provider = hostname.split('.')[0];
          // Capitalize first letter
          provider = provider.charAt(0).toUpperCase() + provider.slice(1);
        } catch {
          provider = 'External';
        }
      }
      
      const resource = {
        title: r.title || r.name || `${provider} ${r.type || 'Resource'}`,
        type: r.type || 'course',
        url: url,
        provider: provider,
        duration: r.duration || r.estimatedTime || '1-2 hours',
        isFree: r.isFree !== undefined ? r.isFree : (r.cost === 'free' || r.cost === 'Free' || !r.cost)
      };
      
      console.log(`   Resource ${idx + 1}:`, resource);
      return resource;
    });
    
    // Get project for this week - use phase-based or week-specific
    const projectForWeek = roadmap.portfolioProjects?.[phaseIndex] || roadmap.portfolioProjects?.[i] || {};
    
    // Ensure skills is always an array
    let projectSkills = projectForWeek.skills || aiTopics || phase.skills || roadmap.skills?.slice(0, 3) || [];
    
    // Convert to array if it's not already
    if (!Array.isArray(projectSkills)) {
      projectSkills = [projectSkills];
    }
    
    // Filter out empty/undefined values
    projectSkills = projectSkills.filter(skill => skill && typeof skill === 'string' && skill.trim() !== '');
    
    // If still empty, provide default
    if (projectSkills.length === 0) {
      projectSkills = ['Problem Solving', 'Critical Thinking', 'Project Management'];
    }
    
    // Get project URL
    const projectUrl = projectForWeek.url || projectForWeek.link || projectForWeek.githubUrl || projectForWeek.sourceUrl || '';
    
    console.log(`\n🎯 Week ${weekNum} project BEFORE mapping:`, {
      projectForWeek,
      title: projectForWeek.title,
      description: projectForWeek.description,
      skills: projectForWeek.skills,
      url: projectUrl
    });
    
    console.log(`\n🎯 Week ${weekNum} project AFTER processing:`, {
      title: projectForWeek.title || `Week ${weekNum}: ${weekPlan.focus || 'Practical Project'}`,
      skills: projectSkills,
      skillsType: typeof projectSkills,
      skillsIsArray: Array.isArray(projectSkills),
      skillsLength: projectSkills.length,
      url: projectUrl
    });
    
    // Create week object
    weeks.push({
      weekNumber: weekNum,
      title: weekPlan.focus || phase.title || `Week ${weekNum}`,
      objectives: aiTopics.length > 0 ? aiTopics : (phase.skills || roadmap.skills?.slice(0, 3) || ['Learn core concepts', 'Practice skills', 'Build projects']),
      dailyPlan,
      resources: mappedResources,
      guidedProject: {
        title: projectForWeek.title || `Week ${weekNum}: ${weekPlan.focus || 'Practical Project'}`,
        description: projectForWeek.description || `Build a project demonstrating ${weekPlan.focus || 'your skills'}`,
        skills: projectSkills,
        estimatedHours: hoursPerDay * 2,
        difficulty: formData.level || 'beginner',
        url: projectUrl,
        link: projectUrl,
        githubUrl: projectUrl
      },
      resumeBullet: (roadmap.resumeBullets?.[phaseIndex] || `Completed ${weekPlan.focus || `week ${weekNum}`} training in ${formData.goal}`),
      completed: false
    });
  }
  
  // Build the pathway object
  const pathway = {
    title: `${formData.goal} Career Pathway`,
    goal: formData.goal,
    level: formData.level || 'beginner',
    summary: roadmap.summary || `A comprehensive pathway to become a ${formData.goal}`,
    weeklyTimeCommitment: `${(formData.hoursPerDay || 2) * (formData.daysPerWeek || 5)} hours/week`,
    weeks,
    finalPortfolioChecklist: roadmap.nextSteps || [
      'Complete all weekly projects',
      'Build a portfolio website',
      'Create a professional resume',
      'Practice technical interviews',
      'Apply to relevant positions'
    ],
    recommendedCertifications: (roadmap.certifications || []).map(cert => ({
      name: cert.name || cert.title,
      provider: cert.provider || 'Various',
      cost: cert.cost || 'Varies',
      timeToComplete: cert.timeToComplete || cert.duration || 'Varies',
      priority: cert.priority || 'recommended'
    })),
    // Add GitHub projects if available
    githubProjects: (roadmap.githubProjects || []).map(project => ({
      name: project.name || project.title || 'GitHub Project',
      description: project.description || 'No description available',
      url: project.url || project.link || project.html_url || '#',
      stars: project.stars || project.stargazers_count || 0,
      language: project.language || 'Unknown',
      topics: project.topics || []
    })),
    // Add metadata for debugging
    _metadata: {
      usedWatsonx: metadata.usedWatsonx !== false,
      generatedAt: new Date().toISOString(),
      githubProjectsCount: roadmap.githubProjects?.length || 0,
      originalRoadmap: roadmap
    }
  };
  
  console.log('\n' + '='.repeat(80));
  console.log('✅ TRANSFORMATION COMPLETE');
  console.log('='.repeat(80));
  console.log(`📦 Pathway title: ${pathway.title}`);
  console.log(`📅 Weeks: ${pathway.weeks.length}`);
  console.log(`📚 Total resources across all weeks: ${pathway.weeks.reduce((sum, w) => sum + w.resources.length, 0)}`);
  console.log(`🐙 GitHub projects: ${pathway.githubProjects.length}`);
  console.log(`🎓 Certifications: ${pathway.recommendedCertifications.length}`);
  console.log(`🤖 Used WatsonX: ${pathway._metadata.usedWatsonx ? 'Yes' : 'No'}`);
  console.log('='.repeat(80) + '\n');
  
  return pathway;
};

/**
 * Search USAJOBS for federal job postings
 * @param {string} keyword - Search keyword (e.g., "cybersecurity")
 * @param {string} location - Optional location (e.g., "Orlando", "Florida")
 * @returns {Promise<Object>} Job search results with fallback information
 */
export const searchUSAJobs = async (keyword, location = null) => {
  try {
    const params = new URLSearchParams({ keyword });
    if (location) {
      params.append('location', location);
    }
    
    const response = await api.get(`/api/usajobs/search?${params.toString()}`);
    return response.data;
  } catch (error) {
    console.error('Failed to search USAJOBS:', error);
    
    if (error.response) {
      throw new Error(error.response.data.detail || 'Failed to search jobs', { cause: error });
    } else if (error.request) {
      throw new Error('Cannot connect to server. Make sure the backend is running at http://localhost:8000', { cause: error });
    } else {
      throw new Error('An unexpected error occurred', { cause: error });
    }
  }
};

/**
 * Test the API connection
 * @returns {Promise<boolean>} True if connected, false otherwise
 */
export const testConnection = async () => {
  try {
    await checkHealth();
    return true;
  } catch {
    return false;
  }
};

export default api;

// Made with Bob
