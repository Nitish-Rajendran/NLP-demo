import streamlit as st
import pandas as pd
from transformers import pipeline
import plotly.express as px

def create_sentiment_analyzer():
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiments(texts, analyzer):
    results = []
    for text in texts:
        result = analyzer(text)[0]
        results.append({
            'text': text,
            'sentiment': result['label'],
            'confidence': result['score']*100})
    return pd.DataFrame(results)

st.title("Real-time Sentiment Analysis Dashboard")
analyzer = create_sentiment_analyzer()
text_input = st.text_area("Enter text (one per line):", height=200)
if st.button("Analyze"):
    if text_input:
        texts = text_input.split('\n')
        texts = [t.strip() for t in texts if t.strip()]
        results_df = analyze_sentiments(texts, analyzer)
        st.subheader("Analysis Results")
        st.dataframe(results_df)
        fig = px.bar(results_df, 
                    x='sentiment', 
                    title="Sentiment Distribution",
                    color='confidence')
        st.plotly_chart(fig)
