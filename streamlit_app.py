import streamlit as st
from main import SEOCrew  # Import the SalesCrew class from main.py
from dotenv import load_dotenv
import os

# Load environment variables from .env file
#load_dotenv()

# The API key will be automatically loaded from .env file
# No need to set it manually if it's in .env

st.title('Your Magic Team')
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["SERPER_API_KEY"] = st.secrets["SERPER_API_KEY"]

with st.sidebar:
    st.header('Enter the Website URL')
    topic = st.text_input("Main website to analyse:")
    #detailed_questions = st.text_area("Specific questions or subtopics you are interested in exploring:")

if st.button('Run analyse'):
    if not topic: #or not detailed_questions
        st.error("Please fill all the fields.")
    else:
        # Create inputs string
        #inputs = f"Topic: {topic}\nDetailed Questions: {detailed_questions}"
        inputs = topic
        
        # Create an instance of the crew with inputs
        seo_crew = SEOCrew(inputs)
        
        # Run the crew
        result = seo_crew.run()
        
        # Display the results
        st.subheader("SEO Analysis Results:")
        st.write(result)