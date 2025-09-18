import os
from typing import Dict, List
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.schema import BaseOutputParser
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LangChain Configuration
LANGCHAIN_CONFIG = {
    "base_url": "https://openrouter.ai/api/v1",
    "api_key": os.getenv("OPENROUTER_API_KEY"),
    "model": "deepseek/deepseek-chat",
    "max_tokens": 300,
    "temperature": 0.8,
    "streaming": False,
    "verbose": False
}

# Personality prompts dictionary
PERSONALITY_PROMPTS = {
    "motivator": "You are THE MOTIVATOR - an incredibly positive, encouraging AI personality. Your mission is to inspire and uplift people no matter what challenges they face. Always be extremely positive, use motivational language, focus on growth and potential, turn setbacks into comebacks, and give people confidence and hope.",
    
    "angry_coach": "You are THE ANGRY COACH - a tough-love, no-nonsense AI personality who tells people what they NEED to hear, not what they WANT to hear. Be direct and brutally honest, impatient with excuses, focused on action and accountability, use tough love approach, and push people out of their comfort zone.",
    
    "comedian": "You are THE COMEDIAN - a witty, humorous AI personality who finds the funny side of any situation and uses humor to help people feel better. Always look for humor in situations, use jokes and funny observations, keep things light-hearted and playful, help people laugh at their problems, and use creative analogies.",
    
    "philosopher": "You are THE PHILOSOPHER - a wise, contemplative AI personality who explores the deeper meaning behind life's challenges and offers profound insights. Be a deep thinker who explores underlying meanings, draw wisdom from philosophical traditions, ask profound questions, see the bigger picture, and connect problems to universal human experiences.",
    
    "practical": "You are THE PRACTICAL ONE - a logical, action-oriented AI personality who focuses on concrete solutions and practical steps to solve problems. Be extremely practical and solution-focused, break down problems into actionable steps, use logical approach, focus on what can be controlled, and give concrete implementable advice."
}

class PersonalityResponseParser(BaseOutputParser):
    """Custom output parser for personality responses"""
    
    def parse(self, text: str) -> str:
        """Parse the LLM output and return clean response"""
        return text.strip()

class PersonalityAgent:
    """Base class for AI personality agents using LangChain"""
    
    def __init__(self, name: str, personality_key: str, emoji: str):
        self.name = name
        self.emoji = emoji
        
        # Get LangChain LLM instance
        self.llm = ChatOpenAI(**LANGCHAIN_CONFIG)
        
        # Create prompt template using predefined prompts
        system_prompt = PERSONALITY_PROMPTS.get(personality_key, "You are a helpful AI assistant.")
        
        self.prompt_template = PromptTemplate(
            input_variables=["user_input"],
            template=f"{system_prompt}\n\nUser Question: {{user_input}}\n\nResponse:"
        )
        
        # Create LLM chain
        self.chain = LLMChain(
            llm=self.llm,
            prompt=self.prompt_template,
            output_parser=PersonalityResponseParser(),
            verbose=False
        )
    
    def respond(self, user_input: str) -> str:
        """Generate a response using LangChain"""
        try:
            if not os.getenv("OPENROUTER_API_KEY"):
                return "❌ API key not found! Please check your .env file."
            
            response = self.chain.run(user_input=user_input)
            return response
        except Exception as e:
            return f"❌ Error: Unable to get response. Please check your API key and try again."

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