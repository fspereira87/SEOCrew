import os
import streamlit as st
from main import SEOCrew
from dotenv import load_dotenv

# Load local .env if present
load_dotenv()

st.set_page_config(page_title="Your Magic Team", layout="wide")

    
    #st.secrets["OPENAI_API_KEY"]

# ---- SIDEBAR ----
with st.sidebar:
    st.header('👥 The Agent Team')
    st.markdown("""
**🔍 SEO Analyst**  
Identify key issues across on-page, off-page, and technical areas.

**📝 Content Strategist**  
Recommend content improvements and new keyword opportunities.

**🛠️ Technical SEO Specialist**  
Optimize technical infrastructure and performance.

**🔗 Link Building Specialist**  
Grow authority through ethical link acquisition.

**📋 SEO Project Manager**  
Compile findings into a clear SEO roadmap.
""")

# ---- MAIN ----
st.title('Your Magic Team')

st.subheader("Enter the Website URL to Analyse")
website_url = st.text_input("Website URL (English only):")

if st.button('Run analysis'):
    if not website_url:
        st.error("Please enter a website URL.")
    else:
        st.subheader("🚀 Running SEO Analysis...")
        log_area = st.empty()
        logs = []

        def stream_log(log_line):
            logs.append(log_line)
            log_area.markdown("```\n" + "\n".join(logs) + "\n```")

        seo_crew = SEOCrew(website_url, log_callback=stream_log)
        result = seo_crew.run()

        st.subheader("🔎 SEO Analysis Results")
        st.write(result)
