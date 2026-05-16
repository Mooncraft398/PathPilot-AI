"""
Multi-Call WatsonX Generation Strategy
Breaks large roadmap generation into smaller, more reliable calls.
"""

import logging
from typing import Dict, Any, List, Optional
from services.watsonx_service import watsonx_service

logger = logging.getLogger(__name__)


class MultiCallGenerator:
    """
    Handles multi-call generation strategy for large roadmaps.
    Breaks generation into smaller chunks to avoid truncation.
    """
    
    # Token limits based on IBM Granite 3 8B Instruct model
    # Context window: 8192 tokens
    # Safe max_new_tokens per call: 2000-3000 (to avoid truncation)
    TOKEN_LIMITS = {
        'summary': 1500,      # Summary, phases, skills, tools
        'weekly_chunk': 2500,  # 4 weeks of detailed plans
        'projects': 2000,      # Project ideas and descriptions
        'resources': 1500      # Learning resources
    }
    
    async def generate_roadmap_summary(
        self,
        career_goal: str,
        current_skills: List[str],
        timeframe: str
    ) -> Optional[Dict[str, Any]]:
        """
        Generate high-level roadmap summary
        
        Returns:
            Dict with summary, phases, skills, tools, resumeBullets
        """
        logger.info("=" * 80)
        logger.info("📋 GENERATING ROADMAP SUMMARY (Call 1)")
        logger.info("=" * 80)
        
        skills_text = ", ".join(current_skills) if current_skills else "none"
        
        prompt = f"""Generate a career roadmap summary for: {career_goal}

Current skills: {skills_text}
Timeframe: {timeframe}

Return ONLY valid JSON. NO markdown. NO code fences. NO explanations.
Start with {{ and end with }}.

{{
  "summary": "One sentence overview of the learning path",
  "phases": [
    {{"phase": 1, "title": "Foundation", "duration": "4 weeks", "focus": "Learn basics", "skills": ["skill1", "skill2"]}},
    {{"phase": 2, "title": "Practice", "duration": "4 weeks", "focus": "Build projects", "skills": ["skill3", "skill4"]}},
    {{"phase": 3, "title": "Portfolio", "duration": "4 weeks", "focus": "Create portfolio", "skills": ["skill5", "skill6"]}}
  ],
  "skills": ["skill1", "skill2", "skill3", "skill4", "skill5"],
  "tools": ["tool1", "tool2", "tool3", "tool4"],
  "resumeBullets": [
    "Completed {timeframe} training in {career_goal}",
    "Built portfolio projects",
    "Learned key skills"
  ],
  "nextSteps": [
    "Start with first resource",
    "Set up environment",
    "Join community"
  ]
}}

CRITICAL: Return ONLY the JSON object. Complete the ENTIRE JSON."""
        
        result = await watsonx_service.generate_text(
            prompt=prompt,
            max_tokens=self.TOKEN_LIMITS['summary'],
            temperature=0.7
        )
        
        if not result:
            logger.error("❌ Summary generation failed")
            return None
        
        return self._parse_json_response(result['generated_text'], 'summary')
    
    async def generate_weekly_chunk(
        self,
        career_goal: str,
        phase_info: Dict[str, Any],
        start_week: int,
        num_weeks: int = 4
    ) -> Optional[List[Dict[str, Any]]]:
        """
        Generate detailed weekly plans for a chunk of weeks
        
        Args:
            career_goal: Target career role
            phase_info: Phase information (title, focus, skills)
            start_week: Starting week number
            num_weeks: Number of weeks to generate (default 4)
        
        Returns:
            List of weekly plan dictionaries
        """
        logger.info("=" * 80)
        logger.info(f"📅 GENERATING WEEKS {start_week}-{start_week + num_weeks - 1}")
        logger.info("=" * 80)
        
        phase_title = phase_info.get('title', 'Learning Phase')
        phase_focus = phase_info.get('focus', 'Build skills')
        phase_skills = phase_info.get('skills', [])
        
        prompt = f"""Generate {num_weeks} weeks of detailed learning plans for: {career_goal}

Phase: {phase_title}
Focus: {phase_focus}
Skills: {', '.join(phase_skills)}
Starting at week {start_week}

Return ONLY valid JSON array. NO markdown. NO code fences.
Start with [ and end with ].

[
  {{
    "week": {start_week},
    "focus": "Specific focus for week {start_week}",
    "topics": ["Topic 1", "Topic 2", "Topic 3"],
    "dailyTasks": ["Task 1", "Task 2", "Task 3", "Task 4", "Task 5"]
  }},
  {{
    "week": {start_week + 1},
    "focus": "Different focus for week {start_week + 1}",
    "topics": ["Topic A", "Topic B", "Topic C"],
    "dailyTasks": ["Task A", "Task B", "Task C", "Task D", "Task E"]
  }}
]

Generate {num_weeks} unique weeks. Each week should have:
- Different focus area
- 3-4 specific topics
- 5 concrete daily tasks
- Progressive difficulty

CRITICAL: Return ONLY the JSON array. Complete ALL {num_weeks} weeks."""
        
        result = await watsonx_service.generate_text(
            prompt=prompt,
            max_tokens=self.TOKEN_LIMITS['weekly_chunk'],
            temperature=0.7
        )
        
        if not result:
            logger.error(f"❌ Weekly chunk generation failed for weeks {start_week}-{start_week + num_weeks - 1}")
            return None
        
        return self._parse_json_response(result['generated_text'], 'weekly_chunk')
    
    def _parse_json_response(self, text: str, section_name: str) -> Optional[Any]:
        """
        Parse JSON from WatsonX response with enhanced error handling
        
        Args:
            text: Generated text from WatsonX
            section_name: Name of section for logging
        
        Returns:
            Parsed JSON object or None
        """
        import json
        import re
        
        logger.info(f"🔍 Parsing JSON for {section_name}")
        logger.info(f"   Raw text length: {len(text)} characters")
        
        # Clean the text
        cleaned = text.strip()
        
        # Remove markdown code fences if present
        cleaned = re.sub(r'^```json\s*', '', cleaned)
        cleaned = re.sub(r'^```\s*', '', cleaned)
        cleaned = re.sub(r'\s*```$', '', cleaned)
        cleaned = cleaned.strip()
        
        # Log first and last characters
        logger.info(f"   First 100 chars: {cleaned[:100]}")
        logger.info(f"   Last 100 chars: {cleaned[-100:]}")
        
        # Find JSON boundaries
        first_brace = cleaned.find('{')
        first_bracket = cleaned.find('[')
        last_brace = cleaned.rfind('}')
        last_bracket = cleaned.rfind(']')
        
        logger.info(f"   First {{ at: {first_brace}, First [ at: {first_bracket}")
        logger.info(f"   Last }} at: {last_brace}, Last ] at: {last_bracket}")
        
        # Determine if it's an object or array
        if first_brace != -1 and (first_bracket == -1 or first_brace < first_bracket):
            # It's an object
            if first_brace == -1 or last_brace == -1:
                logger.error(f"❌ NO JSON OBJECT FOUND IN {section_name}")
                logger.error(f"   Full cleaned text: {cleaned[:500]}")
                return None
            
            json_str = cleaned[first_brace:last_brace + 1]
        elif first_bracket != -1:
            # It's an array
            if first_bracket == -1 or last_bracket == -1:
                logger.error(f"❌ NO JSON ARRAY FOUND IN {section_name}")
                logger.error(f"   Full cleaned text: {cleaned[:500]}")
                return None
            
            json_str = cleaned[first_bracket:last_bracket + 1]
        else:
            logger.error(f"❌ NO JSON FOUND IN {section_name}")
            logger.error(f"   Full cleaned text: {cleaned[:500]}")
            return None
        
        # Check for truncation
        if not (json_str.rstrip().endswith('}') or json_str.rstrip().endswith(']')):
            logger.warning(f"⚠️  RESPONSE APPEARS TRUNCATED for {section_name}")
            logger.warning(f"   Last 200 chars: {json_str[-200:]}")
        
        # Try to parse
        try:
            parsed = json.loads(json_str)
            logger.info(f"✅ Successfully parsed JSON for {section_name}")
            return parsed
        except json.JSONDecodeError as e:
            logger.error(f"❌ JSON PARSE ERROR in {section_name}: {e}")
            logger.error(f"   Error at position {e.pos}")
            logger.error(f"   Context: {json_str[max(0, e.pos - 50):min(len(json_str), e.pos + 50)]}")
            return None
    
    async def generate_full_roadmap(
        self,
        career_goal: str,
        current_skills: List[str],
        timeframe: str,
        local_resources: Dict[str, Any],
        github_projects: List[Dict[str, Any]]
    ) -> Optional[Dict[str, Any]]:
        """
        Generate complete roadmap using multi-call strategy
        
        Args:
            career_goal: Target career role
            current_skills: List of current skills
            timeframe: Available timeframe (e.g., "3 months")
            local_resources: Curated resources from local data
            github_projects: Relevant GitHub projects
        
        Returns:
            Complete roadmap dictionary or None on error
        """
        logger.info("=" * 80)
        logger.info("🚀 MULTI-CALL ROADMAP GENERATION")
        logger.info("=" * 80)
        logger.info(f"Career Goal: {career_goal}")
        logger.info(f"Timeframe: {timeframe}")
        logger.info(f"Strategy: Multi-call (summary + weekly chunks)")
        logger.info("=" * 80)
        
        # Call 1: Generate summary
        summary_data = await self.generate_roadmap_summary(
            career_goal=career_goal,
            current_skills=current_skills,
            timeframe=timeframe
        )
        
        if not summary_data:
            logger.error("❌ Failed to generate summary, aborting multi-call generation")
            return None
        
        logger.info("✅ Summary generated successfully")
        
        # Determine number of weeks based on timeframe
        weeks_needed = self._calculate_weeks_from_timeframe(timeframe)
        logger.info(f"📅 Generating {weeks_needed} weeks of content")
        
        # Generate weekly plans in chunks of 4
        all_weekly_plans = []
        phases = summary_data.get('phases', [])
        
        for i in range(0, weeks_needed, 4):
            chunk_size = min(4, weeks_needed - i)
            start_week = i + 1
            
            # Determine which phase this chunk belongs to
            phase_index = min(i // 4, len(phases) - 1) if phases else 0
            phase_info = phases[phase_index] if phases else {
                'title': 'Learning Phase',
                'focus': 'Build skills',
                'skills': summary_data.get('skills', [])[:3]
            }
            
            weekly_chunk = await self.generate_weekly_chunk(
                career_goal=career_goal,
                phase_info=phase_info,
                start_week=start_week,
                num_weeks=chunk_size
            )
            
            if weekly_chunk:
                all_weekly_plans.extend(weekly_chunk)
                logger.info(f"✅ Generated weeks {start_week}-{start_week + chunk_size - 1}")
            else:
                logger.warning(f"⚠️  Failed to generate weeks {start_week}-{start_week + chunk_size - 1}, using fallback")
                # Generate fallback weeks
                for week_num in range(start_week, start_week + chunk_size):
                    all_weekly_plans.append(self._create_fallback_week(week_num, phase_info))
        
        # Combine everything
        roadmap = {
            **summary_data,
            'weeklyPlan': all_weekly_plans,
            'resources': local_resources.get('resources', [])[:10],
            'githubProjects': github_projects[:5],
            'portfolioProjects': self._generate_portfolio_projects(summary_data.get('skills', []), career_goal),
            'metadata': {
                'usedWatsonx': True,
                'generationStrategy': 'multi_call',
                'requestedWeeks': weeks_needed,
                'generatedWeeks': len(all_weekly_plans),
                'model': 'ibm/granite-3-8b-instruct',
                'calls': {
                    'summary': 1,
                    'weekly_chunks': (weeks_needed + 3) // 4
                }
            }
        }
        
        logger.info("=" * 80)
        logger.info("✅ MULTI-CALL GENERATION COMPLETE")
        logger.info("=" * 80)
        logger.info(f"   Phases: {len(roadmap.get('phases', []))}")
        logger.info(f"   Weekly Plans: {len(roadmap.get('weeklyPlan', []))}")
        logger.info(f"   Skills: {len(roadmap.get('skills', []))}")
        logger.info(f"   Tools: {len(roadmap.get('tools', []))}")
        logger.info(f"   Resources: {len(roadmap.get('resources', []))}")
        logger.info(f"   GitHub Projects: {len(roadmap.get('githubProjects', []))}")
        logger.info("=" * 80)
        
        return roadmap
    
    def _calculate_weeks_from_timeframe(self, timeframe: str) -> int:
        """Calculate number of weeks from timeframe string"""
        timeframe_lower = timeframe.lower()
        
        if 'month' in timeframe_lower:
            # Extract number of months
            import re
            match = re.search(r'(\d+)', timeframe_lower)
            if match:
                months = int(match.group(1))
                return months * 4  # 4 weeks per month
        
        if 'week' in timeframe_lower:
            import re
            match = re.search(r'(\d+)', timeframe_lower)
            if match:
                return int(match.group(1))
        
        # Default to 12 weeks (3 months)
        return 12
    
    def _create_fallback_week(self, week_num: int, phase_info: Dict[str, Any]) -> Dict[str, Any]:
        """Create a fallback week when generation fails"""
        return {
            'week': week_num,
            'focus': f"{phase_info.get('title', 'Learning')} - Week {week_num}",
            'topics': phase_info.get('skills', ['Core concepts', 'Practice', 'Projects'])[:3],
            'dailyTasks': [
                f"Study {phase_info.get('focus', 'core concepts')}",
                "Complete practice exercises",
                "Work on weekly project",
                "Review and document learning",
                "Prepare for next week"
            ]
        }
    
    def _generate_portfolio_projects(self, skills: List[str], career_goal: str) -> List[Dict[str, Any]]:
        """Generate portfolio project ideas based on skills"""
        return [
            {
                'title': f"Beginner {career_goal} Project",
                'description': f"Build a practical project demonstrating {', '.join(skills[:2])}",
                'skills': skills[:3],
                'estimatedHours': 8,
                'difficulty': 'beginner'
            },
            {
                'title': f"Intermediate {career_goal} Project",
                'description': f"Create a more complex project showcasing {', '.join(skills[2:4])}",
                'skills': skills[2:5] if len(skills) > 2 else skills,
                'estimatedHours': 16,
                'difficulty': 'intermediate'
            }
        ]


# Global instance
multi_call_generator = MultiCallGenerator()

# Made with Bob
