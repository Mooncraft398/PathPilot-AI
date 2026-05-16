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
