import webbrowser as web
import sys
from requests.exceptions import RequestException
import logging as log
import httpx
import asyncio

# function to open webrowser on any dict
async def OpenBrowser(url_dict: dict) -> None:
    schema = 'https://'
    temp_dict = {}
    # Bypass for certain websites that I know will give 403 response
    for url_key in url_dict:
        if url_dict[url_key] == 'chat.openai.com':
            url = schema + 'chat.openai.com'
            web.open(url=url)
        else:
           temp_dict[url_key] = url_dict[url_key]
         
    # get a list of all urls
    all_urls = []
    for url_key in temp_dict:
        base_url = temp_dict[url_key]
        base_url = base_url.strip()
        url = (schema + base_url).strip()
        all_urls.append(url)
        

    # async requests to make it more scalable and faster
    # make sure each website is actually reachable 
    async with httpx.AsyncClient() as client:
        reqs = [client.get(url) for url in all_urls]
        results = await asyncio.gather(*reqs)

    for index, response in enumerate(results):
        try:
            if response.status_code == 200 or (response.status_code==301 or response.status_code==302): # Check if the URL is reachable before browser query 
                web.open(url=all_urls[index])
            else:
                log.warning(f'GET Request Failed (Status Code Not 200) and returned a {response.status_code} status code for {all_urls[index]}')
        except RequestException as error:
            log.critical(f'HTTP Error occurred, failed to reach URL: {error}')
        except Exception as error:
            log.critical(f'An unexpected error occurred: {error}')
            
        
        
def open_my_websites() -> None:
    personal_urls = {
        'Youtube' : 'www.youtube.com',
        'Twitch' :'www.twitch.tv',
        'zlibrary' : 'z-library.se',
        'My G-Drive' : 'drive.google.com/drive/u/0/my-drive',
        'My Gmail' : 'mail.google.com/mail/u/0/#inbox',
        'Github' :'www.github.com/BrandonG2001?tab=repositories',
    }

    work_urls = {
        'ChatGPT' :'chat.openai.com',
        'Google Calendar' : 'calendar.google.com/calendar'
    }


    # run different url dicts
    asyncio.run(OpenBrowser(url_dict=personal_urls))
    asyncio.run(OpenBrowser(url_dict=work_urls))

        
if __name__ == '__main__':
    open_my_websites()
    sys.exit()