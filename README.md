SEOCrew

SEOCrew is a multi-agent SEO analysis and optimization tool built with CrewAI.
It uses a team of specialized AI agents, each equipped with custom tools, to collaboratively analyze websites and produce a comprehensive SEO strategy.

The project includes a Streamlit web interface, an agent-level tooling layer for search and web scraping, and a task dependency graph to ensure structured execution.

Features

Multi-agent SEO analysis using specialized agents for different SEO domains.

Agent-level tooling with web search and website scraping capabilities.

Task dependency graph implemented using CrewAI depends_on for deterministic execution and automatic context sharing.

Comprehensive SEO coverage including audits, content strategy, technical SEO, link building, and executive reporting.

Streamlit web interface with live execution logs and final results.

Secure API key management using environment variables and Streamlit secrets.

Agent Team

The project uses five specialized agents:

SEO Analyst
Conducts comprehensive SEO audits using search and scraping tools.

Content Strategist
Analyzes content quality, identifies gaps, and proposes keyword-driven improvements.

Technical SEO Specialist
Evaluates site architecture, performance, mobile readiness, and technical SEO issues.

Link Building Specialist
Identifies backlink opportunities and authority-building strategies.

SEO Project Manager
Aggregates all findings into a unified, actionable SEO roadmap.

Tools Layer

SEOCrew includes a dedicated tools layer that is attached directly to agents in agents.py.

The available tools are:

DuckDuckGoSearchTool (tools/search.py)
Used by agents to perform real-time search queries for competitive analysis, keyword research, and SERP insights.

ScrapeWebsiteTool (tools/web_scraper.py)
Used by agents to scrape website content and structure, enabling analysis of page content, headings, metadata, and on-page SEO signals.

Tools are registered on agents and invoked autonomously during task execution. Tasks themselves do not call tools directly.

Project Structure
.
├── agents.py               # Agent definitions and tool assignment
├── tasks.py                # Task definitions with depends_on
├── main.py                 # Crew orchestration logic
├── streamlit_app.py        # Streamlit web interface
├── tools/
│   ├── search.py           # DuckDuckGo search tool
│   └── web_scraper.py      # Website scraping tool
├── .streamlit/
│   └── secrets.toml        # API keys (not committed)
├── pyproject.toml          # Project dependencies
└── README.md

Setup

Install Poetry if it is not already installed:

pip install poetry


Install project dependencies:

poetry install


Set up API keys.

For local development, create a .env file in the project root:

OPENAI_API_KEY=your_openai_api_key


For Streamlit Cloud or production use, create .streamlit/secrets.toml:

OPENAI_API_KEY = "your_openai_api_key"


The secrets file must never be committed to version control.

Activate the virtual environment:

poetry env activate

Usage

To launch the Streamlit web interface:

streamlit run streamlit_app.py


Enter a website URL, run the analysis, follow the live execution logs, and review the final SEO report.

For programmatic or CLI usage:

python main.py


This is useful for debugging, automation, or extending the project.

Execution Flow

The SEO Analyst performs the initial audit.

Technical SEO, Content Strategy, and Link Building tasks run after the audit based on task dependencies.

The SEO Project Manager runs last and synthesizes all findings into a single strategy document.

All context is passed automatically via task dependencies. No manual output or context plumbing is required.

Security Notes

API keys are loaded via environment variables or Streamlit secrets.

No credentials are hardcoded in the codebase.

Each environment should manage its own secrets.

For production deployment, Streamlit Cloud secrets management is recommended.

Dependencies

crewai
crewai-tools
langchain-openai
streamlit
python-dotenv
pyyaml
setuptools

Contributing

Fork the repository.

Create a feature branch.

Commit your changes.

Push to the branch.

Open a Pull Request.

Acknowledgments

CrewAI for the multi-agent orchestration framework.

OpenAI for the language models.

DuckDuckGo for search data.

Streamlit for the web interface and secrets management.

Hector Pineda (YouTube: @Hector.levelup) for inspiration and project structure.
