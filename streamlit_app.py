import streamlit as st
from main import SEOCrew  # Import the SalesCrew class from main.py
from dotenv import load_dotenv
import os

st.set_page_config(page_title="Your Magic Team", layout="wide")

# Set environment variables from secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["SERPER_API_KEY"] = st.secrets["SERPER_API_KEY"]

# ---- SIDEBAR: Agent Info ----
with st.sidebar:
    st.header('👥 The Agent Team')
    st.markdown("""
**🔍 SEO Analyst**  
Identify key issues across on-page, off-page, and technical areas to improve search rankings.

**📝 Content Strategist**  
Recommend content improvements and identify new opportunities to target relevant keywords effectively.

**🛠️ Technical SEO Specialist**  
Ensure that the website’s technical infrastructure is optimized for search engine performance.

**🔗 Link Building Specialist**  
Increase the website’s domain authority and boost search rankings through ethical, sustainable link building practices.

**📋 SEO Project Manager**  
Oversee the entire SEO project, ensuring all tasks are completed on time and meet quality standards.
""")

# ---- MAIN AREA ----
st.title('Your Magic Team')

st.subheader("Enter the Website URL to Analyse")
topic = st.text_input("Main website (only English websites are supported):")

if st.button('Run analyse'):
    if not topic:
        st.error("Please enter a website URL.")
    else:
        st.subheader("🚀 Running SEO Analysis...")
        log_area = st.empty()

        logs = []
        def stream_log(log_line):
            logs.append(log_line)
            log_area.markdown("```\n" + "\n".join(logs) + "\n```")

        seo_crew = SEOCrew(topic, log_callback=stream_log)
        result = seo_crew.run()

        st.subheader("🔎 SEO Analysis Results")
        st.write(result)
