import urllib.request
import json
from .models import News, Sources

# getting api key

api_key = None

# getting the news base url

base_url = None


def configure_request(app):
    global api_key, base_url
    api_key = app.config["NEWS_API_KEY"]
    base_url = app.config["NEWS_API_BASE_URL"]


def get_news():
    '''
    Function that gets json response to our url request
    '''

    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response["sources"]:
            news_results_list = get_news_response["sources"]
            news_results = process_sources(news_results_list)

    return news_results

def search_news(topic):
    '''
    Function to search for news by topic
    '''
    
    search_news_url = "https://newsapi.org/v2/everything?q={}&apiKey={}".format(topic, api_key)
    
    with urllib.request.urlopen(search_news_url) as url :
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)
        
        search_news_results = None
        if search_news_response["articles"]:
            search_news_list = search_news_response["articles"]
            search_news_results = process_results(search_news_list)
    
    return search_news_results

def sources_news():
    '''
    Function to search news sources
    '''
    sources_url = "https:/newsapi.org/v2/sources?apiKey{}".format(api_key)
    
    with urllib.request.urlopen(sources_url) as url:
        search_sources_data = url.read()
        search_sources_response = json.loads(search_sources_data)
        
        search_sources_results = None
        if search_sources_response["sources"]:
            search_sources_list = search_sources_response["sources"]
            search_sources_results = process_sources(search_sources_list)
    
    return search_sources_results
    

def process_results(news_list):
    '''
    Function that processes the news result and transform them to a list of Objects
    Args:
        news_list: A list of dictionaries that contain movie details
    Returns:
        news_results: A list of news objects
    '''

    news_results = []
    
    for news_item in news_list:
        author = news_item.get("author")
        title = news_item.get("title")
        description = news_item.get("description")
        url = news_item.get("url")
        urlToImage = news_item.get("urlToImage")
        content = news_item.get("content")
        
        if urlToImage:
            news_object = News(author, title, description, url, urlToImage, content)
            news_results.append(news_object)
    
    return news_results

def process_sources(sources_list):
    '''
    
    '''
    sources_results = []
    
    for sources_item in sources_list:
        id = sources_item.get("id")
        name = sources_item.get("name")
        description = sources_item.get("description")
        url = sources_item.get("url")
        category = sources_item.get("category")
        
        if url:
            sources_object = Sources(id, name, description, url, category)
            sources_results.append(sources_object)
    
    return sources_results
