import os
from decouple import config
from crewai import Crew, Process
from textwrap import dedent
from agents import SEOCrewAgents
from tasks import SEOCrewTaks


class SEOCrew:
    def __init__(self, inputs, log_callback=None):
        self.inputs = inputs
        self.agents = SEOCrewAgents()
        self.tasks = SEOCrewTaks()
        self.log_callback = log_callback or (lambda x: None)  # default to no-op

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
        analyst_task = self.tasks.seo_analyses_task(seo_analyst, self.inputs)
        content_task = self.tasks.content_specialist_task(content, [analyst_task.output], self.inputs)
        technical_task = self.tasks.technical_seo_task(technical, self.inputs)
        link_building_task = self.tasks.link_building_task(link_builder, self.inputs)
        manager_task = self.tasks.seo_manager_task(
            manager,
            [analyst_task.output, content_task.output, technical_task.output, link_building_task.output],
            self.inputs
        )

        self.log("🚀 Kicking off Crew...")
        crew = Crew(
            agents=[seo_analyst, content, technical, link_builder, manager],
            tasks=[analyst_task, content_task, technical_task, link_building_task, manager_task],
            process=Process.sequential
        )

        result = crew.kickoff()
        self.log("✅ Crew process completed.")
        return result


# CLI entry point
# if __name__ == "__main__":
#     print("👋 Welcome to the SEO Crew CLI")
#     print("-------------------------------")
#     topic = input("Enter the website to be analysed: ")
    
#     seo_crew = SEOCrew(topic)
#     result = seo_crew.run()

#     print("\n📊 SEO Crew Results:")
#     print("-------------------------------")
#     print(result)