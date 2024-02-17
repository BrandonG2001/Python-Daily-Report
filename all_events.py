from icalevents.icalevents import events
from datetime import datetime, timedelta, timezone
from personal_information import MY_CALENDARS, ALL_DAY_CALENDARS, IMPORTANT_HOLIDAYS
from icecream import ic
from time_period import today


# let the dictionary be in the form
#  {date : [event 1], [event 2], [event 3],
#   date2 : [], []}

# where each event is in the form
# event = [calendar_name, event_name, start_time, end_time]
# or
# event = [all_day_cal_name, all_day_event]

# all times should be formatted as ... %H:%M  -> ex 16:35
# all dates will be formatted as ... %w, %m/%d  -> ex   1, 05/18   -> Monday, May 18
# because icalevents only goes 1 week into future, I can use the %w to signal day of week, but
# i still need the %m/%d to sort it by date or it will sort based on day of week instead of by date

# for all day events (holdidays or birthdays)
    # have check holidays/Birthdays after all sorting,  PREPEND to list



def get_all_events():
    my_tz = datetime.now(timezone.utc).astimezone().tzinfo
    events_info = {}

    
    # my main calendars
    try:
        for calendar_name in MY_CALENDARS:
            event_info_list = None
            es  = events(MY_CALENDARS[calendar_name], fix_apple=('webcal' in MY_CALENDARS[calendar_name]))
            
            # getting all events into the actual dictionary
            for e in es:
                #print(e)
                date_and_time = str(e).split(': ')[0]
                full_name = str(e).split(date_and_time + ': ')[1]
                
                # sometimes apple cal doesnt give timezone
                try:  
                    start_time_datetime = datetime.strptime(date_and_time, "%Y-%m-%d %H:%M:%S%z").astimezone(my_tz)
                except:
                    start_time_datetime = datetime.strptime(date_and_time, "%Y-%m-%d %H:%M:%S").astimezone(my_tz)
                    
                length_1 = full_name.split("(")[-1]            
                name = full_name.split("("+length_1)[0]
                event_length = length_1.split(':00)')[0]
                delta_hr, delta_min = event_length.split(':')
                end_time = start_time_datetime + timedelta(hours=int(delta_hr), minutes=int(delta_min))

                # formatted start and end times
                start_time_formatted = start_time_datetime.time().strftime('%H:%M')
                end_time_formatted = end_time.strftime('%H:%M')
                my_date_formatted = start_time_datetime.date().strftime('%w, %m/%d/%y')

                name = name.strip()

                # specific formatting based on calendar name
                match calendar_name.split():
                    #######################
                    ### Checking Nascar ###
                    #######################
                    case ['Nascar', *_]:
                        name = name.replace('🏁','')
                        name = name.strip()
                        
                        event_info_list = [calendar_name, name, start_time_formatted, end_time_formatted]


                    #########################
                    ### College  Football ###
                    #########################
                    case [*_, 'Football']:
                        # just get the name verses opponent (Special Football Events)
                        name = full_name.split(' - ')[0]
                        
                        # get rid of any length of time in name (calendar makers trying to be helpful)
                        name = name.split('(')[0]
                        # have to do this
                        name = name.replace('University of Texas Football', 't.u.')
                        name = name.replace('Texas A&M University Football', "Texas A&M")
                        name = name.replace('Texas Tech University Football', "Texas Tech")
                        name = name.replace('vs', 'verses')
                        name = name.strip()
                        
                        # team_2_check
                        if (name.split('at')[-1]).strip() == 'Texas':
                            team_1 = name.split('at')[0]
                            name = team_1 + 'at t.u.'
                            
                        elif (name.split('verses')[-1]).strip() == 'Texas':
                            team_1 = name.split('verses')[0]
                            name = team_1 + 'verses t.u.'
                            #pass
                        
                        event_info_list = [calendar_name, name, start_time_formatted, end_time_formatted]

                            
                    ############################
                    ### Checking Formula 1   ###
                    ############################
                    case ['Formula', '1']:
                        name = name.split('F1: ')[-1]
                        event_location = (name.split('(')[1]).split(')')[0]
                        name = name.split('(')[0]
                        name = name.strip()
                        
                        event_info_list = [calendar_name, name, event_location, start_time_formatted, end_time_formatted]
                        
                    ####################
                    ### Default Case ###
                    ####################
                    case _:
                        event_info_list = [calendar_name, name, start_time_formatted, end_time_formatted]


                #############################
                ### Adding Events to Dict ###
                #############################
                if my_date_formatted not in events_info:
                    events_info[my_date_formatted] = [event_info_list]
                else:
                    #last_index = len(events_info[my_date_formatted])
                    events_info[my_date_formatted].append(event_info_list)

        
        
        # check if today is in the list (make sure events are future not past)
        today_key = today.strftime('%w, %m/%d/%y')
        curr_time = datetime.now(tz=my_tz).time()
        for date_key in events_info.keys():
            if datetime.strptime(today_key,'%w, %m/%d/%y').date() > datetime.strptime(date_key,'%w, %m/%d/%y').date():
                #print(date_key)
                del events_info[date_key]
                break
            
        if today_key in events_info.keys():
            todays_events = events_info[today_key]
            items_to_remove = []
            for event in todays_events:
                #print(event)
                event_end_time = datetime.strptime(event[-1],'%H:%M').time()
                #print(event_end_time.strftime('%H:%M'))
                #print('Current time: ',curr_time.strftime('%H:%M'))
                # if the current time is past (greater than) the end time
                if event_end_time < curr_time:
                    #print(event)
                    items_to_remove.append(event)

            for past_event in items_to_remove:
                todays_events.remove(past_event)
            if len(todays_events) == 0:
                del events_info[today_key]
                
        # sort dictionary entries by time
        for date in events_info:
            events_info[date].sort(key=lambda x: datetime.strptime(x[-2], '%H:%M'))
            
        # ugly way to check if two of my tracked football teams are going against each other
        # remove duplicate
        for date in events_info:
            # check for double football 
            for index,event in enumerate(events_info[date]):
                keep_going = True
                #print(event)
                if 'Football' in event[0]:
                    #print('EV1 ',event)
                    football_event = event[1]
                    if 'verses' in football_event:
                        team_1, team_2 = football_event.split('verses', maxsplit=1)
                    else:
                        team_1, team_2 = football_event.split('at', maxsplit=1)
                        
                    team_1 = team_1.strip()
                    team_2= team_2.strip()
                    
                    for other_index,other_football in enumerate(events_info[date]):
                        if 'Football' in other_football[0]:
                            if index != other_index:
                                other_football_event = other_football[1]
                                #print(other_football_event)
                                #print(other_football_event.split('at', maxsplit=1))
                                if 'verses' in other_football_event:
                                    team_1_b, team_2_b = other_football_event.split('verses', maxsplit=1)
                                else:
                                    team_1_b, team_2_b = other_football_event.split('at', maxsplit=1)
                                    
                                team_1_b = team_1_b.strip()
                                team_2_b = team_2_b.strip()
                                
                                if team_1_b in [team_1, team_2]: #or team_1_b in [team_1, team_2]:
                                    events_info[date].remove(other_football)
                                    keep_going = False
                                    break
                if not keep_going:
                    break
        
        ##############################
        ###  All Day Cal Checking  ###
        ##############################
        # GET holidays/Birthdays and PREPEND them to the list
        for all_day_calender in ALL_DAY_CALENDARS:
            event_info_list = None
            all_day_events = events(ALL_DAY_CALENDARS[all_day_calender], fix_apple=False)
            # getting all events into the actual dictionary
            for all_day_event in all_day_events:
                #print(all_day_event)
                date_and_time = str(all_day_event).split(': ')[0]
                full_name = str(all_day_event).split(date_and_time + ': ')[1]
                
                # sometimes apple cal doesnt give timezone
                try:  
                    start_time_datetime = datetime.strptime(date_and_time, "%Y-%m-%d %H:%M:%S%z").astimezone(my_tz)
                except:
                    start_time_datetime = datetime.strptime(date_and_time, "%Y-%m-%d %H:%M:%S").astimezone(my_tz)
                
                #print(full_name)
                event_length = full_name.split('(')[-1]
                name = full_name.split('(' + event_length)[0].strip()
                my_date_formatted = start_time_datetime.date().strftime('%w, %m/%d/%y')
                #print(name)
                
                if 'holidays' not in all_day_calender.lower()  or  (name in IMPORTANT_HOLIDAYS):
                    event_info_list = [all_day_calender, name]
                    
                if event_info_list != None:
                    if my_date_formatted not in events_info:
                            events_info[my_date_formatted] = [event_info_list]
                    else:
                        #last_index = len(events_info[my_date_formatted])
                        events_info[my_date_formatted].insert(0, event_info_list)


        # Getting a sorted list of events by date
        if len(events_info) != 0:
            my_events_unsorted = []
            for key in events_info:
                temp_event = [key]
                for event in events_info[key]:
                    temp_event.append(event)
                my_events_unsorted.append(temp_event)
        
            my_events = sorted(my_events_unsorted, key=lambda x: datetime.strptime(x[0], '%w, %m/%d/%y'), reverse=False)

        return my_events
    except:
        return []


if __name__ == '__main__':
    
    #get_all_events()
    print()
    print(get_all_events())
    
    
