import webbrowser as web
import sys
from requests.exceptions import RequestException
import logging as log
import httpx
import asyncio

from personal_information import WEBSITES_TO_OPEN

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
                case 200: # 200 = ALL GOOD
                    web.open(url=all_urls[index])
                case 301 | 302:  # 301/302 is old url code -> will be sent to updated url
                    web.open(url=all_urls[index])
                    log.warning(f'Opened {all_urls[index]} but code was {response.status_code} indicating url is/has moved')
                # 403 is = no program code access 
                case 403:
                    web.open(url=all_urls[index])
                    log.warning(f'Opened {all_urls[index]} but code was {response.status_code} indicating code has not access to it')
                # default = Sorry error happened
                case _:
                    log.warning(f'GET Request Failed and returned a {response.status_code} status code for {all_urls[index]}')
        except RequestException as error:
            log.critical(f'HTTP Error occurred, failed to reach URL: {error}')
        except Exception as error:
            log.critical(f'An unexpected error occurred: {error}')
            
         
def open_my_websites() -> None:
    # run different url dicts
    asyncio.run(OpenBrowser(url_dict=WEBSITES_TO_OPEN))


if __name__ == '__main__':
    open_my_websites()
    sys.exit()
    