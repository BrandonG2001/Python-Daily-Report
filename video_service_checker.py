from googleapiclient.discovery import build # pip install google-api-python-client
from webbrowser import open as web_open
from time_period import get_time_period
from datetime import timezone, datetime
from httpx import get as req_get
from asyncio import run

from personal_information import TWITCH_CLIENT_ID, YOUTUBE_API_KEY
from personal_information import YOUTUBE_CHANNELS as channel_ids, YOUTUBE_PLAYLISTS as playlists, ALL_STREAMERS as all_streamers
from Twitch_auth_getter import get_access_token

from icecream import ic


# Set up the YouTube Data API
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)


# Get all videos from a playlist
def get_all_videos_from_playlist(playlist_id):
    videos = []
    next_page_token = None
    i = 1
    
    while True:
        
        response = youtube.playlistItems().list(
            playlistId=playlist_id,
            maxResults=100,  # Adjust as needed
            part='snippet',
            pageToken=next_page_token
        ).execute()
        #print(f"For Playlist {playlist_id}, {i} request")
        videos.extend(response['items'])
        
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break
        i = i + 1
    return videos

# Get all videos from a channel
def get_all_videos_from_channel(channel_id):
    videos = []
    next_page_token = None
    i = 1
    
    while True:
        response = youtube.search().list(
            channelId=channel_id,
            order='date',
            maxResults=50,  # Adjust as needed
            part='snippet',  # Add 'snippet' part here
            pageToken=next_page_token
        ).execute()
        #print(f"For Channel {channel_id} - {i} requests")
        
        videos.extend(response['items'])
        
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break
        i = i + 1
    return videos

# Sort videos by published date
def sort_videos_by_date(videos):
    return sorted(videos, key=lambda x: x['snippet']['publishedAt'], reverse=True)


def is_video_released_today(published_at, my_tz=datetime.now(timezone.utc).astimezone().tzinfo):
    utc_published_at = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%SZ')
    #local_timezone = pytz.timezone('US/Central')  # Replace with your local time zone
    local_published_at = utc_published_at.replace(tzinfo=timezone.utc).astimezone(my_tz)
    
    today = datetime.now(tz=my_tz).date()
    
    return local_published_at.date() == today

# Main function to check for new video releases
def youtube_checker_v2():
    return_dict = {}
    my_loc_tz = datetime.now(timezone.utc).astimezone().tzinfo
    try:
        #look through playlists
        for playlist_name, playlist_id in playlists.items():
            videos = get_all_videos_from_playlist(playlist_id)
            sorted_videos = sort_videos_by_date(videos)
            
            for video in sorted_videos:
                published_at = video['snippet']['publishedAt']
                is_private = video['snippet']['title'] == 'Private video' #video['snippet']['status']['privacyStatus'] == 'private'
                is_deleted = video['snippet']['title'] == 'Deleted video'
                # print(video['snippet'])
                if (is_video_released_today(published_at, my_tz=my_loc_tz) and not is_private and not is_deleted):
                    video_title = video['snippet']['title']
                    video_url = f"https://www.youtube.com/watch?v={video['snippet']['resourceId']['videoId']}"

                    return_dict[video_title] = ['Playlist', playlist_name, video_url]

        #look through channels
        for channel_name, channel_id in channel_ids.items():
            videos = get_all_videos_from_channel(channel_id)
            sorted_videos = sort_videos_by_date(videos)
            
            for video in sorted_videos:
                published_at = video['snippet']['publishedAt']
                is_private = video['snippet']['title'] == 'Private video'
                is_deleted = video['snippet']['title'] == 'Deleted video'
                if is_video_released_today(published_at, my_tz=my_loc_tz) and not is_private and not is_deleted:
                    video_title = video['snippet']['title']
                    video_url = f"https://www.youtube.com/watch?v={video['id']['videoId']}"
                    

                    return_dict[video_title] = ['Channel', channel_name, video_url]
                    
                    break  # Break after finding the first new video

        return_dict['ERROR'] = 'None...YAY'
        return return_dict
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        #print(message)
        
        return_dict['ERROR'] = 'HTTP Error'
        return return_dict


#############################################
#########      TWITCH     ###################
#############################################
# Check if a user is live on Twitch
def is_user_live(username, twitch_client_id, twitch_access_token):
    url = f"https://api.twitch.tv/helix/streams?user_login={username}"
    headers = {
        "Client-ID": twitch_client_id,
        "Authorization": f"Bearer {twitch_access_token}"
    }
    response = req_get(url, headers=headers)
    data = response.json()
    #print(data)
    #print(data)
    try:
        return len(data["data"]) > 0
    except:
        return False

# Open a web browser and watch a live stream
def watch_user(username):
    url = f"https://www.twitch.tv/{username}"
    web_open(url, new=1)


def is_anyone_live():
    twitch_access_token = run(get_access_token())
    list_of_users = all_streamers[get_time_period()]
    for username in list_of_users:
        if is_user_live(username, TWITCH_CLIENT_ID, twitch_access_token):
            return username
    return None


if __name__ =='__main__':
    debugging = False
    if debugging:
        http_error = 'None...YAY'
        num_runs = 0
        print('Checking youtube api\n')
        while http_error == 'None...YAY':
            print(f'Run: {num_runs + 1}')
            yt_dict = youtube_checker_v2()
            http_error = yt_dict['ERROR']
            print(f'Response Length w/o error key : {len(yt_dict)-1}')
            if http_error == 'None...YAY':
                num_runs += 1
                
        print(f'Completed {num_runs} full runs of the youtube checker')
    
    live_twitch_user = is_anyone_live()
    if live_twitch_user:
        print(f'Twitch Streamer {live_twitch_user} is Live Right Now...')
        
        
