# Real-time Sentiment Analysis Dashboard

## Overview
An interactive web application that performs real-time sentiment analysis using transformer-based NLP models. Built with Streamlit for seamless UI/UX and leveraging Hugging Face's powerful NLP pipelines. This project is a feature that i needed in my sophomore year mini-project, and the input stream will be integrated with our main code and a sentimental score will be generated.

## Tech Stack
- **Frontend**: Streamlit
- **NLP**: Hugging Face Transformers (DistilBERT)
- **Visualization**: Plotly Express
- **Data Processing**: Pandas

## Features
- Real-time text sentiment analysis
- Batch processing capability
- Confidence scoring
- Interactive visualizations
- User-friendly interface

## Installation
```bash
pip install streamlit transformers torch pandas plotly
```

## Usage
```bash
streamlit run app.py
```

## Learning Outcomes
Building this project helped me understand:
- Modern NLP architectures (Transformers)
- Web app development with Streamlit
- Interactive data visualization
- Real-time data processing
- UI/UX design principles

## Technical Deep Dive
### NLP Pipeline
- Utilizes DistilBERT: A lightweight, distilled version of BERT
- Pre-trained on SST-2 dataset for sentiment classification
- Outputs: Positive/Negative sentiment with confidence scores

### UI Components
- Text input area for multiple entries
- Real-time analysis trigger
- Dynamic data display
- Interactive charts

## Author's Note
Even though I did this project as a feature of my sophomore year mini project, As an **AI enthusiast**, this project combines my passion for:
- Natural Language Processing
- Interactive dashboards
- User experience design
- Deep learning applications


## Acknowledgments
- Hugging Face team
- Streamlit community
