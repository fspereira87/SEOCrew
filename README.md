# SEOCrew
A SEO analysis and optimization tool built with CrewAI. This project uses multiple AI agents working together to provide comprehensive SEO analysis and recommendations for websites.


## Features

- **Multi-Agent SEO Analysis**: Utilizes specialized AI agents for different aspects of SEO
- **Comprehensive Analysis**: Covers technical SEO, content strategy, link building, and more
- **Streamlit Interface**: User-friendly web interface for easy interaction
- **Secure API Key Management**: Uses Streamlit secrets for secure API key storage

## Project Structure

```
.
├── .venv-filipe/           # Virtual environment
├── agents.py              # Agent definitions
├── tasks.py               # Task definitions
├── main.py               # Main application logic
├── streamlit_app.py      # Streamlit web interface
├── .streamlit/           # Streamlit configuration
│   └── secrets.toml     # API keys and secrets
└── pyproject.toml        # Project dependencies
```

## Agents

The project uses five specialized agents:

1. **SEO Analyst**: Conducts comprehensive SEO audits
2. **Content Strategist**: Analyzes and improves content strategy
3. **Technical SEO Specialist**: Evaluates technical aspects of the website
4. **Link Building Specialist**: Identifies backlink opportunities
5. **SEO Project Manager**: Coordinates and integrates all findings

## Setup

1. **Install Poetry** (if not already installed):
   ```bash
   pip install poetry
   ```

2. **Install Dependencies**:
   ```bash
   poetry install
   ```

3. **Set Up Streamlit Secrets**:
   Create a `.streamlit/secrets.toml` file with the following structure:
   ```toml
   [secrets]
   OPENAI_API_KEY = "your_openai_api_key"
   SERPER_API_KEY = "your_serper_api_key"
   ```

   Note: The `.streamlit/secrets.toml` file should never be committed to version control. Each developer/server should maintain their own secrets file.

4. **Activate Virtual Environment**:
   ```bash
   poetry env activate
   ```

## Usage

### Command Line Interface

Run the application from the command line:
```bash
python main.py
```

### Web Interface

Launch the Streamlit web interface:
```bash
streamlit run streamlit_app.py
```

## Security Notes

- API keys are stored securely in Streamlit secrets
- Each environment (development, staging, production) should have its own secrets file
- Never commit the secrets.toml file to version control
- For production deployment, use the Streamlit Cloud secrets management interface

## Dependencies

- crewai
- langchain-openai
- python-dotenv
- crewai-tools
- streamlit
- pyyaml
- setuptools

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- CrewAI for the multi-agent framework
- OpenAI for the language models
- Serper for search capabilities
- Streamlit for the web interface and secrets management
- Hector Pineda (YT: @Hector.levelup) for the fantastic videos and structure for this project
