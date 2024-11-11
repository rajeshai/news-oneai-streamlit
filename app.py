import streamlit as st
import json
import requests
from newspaper import Article

st.set_page_config(page_title='Short News App',
    layout = 'wide',
    initial_sidebar_state = 'expanded',
    menu_items={
        'About':'This is a demo application with One AI',
        'Get help':'https://studio.oneai.com/docs',
        'Report a Bug':'https://discord.com/channels/941458663493746698/941458828187287603'
    })

st.title('Short Summary News Application Demo with OneAI')
st.markdown('This application takes an input from the user and displays upto five latest news articles along with their summary. This application uses the free quota api calls.')
st.sidebar.image('logo.jpg')
st.sidebar.title('ONE AI')
st.sidebar.markdown('[One AI](https://www.oneai.com/) is an API-first, language AI service built for developers. Embed your API to analyze, process, and transform text in your project.')
st.sidebar.markdown('''It can perform several tasks like
- Sentiment Analysis
- Named Entity Recognition
- Topic Analysis
- Text Summarization
- Keyword Extraction
There are several more tasks that One AI can do. Please find the below links to explore more about this:''')
st.sidebar.markdown('[About us](https://www.oneai.com/about-us)')
st.sidebar.markdown('[Documentation](https://studio.oneai.com/docs)')
st.sidebar.markdown('[Contact](https://www.oneai.com/contact-us)')
st.sidebar.markdown('[Community](https://discord.com/channels/941458663493746698/942326235722309642)')
st.sidebar.markdown('© 2022 Logo rights reserved to One AI')

def run():
    @st.cache()
    def summary(text1):
        try:
            api_key = "1c93487c-695c-4089-adfc-5e4b7623718c"
            url = "https://api.oneai.com/api/v0/pipeline"
            headers = {'api-key': api_key, 'content-type': 'application/json'}
            payload = {
                'input': text1,
                'input_type': 'article',
                'steps': [{'skill': 'summarize'}]
            }
            r = requests.post(url, json=payload, headers=headers)
            r.raise_for_status()  # Raise an exception for bad status codes
            data = r.json()
            return data['output'][0]['text']
        except requests.exceptions.RequestException as e:
            st.error(f"Error calling One AI API: {str(e)}")
            return None
        except (KeyError, IndexError) as e:
            st.error(f"Error processing One AI response: {str(e)}")
            return None

    def get_links(text2):
        try:
            url = "https://free-news.p.rapidapi.com/v1/search"
            querystring = {
                "q": text2,
                "lang": "en",
                "page": 1,
                "page_size": 5
            }
            headers = {
                'x-rapidapi-host': "free-news.p.rapidapi.com",
                'x-rapidapi-key': "375ffbaab0mshb442ffb69d6f025p117ba0jsn01e8146148e3"
            }
            
            response = requests.request("GET", url, headers=headers, params=querystring)
            response.raise_for_status()  # Raise an exception for bad status codes
            
            # Debug information
            st.debug(f"API Response Status Code: {response.status_code}")
            st.debug(f"API Response Text: {response.text[:500]}...")  # Show first 500 chars
            
            response_dict = response.json()
            if 'articles' not in response_dict:
                st.warning("No articles found in the API response")
                return []
                
            links = [article['link'] for article in response_dict['articles']]
            return links
            
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching news: {str(e)}")
            return []
        except json.JSONDecodeError as e:
            st.error(f"Error parsing API response: {str(e)}")
            return []
        except KeyError as e:
            st.error(f"Unexpected API response format: {str(e)}")
            return []

    input_text = st.text_input('Search your favorite topic:')
    submitted = st.button('Submit')
    
    if submitted and input_text:
        with st.spinner('Fetching news articles...'):
            links = get_links(input_text)
            
            if not links:
                st.warning("No articles found. Please try a different search term.")
                return
                
            for link in links:
                try:
                    with st.spinner(f'Processing article from {link}...'):
                        news_article = Article(link, language='en')
                        news_article.download()
                        news_article.parse()
                        
                        if news_article.top_image:
                            st.image(news_article.top_image)
                        
                        st.header(news_article.title)
                        st.markdown('*Summary of the Article:*')
                        
                        article_summary = summary(news_article.text)
                        if article_summary:
                            st.markdown(article_summary)
                        else:
                            st.warning("Could not generate summary for this article")
                            
                        with st.expander('Full Article'):
                            st.markdown(news_article.text)
                            
                except Exception as e:
                    st.error(f"Error processing article from {link}: {str(e)}")
                    continue
    elif submitted:
        st.warning("Please enter a search term")

if __name__ == '__main__':
    run()
