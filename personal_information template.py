# rename file to 'personal_information.py'

############
### APIs ###
############
#openweathermap
OPEN_WEATHER_MAP_API_KEY = ''
TOMORROW_IO_API_KEY = ''

weather_sources = ['openweathermap', 'Tommorow.io']
WEATHER_SOURCE = weather_sources[0]

#newsapi.org
NEWS_API_KEY = ''
# use get sources from news.py to get sources you want
NEWS_SOURCES = [ 

                ]

TECH_SOURCES = [

                ]

BUSINESS_SOURCES = [

                    ]

INTERSTING_SOURCES = NEWS_SOURCES + TECH_SOURCES + BUSINESS_SOURCES


#youtube
YOUTUBE_API_KEY = ''

# Define a dictionary of playlists to monitor (playlist name: playlist ID)
YOUTUBE_PLAYLISTS = {
      # playlist name: playlist ID
      # Add more playlists as needed
}

# Define a dictionary of channels to monitor (channel name: channel ID)
YOUTUBE_CHANNELS = {
    # 'Channel': 'CHANNEL_ID'
    # Add more channels as needed
}

# Twitch
# use Twitch_auth_getter to get access token
# otherwise, this sucks trying to get
TWITCH_SECRET_TOKEN = '' # use  https://dev.twitch.tv/console/apps to get secret and client id
TWITCH_CLIENT_ID = ''

# Lists of Twitch usernames I want to check (priority streamers at beginning of list)
# I do it this way b/c i dont wanna just catch the tail end
#    of my fav streamer
MORNING_STREAMERS = [
                        # streamer name
                    ]

AFTERNOON_STREAMERS = [
                        # streamer name
                    ]

EVENING_STREAMERS =[
                        # streamer name
                    ]

LATE_NIGHT_STREAMERS = [
                        # streamer name
                        ]


ALL_STREAMERS = {     
                'Morning' : MORNING_STREAMERS,
                'Afternoon' : AFTERNOON_STREAMERS,
                'Evening' : EVENING_STREAMERS,
                'Late-Night' : LATE_NIGHT_STREAMERS
                }


#################
### CALENDARS ###
#################
# edit as you see fit
# icloud cals will generally start with    webcal://
# other cals (google calendar) generally start with    https://
MY_CALENDARS = {
                'icloud Home' : '',
                'icloud Work' : '',
                'icloud School Work' : '',
                
                'Nascar Cup Series' : '',
                'Nascar Xfinity Series' : '',
                'Nascar Truck Series' : '',
                
                'Formula 1' : '',
                
                "Texas A&M Football" : '',
                "Texas Tech Football" : '',
                'tu Football' : '',
                }


ALL_DAY_CALENDARS = {
                    'US HOLIDAYS' : '',
                    'Birthdays' : ''
                    }


# these are the only holidays I really care about
IMPORTANT_HOLIDAYS = [
                      'Christmas','Halloween', 'Thanksgiving', 'Christmas Eve', "New Year's Day", "New Year's Eve",
                      'Martin Luther King Jr. Day', "Valentine's Day", 'Easter Sunday', 'Tax Day', "Mother's Day", 
                      "Memorial Day", "Cinco de Mayo", "Father's Day", "Independence Day", "Flag Day", "Labor Day"
                      ]