import streamlit as st
import os
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from agents.personality_agents import PersonalityPanel

# Configure page
st.set_page_config(
    page_title="🎭 AI Personality Panel",
    page_icon="🎭",
    layout="wide"
)

# Simple CSS for basic styling
st.markdown("""
<style>
.output-box {
    border: 2px solid #ddd;
    padding: 15px;
    border-radius: 10px;
    margin: 10px 0;
    min-height: 100px;
    background-color: #f8f9fa;
    color: #333333;
}
.personality-title {
    font-weight: bold;
    font-size: 18px;
    margin-bottom: 10px;
    color: #2c3e50;
}
.output-text {
    color: #444444;
    line-height: 1.5;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

def main():
    # Initialize personality panel
    if 'personality_panel' not in st.session_state:
        st.session_state.personality_panel = PersonalityPanel()
    
    # Title
    st.title("🎭 AI Personality Panel")
    
    # Input box
    user_input = st.text_area("Ask your question:", placeholder="Type your question here...", height=100)
    
    # Submit button
    if st.button("Get Answers", use_container_width=True):
        if user_input.strip():
            # Get responses from all personalities
            with st.spinner("Getting responses..."):
                responses = st.session_state.personality_panel.get_all_responses(user_input)
            
            # Create 5 columns for output boxes
            col1, col2, col3, col4, col5 = st.columns(5)
            
            # Display each personality response
            personalities = [
                ("angry_coach", "� Angry Coach", col1),
                ("philosopher", "🤔 Philosopher", col2), 
                ("comedian", "😄 Comedian", col3),
                ("motivator", "💪 Motivator", col4),
                ("practical", "📋 Practical", col5)
            ]
            
            for personality_key, title, column in personalities:
                with column:
                    st.markdown(f"""
                    <div class="output-box">
                        <div class="personality-title">{title}</div>
                        <div class="output-text">{responses.get(personality_key, "No response")}</div>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.error("Please enter a question first!")

if __name__ == "__main__":
    main()