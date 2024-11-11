# News Summarization Application 📰

A Streamlit web application that fetches recent news articles based on user queries and provides AI-generated summaries using One AI's summarization capabilities. The app helps users stay informed by providing quick access to news with concise summaries.



## Features ✨

- **News Search**: Search for news articles on any topic
- **AI-Powered Summaries**: Get concise summaries of articles using One AI's natural language processing
- **Article Preview**: View full articles with their original images
- **User-Friendly Interface**: Clean and intuitive design built with Streamlit
- **Expandable Content**: Toggle between summary and full article text

## Technologies Used 🛠️

- **Python 3.10+**
- **Streamlit**: For the web interface
- **NewsAPI**: To fetch recent news articles
- **One AI**: For article summarization
- **Newspaper3k**: For article parsing and content extraction

## Installation 💻

1. Clone the repository:
```bash
git clone https://github.com/yourusername/news-summarization-app.git
cd news-summarization-app
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Set up your API keys:
   - Get a NewsAPI key from [NewsAPI.org](https://newsapi.org)
   - Get a One AI API key from [One AI](https://www.oneai.com/)

4. Create a `.env` file in the project root and add your API keys:
```env
NEWS_API_KEY=your_news_api_key_here
ONE_AI_API_KEY=your_one_ai_api_key_here
```

## Usage 🚀

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to `http://localhost:8501`

3. Enter a search term in the text input field

4. Click "Submit" to fetch and summarize news articles

## Requirements 📋

Create a `requirements.txt` file with the following dependencies:
```
streamlit
newsapi-python
newspaper3k
requests
python-dotenv
```

## Project Structure 📁

```
news-summarization-app/
├── app.py              # Main application file
├── .env               # Environment variables (API keys)
├── requirements.txt   # Project dependencies
├── README.md         # Project documentation
└── assets/
    └── logo.jpg      # Application logo
```

## API Documentation 📚

### NewsAPI
- [NewsAPI Documentation](https://newsapi.org/docs)
- Used for fetching news articles
- Free tier includes:
  - 100 requests per day
  - Access to recent articles
  - Multiple news sources

### One AI
- [One AI Documentation](https://studio.oneai.com/docs)
- Used for article summarization
- Features include:
  - Text Summarization
  - Sentiment Analysis
  - Named Entity Recognition
  - Topic Analysis

## Contributing 🤝

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## Acknowledgments 🙏

- [NewsAPI](https://newsapi.org) for providing access to news articles
- [One AI](https://www.oneai.com/) for their powerful text summarization API
- [Streamlit](https://streamlit.io/) for the awesome web framework


---
⭐️ Star this repo if you find it useful!
