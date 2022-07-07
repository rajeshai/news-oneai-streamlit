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
st.sidebar.markdown('[One AI](https://www.oneai.com/) is an API-first, language AI service built for developers. Embed our API to analyze, process, and transform text in your project.')

st.sidebar.markdown('[About us](https://www.oneai.com/about-us)')
st.sidebar.markdown('[Documentation](https://studio.oneai.com/docs)')
st.sidebar.markdown('[Contact](https://www.oneai.com/contact-us)')
st.sidebar.markdown('[Community](https://discord.com/channels/941458663493746698/942326235722309642)')
st.sidebar.markdown('© 2022 logo rights reserved to One AI')



def run():
    #@st.cache()
    #def summary(text1):
        #oneai.api_key = '1c93487c-695c-4089-adfc-5e4b7623718c'
        #pipeline = oneai.Pipeline(steps=[oneai.skills.Summarize()])
        #my_text = text1
        #output = pipeline.run(my_text)
        #return output.text
    
    @st.cache()
    def summary(text1):
        api_key = "1c93487c-695c-4089-adfc-5e4b7623718c"
        url = "https://api.oneai.com/api/v0/pipeline"
        text = text1
        headers = {
  "api-key": api_key, 
  "content-type": "application/json"
}
        payload = {
  "input": text,
  "input_type": "article",
  "steps": [
        {
          "skill": "summarize",
          "params": {
            "max_length": 100,
					"auto_length": True,
					"find_origins": True,
					"min_length": 5
          }
        }
    ]
}
        r = requests.post(url, json=payload, headers=headers)
        data = r.json()
        return data['output'][0]['text']

    @st.cache()
    def get_links(text1):
        url = "https://free-news.p.rapidapi.com/v1/search"
        querystring = {"q":text1,"lang":"en", "page":1, "page_size":5}
        headers = {'x-rapidapi-host': "free-news.p.rapidapi.com",'x-rapidapi-key': "375ffbaab0mshb442ffb69d6f025p117ba0jsn01e8146148e3"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        response_dict = json.loads(response.text)
        links = [response_dict['articles'][i]['link'] for i in range(len(response_dict['articles']))]
        return links
    
    input_text = st.text_input('Search your favorite topic:')
    submitted = st.button('Submit')
    
    if submitted:
        links = get_links(input_text)
        for link in links:
            try:
                news_article = Article(link, language='en')
                news_article.download()
                news_article.parse()
                st.image(news_article.top_image)
                st.header(news_article.title)
                st.markdown(summary(news_article.text))
                with st.expander('Full Article'):
                    st.markdown(news_article.text)
            except:
                print('No Results!! Please try with new search!!')
if __name__ == '__main__':
    run()