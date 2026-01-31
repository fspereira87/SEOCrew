from crewai import Crew, Process
from agents import SEOCrewAgents
from tasks import SEOCrewTasks


class SEOCrew:
    def __init__(self, website_url, log_callback=None):
        self.website_url = website_url
        self.agents = SEOCrewAgents()
        self.tasks = SEOCrewTasks()
        self.log_callback = log_callback or (lambda x: None)

    def log(self, message):
        print(message)
        self.log_callback(message)

    def run(self):
        self.log("👤 Initializing agents...")
        seo_analyst = self.agents.seo_analyst()
        content = self.agents.content_strategist()
        technical = self.agents.technical_seo_specialist()
        link_builder = self.agents.link_building_specialist()
        manager = self.agents.seo_project_manager()

        self.log("📌 Defining tasks...")

        # Base audit (root task)
        analyst_task = self.tasks.seo_analyses_task(
            seo_analyst,
            self.website_url
        )

        # Dependent tasks
        technical_task = self.tasks.technical_seo_task(
            technical,
            self.website_url,
            analyst_task
        )

        content_task = self.tasks.content_specialist_task(
            content,
            self.website_url,
            analyst_task
        )

        link_building_task = self.tasks.link_building_task(
            link_builder,
            self.website_url,
            analyst_task
        )

        # Manager depends on everything
        manager_task = self.tasks.seo_manager_task(
            manager,
            self.website_url,
            analyst_task,
            technical_task,
            content_task,
            link_building_task
        )

        self.log("🚀 Kicking off Crew...")
        crew = Crew(
            agents=[
                seo_analyst,
                content,
                technical,
                link_builder,
                manager
            ],
            tasks=[
                analyst_task,
                technical_task,
                content_task,
                link_building_task,
                manager_task
            ],
            process=Process.sequential
        )

        result = crew.kickoff()
        self.log("✅ Crew process completed.")
        return result