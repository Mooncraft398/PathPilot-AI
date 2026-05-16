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
  console.log('🔄 Transforming Watsonx.ai roadmap to pathway format...');
  console.log('Input roadmap:', roadmapResponse);
  console.log('Form data:', formData);
  
  const roadmap = roadmapResponse.roadmap || {};
  const metadata = roadmapResponse.metadata || {};
  
  // Log whether WatsonX was used
  if (metadata.usedWatsonx === true) {
    console.log('✅ USING WATSONX.AI GENERATED ROADMAP');
    console.log(`   Model: ${metadata.model || 'unknown'}`);
    console.log(`   Tokens: ${metadata.tokens || 0}`);
  } else {
    console.warn('⚠️  USING FALLBACK TEMPLATE DATA (WatsonX unavailable)');
    console.warn(`   Reason: ${metadata.fallbackReason || 'unknown'}`);
  }
  
  // Transform phases into weeks
  const weeks = [];
  const phases = roadmap.phases || [];
  const weeklyPlan = roadmap.weeklyPlan || [];
  
  // Calculate weeks from timeframe (e.g., "3 months" -> 12 weeks)
  let totalWeeks = formData.weeks || 12;
  if (formData.timeframe) {
    const monthMatch = formData.timeframe.match(/(\d+)\s*month/i);
    if (monthMatch) {
      totalWeeks = parseInt(monthMatch[1]) * 4;
    }
  }
  
  // Create weeks from phases and weekly plan
  for (let i = 0; i < totalWeeks; i++) {
    const weekNum = i + 1;
    const phaseIndex = Math.floor(i / (totalWeeks / Math.max(phases.length, 1)));
    const phase = phases[phaseIndex] || phases[0] || {};
    const weekPlan = weeklyPlan[i] || {};
    
    // Generate daily plan using AI-provided data when available
    const dailyPlan = [];
    const daysPerWeek = formData.daysPerWeek || 5;
    const hoursPerDay = formData.hoursPerDay || 2;
    
    // Use AI-generated daily tasks if available, otherwise create varied tasks
    const aiDailyTasks = weekPlan.dailyTasks || [];
    const aiTopics = weekPlan.topics || phase.skills || [];
    
    for (let day = 1; day <= daysPerWeek; day++) {
      // Create unique tasks for each day
      const dayTasks = [];
      
      if (aiDailyTasks.length >= day) {
        // Use AI-generated task for this day
        dayTasks.push(aiDailyTasks[day - 1]);
      } else {
        // Generate varied tasks based on week focus and topics
        if (day === 1) {
          dayTasks.push(`Introduction to ${weekPlan.focus || phase.title || 'this week\'s topic'}`);
        } else if (day === daysPerWeek) {
          dayTasks.push(`Complete ${weekPlan.focus || 'weekly'} project and review`);
        } else if (aiTopics[day - 2]) {
          dayTasks.push(`Deep dive into ${aiTopics[day - 2]}`);
        } else {
          dayTasks.push(`Continue practicing ${weekPlan.focus || phase.focus || 'core concepts'}`);
        }
      }
      
      // Add 2-3 more tasks per day for variety
      if (aiTopics.length > 0) {
        const topicIndex = (day - 1) % aiTopics.length;
        dayTasks.push(`Practice: ${aiTopics[topicIndex]}`);
      }
      dayTasks.push(`Work on hands-on exercises`);
      
      dailyPlan.push({
        day,
        focus: weekPlan.focus || phase.focus || `Day ${day}: ${aiTopics[day - 1] || 'Continue learning'}`,
        tasks: dayTasks,
        estimatedHours: hoursPerDay
      });
    }
    
    // Use week-specific resources if provided by AI
    const weekResources = weekPlan.resources || roadmap.resources || [];
    const resourcesForWeek = weekResources.slice(i * 2, i * 2 + 5); // Different resources per week
    
    // Create week object
    weeks.push({
      weekNumber: weekNum,
      title: weekPlan.focus || phase.title || `Week ${weekNum}`,
      objectives: aiTopics.length > 0 ? aiTopics : (phase.skills || roadmap.skills?.slice(0, 3) || ['Learn core concepts', 'Practice skills', 'Build projects']),
      dailyPlan,
      resources: resourcesForWeek.map(r => ({
        title: r.title || r.name || 'Learning Resource',
        type: r.type || 'article',
        url: r.url || r.link || '#',
        duration: r.duration || '1-2 hours',
        isFree: r.isFree !== false
      })),
      guidedProject: {
        title: (roadmap.portfolioProjects?.[phaseIndex]?.title || `Week ${weekNum}: ${weekPlan.focus || 'Practical Project'}`),
        description: (roadmap.portfolioProjects?.[phaseIndex]?.description || `Build a project demonstrating ${weekPlan.focus || 'your skills'}`),
        skills: aiTopics.length > 0 ? aiTopics : (phase.skills || roadmap.skills?.slice(0, 3) || ['Problem Solving']),
        estimatedHours: hoursPerDay * 2,
        difficulty: formData.level || 'beginner'
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
    // Add metadata for debugging
    _metadata: {
      usedWatsonx: metadata.usedWatsonx !== false,
      generatedAt: new Date().toISOString(),
      originalRoadmap: roadmap
    }
  };
  
  console.log('✅ Transformation complete');
  console.log('📦 Transformed pathway:', pathway);
  
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
