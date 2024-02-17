from news import get_news, remove_double_occurrences, INTERSTING_SOURCES
from weather import get_all_weather
from python_speech import print_and_speak, speak, set_ai_voice
from random_quotes import get_random_quote
from rocket_launches import get_space_launches
from stardate_stuff import StarDate 
from execute_command import run_updates, clean_windows_temp_files
from video_service_checker import is_anyone_live, watch_user, youtube_checker_v2
from multiprocessing.pool import ThreadPool
from random import choice
from webbrowser import open as open_browser

from all_events import get_all_events
from time_period import today, tomorow, days_of_wk
from datetime import datetime, timedelta

from icecream import ic
from warnings import filterwarnings
filterwarnings("ignore", category=UserWarning)


# returns dict with keys = Calendar, Weather, News, Space Launches
def fast_thread_func(checking_calendar, checking_weather, checking_news, checking_space_launches):
    return_dict = {}
    if checking_calendar:
        return_dict['Calendar'] = get_all_events()
    if checking_weather:
        return_dict['Weather'] = get_all_weather()
    if checking_news:
        return_dict['News'] = get_news()
    if checking_space_launches:
        return_dict['Space Launches'] = get_space_launches()
    return return_dict

# returns dict with keys = Youtube, Twitch
def video_thread_func():
    return_dict = {}
    twitch_result = is_anyone_live()
    yt_result = youtube_checker_v2()
    return_dict['Twitch'] = twitch_result
    return_dict['Youtube'] = yt_result
    return return_dict


