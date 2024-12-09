# AIAgents: Terms and Conditions Analyzer

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
# Step 1: Clone the Repository
git clone https://github.com/KhajiraCraft/AIAgents.git
cd AIAgents

# Step 2: Set Up Virtual Environment (Optional)
python -m venv venv
# Activate the environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Step 3: Install Dependencies
pip install -r requirements.txt

# Step 4: Start the Flask Server
python app.py
