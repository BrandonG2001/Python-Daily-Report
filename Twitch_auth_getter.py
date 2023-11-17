from asyncio import run
from twitchAPI.twitch import Twitch
from icecream import ic

from personal_information import TWITCH_CLIENT_ID, TWITCH_SECRET_TOKEN



##
## IMPORTANT: set at least one link in dev portal to be  http://localhost:17563
##
async def get_access_token(client_id = TWITCH_CLIENT_ID, secret_token = TWITCH_SECRET_TOKEN):
    twitch = await Twitch(client_id, secret_token)
    
    user_token = twitch.get_app_token()

    return user_token

if __name__ == '__main__':
    # run this to get client tokens
    ic(run(get_access_token(client_id=TWITCH_CLIENT_ID, secret_token=TWITCH_SECRET_TOKEN)))