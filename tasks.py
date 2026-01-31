from crewai import Task


class SEOCrewTasks:

    def seo_analyses_task(self, agent, website_url):
        return Task(
            agent=agent,
            description=(
                f"Conduct a comprehensive SEO audit of the website {website_url}. "
                "Analyze keyword usage, meta tags, site structure, backlinks, and content quality. "
                "Use available tools where appropriate to gather factual insights."
            ),
            expected_output=(
                "A comprehensive SEO audit report detailing current performance metrics "
                "(crawlability, indexing issues, PageSpeed indicators), a prioritized list of SEO issues, "
                "benchmarks, and actionable recommendations."
            ),
            config={}
        )

    def technical_seo_task(self, agent, website_url, seo_audit_task):
        return Task(
            agent=agent,
            depends_on=[seo_audit_task],
            description=(
                f"Based on the SEO audit findings, evaluate the technical SEO aspects of {website_url}, "
                "including site architecture, performance, mobile usability, URL structure, "
                "internal linking, and structured data."
            ),
            expected_output=(
                "A technical SEO audit report with performance metrics, "
                "a prioritized list of technical issues, and step-by-step fixes."
            ),
            config={}
        )

    def content_specialist_task(self, agent, website_url, seo_audit_task):
        return Task(
            agent=agent,
            depends_on=[seo_audit_task],
            description=(
                f"Using insights from the SEO audit, analyze the content of {website_url}. "
                "Identify content gaps, keyword opportunities, and competitive weaknesses. "
                "Propose content topics, formats, and optimization strategies aligned with search intent."
            ),
            expected_output=(
                "A detailed content strategy including content gap analysis, "
                "high-potential long-tail keywords, competitive comparisons, "
                "and recommendations for content updates and new initiatives."
            ),
            config={}
        )

    def link_building_task(self, agent, website_url, seo_audit_task):
        return Task(
            agent=agent,
            depends_on=[seo_audit_task],
            description=(
                f"Using findings from the SEO audit, identify backlink opportunities for {website_url}. "
                "Analyze competitors, industry publications, and authoritative domains "
                "to design an effective link acquisition strategy."
            ),
            expected_output=(
                "A link building strategy outlining high-authority backlink opportunities, "
                "recommended outreach tactics, and KPIs for measuring link quality and success."
            ),
            config={}
        )

    def seo_manager_task(
        self,
        agent,
        website_url,
        seo_audit_task,
        technical_task,
        content_task,
        link_task
    ):
        return Task(
            agent=agent,
            depends_on=[
                seo_audit_task,
                technical_task,
                content_task,
                link_task
            ],
            description=(
                f"Aggregate and synthesize all SEO findings for {website_url}. "
                "Produce a unified, executive-level SEO strategy and improvement roadmap."
            ),
            expected_output=(
                "A comprehensive SEO strategy document with an executive summary, "
                "integrated insights from all analyses, a prioritized action roadmap, "
                "defined KPIs, and implementation timelines."
            ),
            config={}
        )
