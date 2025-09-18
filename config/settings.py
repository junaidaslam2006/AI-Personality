"""
Configuration settings for the AI Personality Panel application
"""

import os

# API Configuration
OPENROUTER_API_KEY = "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"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
DEFAULT_MODEL = "deepseek/deepseek-chat"

# App Configuration
APP_CONFIG = {
    "title": "🎭 AI Personality Panel",
    "page_icon": "🎭",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
    "max_tokens": 300,
    "temperature": 0.8
}

# UI Configuration
UI_CONFIG = {
    "primary_color": "#667eea",
    "secondary_color": "#764ba2",
    "background_color": "#f5f7fa",
    "text_color": "#333333",
    "card_border_radius": "15px",
    "button_border_radius": "10px"
}

# Personality Configuration
PERSONALITY_CONFIG = {
    "motivator": {
        "name": "The Motivator",
        "emoji": "💪",
        "color": "#FF6B6B",
        "description": "Positive, encouraging, focused on growth"
    },
    "angry_coach": {
        "name": "The Angry Coach", 
        "emoji": "🔥",
        "color": "#DC143C",
        "description": "Direct, intense, no-nonsense approach"
    },
    "comedian": {
        "name": "The Comedian",
        "emoji": "😄", 
        "color": "#FFD700",
        "description": "Humorous, light-hearted, finds the funny side"
    },
    "philosopher": {
        "name": "The Philosopher",
        "emoji": "🤔",
        "color": "#9B59B6", 
        "description": "Deep thinker, explores meaning and wisdom"
    },
    "practical": {
        "name": "The Practical One",
        "emoji": "📋",
        "color": "#2ECC71",
        "description": "Action-oriented, gives concrete steps"
    },
    "therapist": {
        "name": "The Therapist", 
        "emoji": "💙",
        "color": "#3498DB",
        "description": "Empathetic, supportive, emotionally aware"
    }
}

# Example questions for random generation
EXAMPLE_QUESTIONS = [
    "I failed my exam, what should I do?",
    "I'm feeling overwhelmed at work",
    "Should I quit my job to pursue my dreams?",
    "I'm having relationship problems",
    "I want to start my own business but I'm scared",
    "I feel like I'm not good enough",
    "I can't decide what to study in college",
    "My friends don't support my goals",
    "I'm procrastinating too much",
    "I don't know what I want to do with my life",
    "I'm struggling with anxiety",
    "I feel stuck in life",
    "How do I build confidence?",
    "I'm afraid of failure",
    "I need to make a difficult decision",
    "I'm dealing with rejection",
    "How do I handle criticism?",
    "I'm feeling burned out",
    "I want to change careers",
    "I'm having trouble with motivation"
]

# CSS Styles
CUSTOM_CSS = """
/* Main header styling */
.main-header {
    text-align: center;
    font-size: 3rem;
    font-weight: bold;
    margin-bottom: 2rem;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 1.2rem;
    margin-bottom: 3rem;
    font-style: italic;
}

/* Personality cards */
.personality-card {
    border-radius: 15px;
    padding: 20px;
    margin: 15px 0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    position: relative;
    overflow: hidden;
}

.personality-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
}

.personality-title {
    font-size: 1.4rem;
    font-weight: bold;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.personality-response {
    font-size: 1.1rem;
    line-height: 1.6;
    background: rgba(255,255,255,0.1);
    padding: 15px;
    border-radius: 10px;
    margin-top: 10px;
    backdrop-filter: blur(5px);
}

.input-container {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    padding: 30px;
    border-radius: 20px;
    margin-bottom: 30px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
}

/* Button styling */
.stButton > button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.6rem 2rem;
    font-weight: 600;
    font-size: 1.1rem;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
}
"""