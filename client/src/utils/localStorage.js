/**
 * LocalStorage utility functions for PathPilot AI
 * Handles saving and retrieving pathway data
 */

const PATHWAY_KEY = 'generatedPathway';

/**
 * Save a generated pathway to localStorage
 * @param {Object} pathway - The pathway object from the API
 */
export const savePathway = (pathway) => {
  try {
    localStorage.setItem(PATHWAY_KEY, JSON.stringify(pathway));
    return true;
  } catch (error) {
    console.error('Error saving pathway to localStorage:', error);
    return false;
  }
};

/**
 * Get the saved pathway from localStorage
 * @returns {Object|null} The pathway object or null if not found
 */
export const getPathway = () => {
  try {
    const pathway = localStorage.getItem(PATHWAY_KEY);
    return pathway ? JSON.parse(pathway) : null;
  } catch (error) {
    console.error('Error reading pathway from localStorage:', error);
    return null;
  }
};

/**
 * Clear the saved pathway from localStorage
 */
export const clearPathway = () => {
  try {
    localStorage.removeItem(PATHWAY_KEY);
    return true;
  } catch (error) {
    console.error('Error clearing pathway from localStorage:', error);
    return false;
  }
};

/**
 * Update the saved pathway in localStorage
 * @param {Object} pathway - The updated pathway object
 */
export const updatePathway = (pathway) => {
  try {
    localStorage.setItem(PATHWAY_KEY, JSON.stringify(pathway));
    return true;
  } catch (error) {
    console.error('Error updating pathway in localStorage:', error);
    return false;
  }
};

/**
 * Check if a pathway exists in localStorage
 * @returns {boolean}
 */
export const hasPathway = () => {
  return localStorage.getItem(PATHWAY_KEY) !== null;
};

// Made with Bob
