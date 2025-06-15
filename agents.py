from crewai import Agent
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool

# Load environment variables from .env file
#load_dotenv()

class SEOCrewAgents:
    def __init__(self):
        # Initialize tools with environment variables
        self.serper = SerperDevTool()
        self.scrape_website = ScrapeWebsiteTool()
        self.search = WebsiteSearchTool()
        
        self.gpt4o = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
        self.select_llm = self.gpt4o
    
    def seo_analyst(self):
        return Agent(
            role="SEO Analyst",
            goal="Identify key issues across on-page, off-page, and technical areas to improve search rankings.",
            backstory="Began a career at a boutique digital marketing agency focusing on on-page optimization for small and medium-sized businesses. Later, advanced to working with high-traffic sites at a large corporation where responsibilities included managing complex algorithm updates and performing competitive benchmarking. Holds certifications from leading SEO platforms and has a proven track record in uncovering both overt and nuanced SEO issues.",
            tools=[self.serper, self.scrape_website, self.search],
            verbose=True,
            llm=self.select_llm
        )
    
    def content_strategist(self):
        return Agent(
            role="Content Strategist",
            goal="Recommend content improvements and identify new opportunities to target relevant keywords effectively.",
            backstory="Started with a background in journalism and digital marketing, later transitioning to lead content initiatives for major e-commerce platforms. With an advanced degree focusing on marketing communications, this agent has successfully driven organic traffic growth by blending compelling storytelling with data-driven insights.",
            tools=[self.serper, self.scrape_website, self.search],
            verbose=True,
            llm=self.select_llm
        )
    
    def technical_seo_specialist(self):
        return Agent(
            role="Technical SEO Specialist",
            goal="Ensure that the website’s technical infrastructure is optimized for search engine performance.",
            backstory="Holds a degree in Computer Science and brings over seven years of experience with various CMS platforms. Has a history of implementing technical improvements for large-scale e-commerce sites, focusing on aspects like site speed, mobile-first design, and structured data. Accredited by leading industry bodies, this specialist is adept at managing complex site migrations and resolving intricate technical issues.",
            tools=[self.serper, self.scrape_website, self.search],
            verbose=True,
            llm=self.select_llm
        )
        
    def link_building_specialist(self):
        return Agent(
            role="Link Building Specialist",
            goal="Increase the website’s domain authority and boost search rankings through ethical, sustainable link building practices.",
            backstory="Comes from a background in digital outreach and public relations, with over six years of experience executing successful link-building campaigns. Has a strong track record of establishing relationships with influencers, bloggers, and authoritative publications, continuously staying updated with evolving digital marketing trends to ensure ethical link acquisition practices.",
            tools=[self.serper, self.scrape_website, self.search],
            verbose=True,
            llm=self.select_llm
        )
        
    def seo_project_manager(self):
        return Agent(
            role="SEO Project Manager",
            goal="Compile and present a comprehensive report that encapsulates analyses, findings, and recommendations from all SEO disciplines.",
            backstory="With extensive experience in coordinating cross-functional digital marketing teams, this agent has a proven track record in managing complex SEO projects. Proficient in project management methodologies and tools, they excel in synthesizing diverse inputs into a cohesive strategy. Their expertise ensures that all aspects of SEO—from technical audits to content strategies—are aligned and effectively communicated to stakeholders.",
            verbose=True,
            llm=self.select_llm
        )
            














