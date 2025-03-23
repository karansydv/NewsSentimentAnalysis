from fastapi import FastAPI
from utils import (
    fetch_news, analyze_sentiment, analyze_topic_overlap, 
    summarize_text, translate_to_hindi, text_to_speech_hindi
)

app = FastAPI()

@app.get("/sentiment/")
def get_sentiment(company: str):
    """Fetch news and analyze sentiment"""
    url = f"https://newsapi.org/v2/everything?q={company}&language=en&sortBy=publishedAt&pageSize=5&apiKey=15e3220b23c441bc8f8d58f983c8bb2c"
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": "Failed to fetch news"}

    articles = response.json().get("articles", [])

    news_list = []
    for article in articles:
        summary = article["description"] if article["description"] else "No summary available"
        sentiment = analyze_sentiment(summary)

        news_list.append({
            "title": article["title"],
            "summary": summary,
            "sentiment": sentiment,
            "date": article["publishedAt"][:10],
            "source": article["source"]["name"],
            "url": article["url"]
        })

    # Compute sentiment distribution
    sentiment_distribution = get_sentiment_distribution(news_list)
    
    # Compute topic overlap
    shared_topics, unique_topics = analyze_topic_overlap(news_list)

    article_comparisons = compare_articles(news_list)

    final_analysis = overall_sentiment_analysis(news_list)

    audio_file_path, hindi_summary = convert_summary_to_hindi_tts(final_summary)

    return {
        "news": news_list,
        "sentiment_distribution": sentiment_distribution,
        "shared_topics": list(shared_topics),  # Convert set to list for JSON response
        "unique_topics": {k: list(v) for k, v in unique_topics.items()}, 
        "article_comparisons": article_comparisons,  # Convert sets to lists
        "final_summary": final_analysis["Summary"],
        "hindi_summary": hindi_summary,
        "audio_file": f"/download_audio"
    }

@app.get("/download_audio")
def download_audio():
    """Serve the generated TTS audio file."""
    return {"message": "Audio available at: /summary_audio.mp3"}
