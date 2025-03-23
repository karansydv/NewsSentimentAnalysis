import streamlit as st
import requests
import subprocess
import time
import matplotlib.pyplot as plt

# Start FastAPI backend in the background
backend_process = subprocess.Popen(["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"])

# Wait for FastAPI to start
time.sleep(3)

st.title("News Sentiment Analyzer 📰📊")

company_name = st.text_input("Enter a company name:", "")

if st.button("Analyze News Sentiment"):
    if company_name:
        # Send a request to FastAPI backend
        response = requests.get(f"http://0.0.0.0:8000/sentiment/?company={company_name}")

        if response.status_code == 200:
            news_data = response.json()
            if "error" in news_data:
                st.error(news_data["error"])
            elif not news_data["news"]:
                st.warning("No news articles found for this company.")
            else:
                st.subheader("News Sentiment Analysis")
                for article in news_data["news"]:
                    st.write(f"**Title:** {article['title']}")
                    st.write(f"**Summary:** {article['summary']}")
                    st.write(f"**Sentiment:** `{article['sentiment']}`")
                    st.write(f"**Date:** {article['date']}")
                    st.write(f"**Source:** {article['source']}")
                    st.markdown(f"[Read more]({article['url']})", unsafe_allow_html=True)
                    st.write("---")

                # Display sentiment distribution
                st.subheader("Sentiment Distribution")

                sentiment_distribution = news_data.get("sentiment_distribution", {})
                labels = list(sentiment_distribution.keys())
                values = list(sentiment_distribution.values())

                fig, ax = plt.subplots()
                ax.bar(labels, values, color=["green", "red", "gray"])
                ax.set_ylabel("Number of Articles")
                ax.set_title("Sentiment Analysis Distribution")

                st.pyplot(fig)

                
                # Display Shared Topics
                st.subheader("Shared Topics Across Articles 📌")
                shared_topics = news_data.get("shared_topics", [])
                if shared_topics:
                    st.write(", ".join(shared_topics))
                else:
                    st.write("No shared topics found.")

                # Display Unique Topics per Article
                st.subheader("Unique Topics Per Article 🔍")
                unique_topics = news_data.get("unique_topics", {})
                if unique_topics:
                    for article, topics in unique_topics.items():
                        st.write(f"**{article}:** {', '.join(topics) if topics else 'No unique topics'}")
                else:
                    st.write("No unique topics found.")

                # ✅ Display Comparative Article Analysis
                st.subheader("Comparative Article Insights 🔍")
                for comparison in news_data["article_comparisons"]:
                    st.write(f"**Comparison:** {comparison['Comparison']}")
                    st.write(f"**Divergences:** {comparison['Divergences']}")
                    st.write(f"**Impact Analysis:** {comparison['Impact']}")
                    st.write("---")

                # ✅ New: Display Overall Summary
                st.subheader("AI-Generated News Summary")
                st.write(news_data["final_summary"])

                # ✅ Display Hindi Translated Summary
                st.subheader("हिन्दी सारांश (Hindi Summary)")
                st.write(news_data["hindi_summary"])

                # ✅ Provide Audio Playback and Download Option
                st.subheader("📢 Listen to Hindi Summary")
                audio_url = f"http://0.0.0.0:8000/download_audio"
                st.audio("summary_audio.mp3", format="audio/mp3")

                st.download_button(label="Download Audio 🎵", data=requests.get(audio_url).content, file_name="summary_audio.mp3", mime="audio/mp3")

        else:
            st.error("Failed to fetch news. Please try again.")
    else:
        st.warning("Please enter a company name.")

# Stop backend when Streamlit exits
import atexit
atexit.register(lambda: backend_process.terminate())
