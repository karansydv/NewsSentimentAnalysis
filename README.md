News Sentiment Analyzer 📰📊
Overview

This project extracts, analyzes, and provides sentiment insights on news articles related to a given company. The application:

    Scrapes at least 10 unique news articles (avoiding JavaScript-based links)
    Conducts sentiment analysis (positive, negative, neutral)
    Performs comparative sentiment analysis across articles
    Converts the summarized content into Hindi speech
    Provides a simple Streamlit-based web interface
    Uses FastAPI for backend API development
    Deploys on Hugging Face Spaces

Features

✔️ News Extraction: Scrapes news articles using BeautifulSoup from non-JS weblinks. ✔️ Sentiment Analysis: Determines whether news articles are positive, negative, or neutral. ✔️ Comparative Analysis: Compares sentiment across multiple articles. ✔️ Text-to-Speech (TTS): Converts summarized news into Hindi speech. ✔️ User-Friendly Web Interface: Built using Streamlit. ✔️ API Development: FastAPI ensures seamless frontend-backend communication. ✔️ Deployment: Hosted on Hugging Face Spaces.
Installation & Setup
Prerequisites

Ensure you have the following installed:

    Python 3.x
    pip (Python package manager)
    Virtual environment (optional but recommended)

Installation Steps

    Clone the repository:

    git clone (https://github.com/karansydv/NewsSentimentAnalysis/)

    Create and activate a virtual environment (optional but recommended):

    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

    Install dependencies:

    pip install -r requirements.txt

    Run the FastAPI backend:

    uvicorn api:app --host 0.0.0.0 --port 8000

    Start the Streamlit frontend:

    streamlit run app.py

Configuration

Ensure that the following dependencies are installed in requirements.txt:

streamlit
fastapi
uvicorn
beautifulsoup4
requests
nltk
transformers
torch
gtts
googletrans==4.0.0-rc1
sentence-transformers
scikit-learn
matplotlib
numpy
pandas

API Configuration:

    The FastAPI backend fetches news from https://newsapi.org/v2/everything.
    Ensure you have a valid NewsAPI API key and replace it in api.py:

    url = f"https://newsapi.org/v2/everything?q={company}&language=en&sortBy=publishedAt&pageSize=10&apiKey=YOUR_API_KEY"

Deployment
Deploy on Hugging Face Spaces

    Ensure all files are in the repository, including app.py, api.py, utils.py, requirements.txt, and Dockerfile (if needed).
    Push the repository to GitHub:

    git add .
    git commit -m "Initial commit"
    git push origin main

    Go to Hugging Face Spaces and create a new Space.
    Select Streamlit as the SDK.
    Connect your GitHub repository.
    Click Deploy and wait for the app to be live.

Usage

    Enter a company name in the search bar.
    Click Analyze News Sentiment.
    View extracted articles, their sentiment analysis, and comparative insights.
    Listen to the Hindi TTS output.

File Structure

📂 Project Folder
├── app.py              # Streamlit frontend
├── api.py              # FastAPI backend
├── utils.py            # Utility functions
├── requirements.txt    # Dependencies
├── Dockerfile          # (Optional) For containerized deployment
├── README.md           # Project documentation

Contribution

Feel free to submit pull requests or open issues to improve the project.
License

This project is licensed under the MIT License.
Contact

For any issues or suggestions, please reach out via GitHub Issues.

🚀 Happy Coding!
