from crewai import Agent
from langchain_openai import ChatOpenAI

from tools.search import DuckDuckGoSearchTool
from tools.web_scraper import ScrapeWebsiteTool


class SEOCrewAgents:
    def __init__(self):
        # Tools (CrewAI-native)
        self.search_tool = DuckDuckGoSearchTool()
        self.scrape_tool = ScrapeWebsiteTool()

        # LLM
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.7
        )

    def seo_analyst(self):
        return Agent(
            role="SEO Analyst",
            goal=(
                "Identify key SEO issues and opportunities across on-page, "
                "off-page, and technical SEO dimensions."
            ),
            backstory=(
                "An experienced SEO analyst with a background in auditing "
                "medium to large websites, specializing in uncovering "
                "technical issues, content gaps, and ranking opportunities."
            ),
            tools=[self.search_tool, self.scrape_tool],
            verbose=True,
            llm=self.llm
        )

    def content_strategist(self):
        return Agent(
            role="Content Strategist",
            goal=(
                "Recommend content improvements and identify new opportunities "
                "to target relevant keywords effectively."
            ),
            backstory=(
                "A former journalist turned SEO content strategist, skilled "
                "at aligning search intent with high-performing content formats."
            ),
            tools=[self.search_tool, self.scrape_tool],
            verbose=True,
            llm=self.llm
        )

    def technical_seo_specialist(self):
        return Agent(
            role="Technical SEO Specialist",
            goal=(
                "Ensure that the website’s technical infrastructure is optimized "
                "for search engine crawling, indexing, and performance."
            ),
            backstory=(
                "A technically minded SEO expert with experience in site speed, "
                "schema markup, mobile optimization, and large-scale audits."
            ),
            tools=[self.scrape_tool],
            verbose=True,
            llm=self.llm
        )

    def link_building_specialist(self):
        return Agent(
            role="Link Building Specialist",
            goal=(
                "Increase the website’s domain authority and rankings through "
                "ethical, sustainable link-building strategies."
            ),
            backstory=(
                "A digital PR and outreach expert who focuses on white-hat "
                "link acquisition and competitor backlink analysis."
            ),
            tools=[self.search_tool],
            verbose=True,
            llm=self.llm
        )

    def seo_project_manager(self):
        return Agent(
            role="SEO Project Manager",
            goal=(
                "Compile insights from all SEO specialists into a structured, "
                "actionable SEO roadmap and final report."
            ),
            backstory=(
                "A seasoned project manager who translates complex SEO findings "
                "into clear strategies, timelines, and priorities for stakeholders."
            ),
            verbose=True,
            llm=self.llm
        )
