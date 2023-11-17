import webbrowser as web
import sys
from requests.exceptions import RequestException
import logging as log
import httpx
import asyncio

# function to open webrowser on any dict
async def OpenBrowser(url_dict: dict) -> None:
    schema = 'https://'
    all_urls = []
    for url_key in url_dict:
        base_url = url_dict[url_key]
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
            # Check if the URL is reachable before browser query
            # switch statement based on the status code
            match response.status_code:
                # 200 = ALL GOOD
                case 200: 
                    web.open(url=all_urls[index])
                # 301 is old url code -> will be sent to updated url
                case 301:  
                    web.open(url=all_urls[index])
                # 302 is temporary version of code 301
                case 302:  
                    web.open(url=all_urls[index])
                # 403 is = no program code access 
                case 403:
                    web.open(url=all_urls[index])
                # default = Sorry error happened
                case _:
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
        'Amazon' : 'www.amazon.com',
        'Reqzone' : 'reqzone.com'
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
    