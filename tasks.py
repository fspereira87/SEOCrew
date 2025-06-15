from crewai import Task

class SEOCrewTaks:
    
    def seo_analyses_task(self, agent, inputs):
        return Task(
            agent = agent,
            description = f"Conduct a comprehensive SEO audit of the all website {inputs} covering keyword usage, meta tags, site structure, backlinks, and content quality.",
            expected_output = f"A comprehensive SEO audit report that details current performance metrics (including PageSpeed scores, crawl errors, etc.), a prioritized list of issues, industry-specific benchmarks, and actionable recommendations tailored to the website’s niche."
        )
    
    def content_specialist_task(self, agent, context, inputs):
        return Task(
            agent = agent,
            description = f"Based on the seo analyst agent report, and after analyzing {inputs} website content alongside competitor material, then propose topic ideas, formats, and keyword-focused improvements.",
            expected_output = f"A detailed content strategy document that includes a content gap analysis, a shortlist of targeted long-tail keywords and phrases, competitive content comparisons, and specific recommendations for content updates and new topic ideas aligned with the website’s target audience."
        )
        
    def technical_seo_task(self, agent, inputs):
        return Task(
            agent = agent,
            description = f"Evaluate the {inputs} website's architecture, loading speed, mobile responsiveness, URL structure, and schema markup.",
            expected_output = f"A technical SEO audit report featuring specific metrics (e.g., mobile performance scores, load times, structured data validation results), a prioritized list of technical issues, and detailed, step-by-step recommendations for addressing each issue."
        )
        
    def link_building_task(self, agent, inputs):
        return Task(
            agent = agent,
            description = f"Identify potential backlink opportunities, manage outreach campaigns, and monitor the quality of incoming links of the {inputs} website and taking into consideration other agents' output.",
            expected_output = f"A targeted link building strategy report that identifies industry-specific high-authority websites (backed by competitor analysis), provides a detailed outreach plan (including tactics such as guest blogging and expert roundups), and outlines key performance indicators for tracking link quality and success."
        )
        
    def seo_manager_task(self, agent, context, inputs):
        return Task(
            agent = agent,
            description = f"Gather and integrate outputs from all SEO team members, including analyses, audits, and strategic recommendations. Compile these into a structured, comprehensive report that provides a holistic view of the website's SEO performance and outlines a clear roadmap for improvement.",
            expected_output = f"A unified, comprehensive SEO strategy document that integrates detailed findings and recommendations from all disciplines (technical, content, link building, UX/UI, and data analysis). It should feature an executive summary, industry-specific benchmarks, a prioritized roadmap with clear KPIs and timelines, and actionable steps for enhancing the website’s overall SEO performance."
        )
        
    
        
