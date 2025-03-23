import requests
from bs4 import BeautifulSoup
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter
import nltk
from transformers import pipeline
from googletrans import Translator
from gtts import gTTS

# Download necessary resources
nltk.download("vader_lexicon")
nltk.download("stopwords")

# Initialize utilities
sia = SentimentIntensityAnalyzer()
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
translator = Translator()

### 1️⃣ Extract News Articles
def fetch_news(company):
    """Scrape and return news articles for a given company."""
    url = f"https://newsapi.org/v2/everything?q={company}&language=en&pageSize=10&apiKey=YOUR_API_KEY"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Failed to fetch news"}
    
    articles = response.json().get("articles", [])
    return articles

### 2️⃣ Perform Sentiment Analysis
def analyze_sentiment(text):
    """Analyze sentiment (Positive, Neutral, Negative) using VADER."""
    if not text:
        return "Neutral"
    
    score = sia.polarity_scores(text)["compound"]
    return "Positive" if score > 0.05 else "Negative" if score < -0.05 else "Neutral"

### 3️⃣ Compare Topic Overlap
def analyze_topic_overlap(news_articles):
    """Identify shared and unique topics across all articles."""
    stop_words = set(nltk.corpus.stopwords.words("english"))
    all_words = []
    article_topics = {}

    for idx, article in enumerate(news_articles):
        words = set(article["summary"].lower().split()) - stop_words
        all_words.extend(words)
        article_topics[f"Article {idx + 1}"] = words

    shared_topics = {word for word, count in Counter(all_words).items() if count > 1}
    unique_topics_per_article = {k: v - shared_topics for k, v in article_topics.items()}

    return shared_topics, unique_topics_per_article

### 4️⃣ Summarize News Articles
def summarize_text(text):
    """Summarize text using a transformer-based model."""
    return summarizer(text, max_length=150, min_length=50, do_sample=False)[0]["summary_text"]

### 5️⃣ Translate Summary to Hindi
def translate_to_hindi(summary_text):
    """Translate English text to Hindi."""
    translated_text = translator.translate(summary_text, src="en", dest="hi").text
    return translated_text

### 6️⃣ Convert Hindi Summary to Speech
def text_to_speech_hindi(text):
    """Convert Hindi text to speech and save as MP3."""
    tts = gTTS(text=text, lang="hi")
    audio_path = "summary_audio.mp3"
    tts.save(audio_path)
    return audio_path
