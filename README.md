# AIAgents: Terms and Conditions Analyzer

# Members
Christopher Khajira
Esther Ochieng

## Overview

AIAgents is a web-based application designed to simplify and enhance the process of analyzing Terms and Conditions (T&Cs) documents. The application scrapes T&Cs from a given website, summarizes key points, identifies risks, and provides actionable recommendations, all in an intuitive and user-friendly manner. It uses Flask as the backend framework and integrates with AI models for analysis.

---

## Features

1. **Scrape Terms and Conditions**:
   - Extracts T&Cs from any website URL.
   - Handles dynamic content and limits extraction to 2000 tokens for efficient processing.

2. **Summarize Content**:
   - AI-powered summarization of lengthy and complex legal documents.
   - Categorizes text into different topics for better understanding.

3. **Risk Analysis**:
   - Identifies red flags, such as privacy concerns and auto-renewal clauses.
   - Classifies risks into high, medium, or low categories.

4. **Generate Recommendations**:
   - Provides actionable suggestions tailored to the identified risks.
   - Ensures recommendations are concise and specific.

---

## Installation and Usage

### Prerequisites
- Python 3.8 or higher
- Pip package manager

### Steps to Set Up and Run the Application
```bash
```
## Step 1: Clone the Repository
git clone https://github.com/KhajiraCraft/AIAgents.git
cd AIAgents

## Step 2: Set Up Virtual Environment (Optional)
python -m venv venv
## Activate the environment
### On Windows:
venv\Scripts\activate
### On macOS/Linux:
source venv/bin/activate

## Step 3: Install Dependencies
pip install -r requirements.txt

## Step 4: Start the Flask Server
python app.py

## Example Request
### Endpoint: http://127.0.0.1:5000/analyze
### Method: POST
### Body (JSON):
{
  "url": "https://example.com/terms"
}

## Directory Structure
AIAgents/
├── backend/
│   ├── app.py                # Main Flask application
│   ├── chains/
│   │   ├── custom_chains.py  # Custom chains for AI tasks
│   │   └── ...
│   └── requirements.txt      # Dependencies
├── chrome_extension/
│   └── ...                   # Code for Chrome extension (if applicable)
├── venv/                     # Virtual environment (optional)
├── README.md                 # Project documentation

## Technology Stack
- Backend: Flask
- AI Tools: LangChain, OpenAI GPT
- Web Scraping: BeautifulSoup, Requests
- LLM Models: ChatOpenai

## Contributing
1. Fork the repository.

2. Create a feature branch:
git checkout -b feature-name

3. Commit your changes:
git commit -m "Add feature-name"

4. Push to the branch:
git push origin feature-name

5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- OpenAI for their powerful AI tools.
- Flask for providing a lightweight web framework.
- LangChain for simplifying AI workflows.
- All contributors who made this project possible.
```

