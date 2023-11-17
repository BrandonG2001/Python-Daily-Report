from httpx import get as req_get
from json import loads as json_loads
from icecream import ic

from personal_information import NEWS_API_KEY, INTERSTING_SOURCES


def get_news():
    my_url = ('https://newsapi.org/v2/top-headlines?'                   
                     'country=us&' #we chose the country we want
                     'language=en&' #we chose the language we want
                     'pageSize=100&' #no. of results. Default 20, max 100
                     'apiKey=' + NEWS_API_KEY) # Your Api key
    news = req_get(my_url).text
    news_dict = json_loads(news)
    articles = news_dict['articles']
    #print(articles.keys())
    try:
        return articles
    except:
        return False
    
    
def get_sources():
    my_url = ('https://newsapi.org/v2/top-headlines/sources?country=us&language=en&apiKey=' + NEWS_API_KEY)
    sources = req_get(my_url).text
    sources_dict = json_loads(sources)
    all_sources = sources_dict['sources']
    for source in all_sources:
        if source['name'] not in INTERSTING_SOURCES:
            print(f"Source : {source['name']}")
            print(f'Categ  : {source["category"]}')
            print(f"Descr  : {source['description']}")
            print('')

# sometimes The Washington Post occures twice in article headline
# this gets rid of double occurances
def remove_double_occurrences(main_string, sub_string_list):
    for sub_string in sub_string_list:
        sub_string = '- ' + sub_string
        if main_string.count(sub_string) > 1:
            last_index = main_string.rfind(sub_string)
            if last_index != -1:
                result = main_string[:last_index] + main_string[last_index + len(sub_string):]
                return result
    return main_string



if __name__ == '__main__':
    news_res = get_news()
    for index, articles in enumerate(news_res):
        print(articles.keys())
        print(articles['title'])
        print(articles['description'])
        break
    
    get_sources()