### Running Variables
def main_report(Full_run=False, get_stardate=True, give_random_quote=False, checking_calendar=True,
                checking_weather=True, checking_news=True, checking_space_launches=True, checking_vids=False,
                clean_windows=False, debugging=False) -> bool:
    
    if debugging:
        ic.enable()
    else:
        ic.disable()

    # start updating apps in background
    if Full_run:
        update_pool = ThreadPool(processes=1)     
        update_pool.apply_async(run_updates, ())

    ######################
    ### MULTITHREADING ###   -> get info from internet before it is needed in main function
    ######################
    if checking_vids:
        vid_pool = ThreadPool(processes=1)
        vid_thread = vid_pool.apply_async(video_thread_func, ())

    # fast thread
    pool_2 = ThreadPool(processes=1)
    fast_thread = pool_2.apply_async(fast_thread_func, (checking_calendar, checking_weather, checking_news, checking_space_launches))

    ###########################
    ###   Today's Stardate  ###
    ########################### 
    if get_stardate == True:
        set_ai_voice('George')
        today_stardate = StarDate().getStardate()
        # getting it to speak the number as a bunch of numbers instead of 1 big number in the tens of thousands
        stardate_number_to_speak = ''
        for number in str(today_stardate):
            if number == '.':
                stardate_number_to_speak = stardate_number_to_speak + ' point'
            elif number == '0':
                stardate_number_to_speak = stardate_number_to_speak + ' o'
            else:
                stardate_number_to_speak = stardate_number_to_speak + " " + number
        print(f"Stardate : {today_stardate}")
        speak(f"Stardate - {stardate_number_to_speak}...", speed=120)
        print()


    ########################
    ###   Today's Quote  ###
    ########################
    if give_random_quote:
        set_ai_voice('Susan')
        #quote_type = 'bible'
        quote_type = choice(['inspirational', 'philosophical', 'bible'])
        if quote_type == 'bible':
            print_and_speak(f"Today's bible quote of the day is ...", speed=120)
        random_quote = get_random_quote(quote_type)
        print(random_quote[0])
        speak(random_quote[1], speed=138)
        print()


    ## fast thread cashing out
    fast_thread.wait()
    fast_thread_dict = fast_thread.get()

    ###########################
    ###  Calendar Checking  ###
    ###########################     Includes (Nascar, F1, Football, Personal, Holidays)
    if checking_calendar:
        all_my_events = fast_thread_dict['Calendar']
        print_and_speak('Checking your upcoming calendar events...', speed=140)
        if len(all_my_events) != 0:
            for i in range(len(all_my_events)):
                day_index = all_my_events[i][0][0]
                day_of_the_week = days_of_wk[day_index]
                event_date = all_my_events[i][0][3:]
                # event_date = event_date + "/" + today.strftime("%y")
                if not (today.date() > datetime.strptime(event_date, "%m/%d/%y").date()):
                    if today.strftime('%w, %m/%d/%y') == all_my_events[i][0]:
                        on_date = 'Today,'
                    elif tomorow.strftime('%w, %m/%d/%y') == all_my_events[i][0]:
                        on_date = 'Tomorrow,'
                    else:
                        on_date = 'On ' + day_of_the_week + ','
                    print_and_speak(on_date)
                    for k in range(1, len(all_my_events[i])):
                        calendar_name = all_my_events[i][k][0]
                        if 'Nascar' in calendar_name:
                            series = all_my_events[i][k][0]
                            title = all_my_events[i][k][1]
                            #start = all_my_events[i][k][2]
                            start = datetime.strptime(all_my_events[i][k][2],'%H:%M').time()
                            start_time = start.strftime('%I:%M %p')
                            if start_time[0] == '0':
                                start_time = start_time[1:]
                            if start_time[-2:] == 'AM':
                                start_time = start_time[:-2] + 'A.M.'
                            elif start_time[-2:] == 'PM':
                                start_time = start_time[:-2] + 'P.M.'
                            #end = all_my_events[i][k][3]

                            # because pyttsx3 cant pronounce xfinity correctly (its really bad)
                            if 'Xfinity' in series:
                                print(f'   {series} - {title} starting at {start_time}')
                                speak(f'   Nascar X-finidy Series - {title} starting at {start_time}', speed=140)
                                pass
                            else:
                                print_and_speak(f'   {series} - {title} starting at {start_time}', speed=140)

                        elif calendar_name == 'Formula 1':
                            event_type = all_my_events[i][k][1]
                            event = all_my_events[i][k][2]
                            #start = all_my_events[i][k][3]
                            start = datetime.strptime(all_my_events[i][k][3],'%H:%M')
                            start_time = start.time().strftime('%I:%M %p')
                            if start_time[0] == '0':
                                start_time = start_time[1:]
                            #end = f1_events[i][k][4]
                            # this is for the main race (ex   Monaco Grand Prix)
                            if event_type in event:
                                print(f'   Formula 1 {event} starting at {start_time}')
                                start_time_hour, start_time_end = start_time.split(':')
                                if '00' in start_time_end:
                                    start_time_end = start_time_end[-3:]
                                speak(f'   Formula 1 {event} starting at {start_time_hour} {start_time_end}', speed=140)
                            # this is for Qualifying, Sprints, etc
                            else:
                                start_time_hour, start_time_end = start_time.split(':')
                                if '00' in start_time_end:
                                    start_time_end = start_time_end[-3:]
                                print(f'   Formula 1 {event_type} for {event} starting at {start_time}')
                                speak(f'   Formula 1 {event_type} for {event} starting at {start_time_hour} {start_time_end}', speed=140)

                        elif 'football' in calendar_name.lower():
                            title = all_my_events[i][k][1]
                            #start = all_my_events[i][k][2]
                            #end = all_my_events[i][k][3]

                            start = datetime.strptime(all_my_events[i][k][2],'%H:%M').time()
                            start_time = start.strftime('%I:%M %p')
                            end = datetime.strptime(all_my_events[i][k][3],'%H:%M').time()
                            end_time = end.strftime('%I:%M %p')

                            if start_time[0] == '0':
                                start_time = start_time[1:]
                            if end_time[0] == '0':
                                end_time = end_time[1:]
                            # in same am/pm time
                            if start_time[-3:] == end_time[-3:]:
                                print_and_speak(f'   {title} from {start_time[:-3]} to {end_time}', speed=140)
                            else:
                                print_and_speak(f'   {title} from {start_time} to {end_time}', speed=140)
                                
                        elif "holidays" not in calendar_name.lower() and calendar_name != 'Birthdays':
                            title = all_my_events[i][k][1]
                            #start = all_my_events[i][k][2]
                            #end = all_my_events[i][k][3]

                            start = datetime.strptime(all_my_events[i][k][2],'%H:%M').time()
                            start_time = start.strftime('%I:%M %p')
                            end = datetime.strptime(all_my_events[i][k][3],'%H:%M').time()
                            end_time = end.strftime('%I:%M %p')

                            if start_time[0] == '0':
                                start_time = start_time[1:]
                            if end_time[0] == '0':
                                end_time = end_time[1:]
                            # in same am/pm time
                            if start_time[-3:] == end_time[-3:]:
                                print_and_speak(f'   {title} from {start_time[:-3]} to {end_time}', speed=140)
                            else:
                                print_and_speak(f'   {title} from {start_time} to {end_time}', speed=140)
                            
                        elif calendar_name == 'Birthdays':
                            title = all_my_events[i][k][1]
                            print_and_speak(f'   {title}. Do NOT forget to call or text.', speed=140)
                        
                        elif calendar_name == 'Holidays':
                            title = all_my_events[i][k][1]
                            print_and_speak(f'   {title}', speed=140)
                            
                        else:
                            title = all_my_events[i][k][1]
                            print_and_speak(f'   {title}', speed=140)
                            
                    print()
        else:
            print_and_speak('Your Calendar is clear for the upcoming week.')

        
    #################
    ###  WEATHER  ###
    #################
    if checking_weather:
        set_ai_voice('Susan')
        #print_and_speak("Checking the local weather...", speed=142)

        all_weather = fast_thread_dict['Weather']

        ## morning or afternoon -> current weather
        current_hour = int(today.strftime('%H'))
        if current_hour < (12 + 4):
            weather_report = all_weather['Current Weather']
            print_and_speak("Today's weather report:", speed=140)
            print_and_speak(weather_report, speed=145)
            print()
        
        # afternoon, evening or after midnight -> tomorow weather
        if current_hour > (12 + 2):
            weather_report = all_weather["Tomorrow's Weather"]
            print_and_speak(f"The weather report for tomorrow:", speed=140)
            print_and_speak(weather_report, speed=140)
            print()

        
    ##############
    ###  NEWS  ###
    ##############
    if checking_news: 
        set_ai_voice('David')
        print_and_speak("Checking the news...")
        news_res = fast_thread_dict['News']
        max_headlines = 7
        num_headlines = 0
        for index, articles in enumerate(news_res):
            if any(source in articles['source']['name'] for source in INTERSTING_SOURCES):  # just getting articles from/mentioning my interesting_srcs
                article = articles['title']
                url = articles['url']
                if num_headlines == 0: # if there is any headlines
                    print_and_speak('Todays Headlines are...', speed=130)
                article = remove_double_occurrences(article, INTERSTING_SOURCES)
                print_and_speak('   ' + article, speed=130)
                print('\t',url)
                if index == len(news_res)-1:
                    break
                num_headlines += 1
                if num_headlines >= max_headlines:
                    break
        
        # if no headlines (very unlikely)
        if num_headlines == 0:
            print_and_speak('There are no headlines today...', speed=135)
        print()
    

    #####################
    ### SPACE LAUNCES ###
    #####################
    if checking_space_launches:
        set_ai_voice('Mark')
        #print_and_speak("Checking The Next Space Launches...")
        launches = fast_thread_dict['Space Launches']
        if len(launches) != 0:
            if len(launches) == 1:
                print_and_speak(f"There is 1 space launch coming up in the U.S.")
            else:
                print_and_speak(f"There are {len(launches)} space launches coming up in the U.S.")

            curr_time = datetime.now()
            time_difference_minutes = 20

            for launch in launches:        
                launch_time = datetime.strptime(launch[2],"%m/%d/%Y, %H:%M")        
                time_before = launch_time - timedelta(minutes=time_difference_minutes)
                time_after = launch_time + timedelta(minutes=time_difference_minutes)
                if  time_before <= curr_time <= time_after: 
                    open_browser(url=launch[1], new=1)  # open the livestream link
                print_and_speak(launch[0])    # speech portion
                print()


    ########################
    ###  Youtube/Twitch  ###
    ########################
    if checking_vids:
        vid_thread.wait()
        video_dict = vid_thread.get()
        #################
        ###  Youtube  ###
        #################
        youtube_videos = video_dict['Youtube']

        # did an error occur (# of API Calls  -> throws an HTTPError)
    
        num_videos = len(youtube_videos) - 1 #accounting for ERROR CODE

        if num_videos > 0:
            first_video = True
            for video_title in youtube_videos:
                #where_vid_from = youtube_videos[video_title][0]  # either 'Playlist'   or   'Channel'
                #playlist_or_channel_name = youtube_videos[video_title][1]
                if video_title != 'ERROR':
                    vid_url = youtube_videos[video_title][2]

                    if first_video:
                        # Open the first video in a new window
                        open_browser(url=vid_url, new=1)
                        first_video = False
                    else:
                        # Open subsequent videos in the same tab (without starting new audio)
                        open_browser(url=vid_url, new=2, autoraise=False)

        elif youtube_videos['ERROR'] != 'HTTP ERROR':
            print_and_speak('There are no youtube videos', speed=140)
        
        if youtube_videos['ERROR'] == 'HTTP ERROR':
            print_and_speak('You have reached the API limit for YOUTUBE.', speed=138)

        ####################
        ###  Twitch.tv   ###
        ####################
        twitch_streamer = video_dict['Twitch']
        if twitch_streamer != None:
            watch_user(twitch_streamer)
        else:
            print_and_speak('No Twitch Streamers Live from your list', speed=140)
    
    #########################
    ###  CLEANUP WINDOWS  ###
    #########################
    # if cleanup day (cannot be threaded or it deletes important temp file for calendar checking)
    # also, if running exe file, this makes calendar fail if exe is not restarted 

    if clean_windows:
        print_and_speak('Cleaning the System...')
        clean_windows_temp_files()
        print_and_speak("This has been your Daily Report for Today.", speed=140)
        return False # returning False will exit the app


    print_and_speak("This has been your Daily Report for Today.", speed=140)
    print()
    return True
    #input("Press Enter to Exit")

if __name__ == '__main__':
    main_report()

