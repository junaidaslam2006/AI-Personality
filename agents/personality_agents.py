import os
from typing import Dict, List
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(dotenv_path=env_path, override=True)  # Override existing env vars

# Debug: Print to check if API key is loaded
api_key = os.getenv("OPENROUTER_API_KEY")

# Check if API key is loaded properly
if not api_key:
    print("ERROR: No API key found in environment variables!")
    print("Please make sure OPENROUTER_API_KEY is set in your .env file")
else:
    print("SUCCESS: API Key loaded from environment")
    print(f"API Key starts with: {api_key[:10]}...")
    print(f"API Key length: {len(api_key)}")

# OpenAI Client Configuration for OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

# Personality prompts dictionary - concise versions
PERSONALITY_PROMPTS = {
    "motivator": "You are THE MOTIVATOR - an incredibly positive, encouraging AI personality. Your mission is to inspire and uplift people. Always be extremely positive, use motivational language, focus on growth and potential, turn setbacks into comebacks. KEEP RESPONSES 30-50 WORDS.",
    
    "angry_coach": "You are THE ANGRY COACH - a tough-love, no-nonsense AI personality who tells people what they NEED to hear, not what they WANT to hear. Be direct and brutally honest, impatient with excuses, focused on action and accountability. KEEP RESPONSES 30-50 WORDS.",
    
    "comedian": "You are THE COMEDIAN - a witty, humorous AI personality who finds the funny side of any situation and uses humor to help people feel better. Always look for humor, use jokes and funny observations, keep things light-hearted and playful. KEEP RESPONSES 30-50 WORDS.",
    
    "philosopher": "You are THE PHILOSOPHER - a wise, contemplative AI personality who explores the deeper meaning behind life's challenges and offers profound insights. Be a deep thinker, draw wisdom from philosophical traditions, see the bigger picture. KEEP RESPONSES 30-50 WORDS.",
    
    "practical": "You are THE PRACTICAL ONE - a logical, action-oriented AI personality who focuses on concrete solutions and practical steps. Be extremely practical and solution-focused, break down problems into actionable steps, focus on what can be controlled. KEEP RESPONSES 30-50 WORDS."
}

class PersonalityAgent:
    """Base class for AI personality agents using OpenAI client"""
    
    def __init__(self, name: str, personality_key: str, emoji: str):
        self.name = name
        self.emoji = emoji
        self.system_prompt = PERSONALITY_PROMPTS.get(personality_key, "You are a helpful AI assistant.")
    
    def respond(self, user_input: str) -> str:
        """Generate a response using OpenAI client"""
        try:
            # Check if API key is available
            if not api_key:
                return "ERROR: API key not found. Please add OPENROUTER_API_KEY to your .env file."
            
            # Make API call to OpenRouter
            response = client.chat.completions.create(
                model="deepseek/deepseek-chat",
                messages=[
                    {"role": "system", "content": f"{self.system_prompt}\n\nIMPORTANT: Keep your response between 30-50 words. Be concise and direct."},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=80,  # Reduced for shorter responses
                temperature=0.8
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            error_msg = str(e).lower()
            if "401" in error_msg or "unauthorized" in error_msg or "user not found" in error_msg:
                return "ERROR: API key authentication failed. Please check if your OpenRouter API key is valid."
            elif "network" in error_msg or "connection" in error_msg:
                return "ERROR: Network error. Please check your internet connection."
            else:
                return f"ERROR: Service temporarily unavailable. Please try again."

class MotivatorAgent(PersonalityAgent):
    """The encouraging, positive motivator personality"""
    
    def __init__(self):
        super().__init__("Motivator", "motivator", "💪")

class AngryCoachAgent(PersonalityAgent):
    """The tough-love, no-nonsense coach personality"""
    
    def __init__(self):
        super().__init__("Angry Coach", "angry_coach", "🔥")

class ComedianAgent(PersonalityAgent):
    """The humorous, light-hearted comedian personality"""
    
    def __init__(self):
        super().__init__("Comedian", "comedian", "😄")

class PhilosopherAgent(PersonalityAgent):
    """The deep-thinking, wise philosopher personality"""
    
    def __init__(self):
        super().__init__("Philosopher", "philosopher", "🤔")

class PracticalAgent(PersonalityAgent):
    """The action-oriented, practical problem-solver personality"""
    
    def __init__(self):
        super().__init__("Practical", "practical", "📋")

class PersonalityPanel:
    """Main class that manages all personality agents using LangChain"""
    
    def __init__(self):
        # Initialize all personality agents
        self.agents = self._create_agents()
    
    def _create_agents(self) -> Dict[str, PersonalityAgent]:
        """Create and return all personality agents"""
        return {
            "motivator": MotivatorAgent(),
            "angry_coach": AngryCoachAgent(),
            "comedian": ComedianAgent(),
            "philosopher": PhilosopherAgent(),
            "practical": PracticalAgent()
        }
    
    def get_response(self, personality: str, user_input: str) -> str:
        """Get response from a specific personality using LangChain"""
        if personality in self.agents:
            return self.agents[personality].respond(user_input)
        else:
            return f"Personality '{personality}' not found!"
    
    def get_all_responses(self, user_input: str) -> Dict[str, str]:
        """Get responses from all personalities using LangChain parallel processing"""
        responses = {}
        
        # Use LangChain's built-in capabilities for efficient processing
        for personality_name, agent in self.agents.items():
            try:
                responses[personality_name] = agent.respond(user_input)
            except Exception as e:
                responses[personality_name] = f"Error getting response: {str(e)}"
        
        return responses
    
    def get_available_personalities(self) -> List[str]:
        """Get list of available personalities"""
        return list(self.agents.keys())