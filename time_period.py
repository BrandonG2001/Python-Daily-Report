from datetime import datetime, timedelta, timezone
#import pytz

# Set the US Central Timezone
# Get the current time in the US Central Timezone
today = datetime.now(timezone.utc).astimezone()
tomorow = today + timedelta(days=1)

# Define time periods
morning_period = (datetime.strptime('04:00:00', '%H:%M:%S').time(), datetime.strptime('13:00:00', '%H:%M:%S').time())  # 4am-1pm
afternoon_period = (datetime.strptime('13:00:00', '%H:%M:%S').time(), datetime.strptime('18:00:00', '%H:%M:%S').time()) #1pm -6pm
evening_period = (datetime.strptime('18:00:00', '%H:%M:%S').time(), datetime.strptime('22:00:00', '%H:%M:%S').time()) # 6pm -10pm
#late_night_period = (datetime.strptime('22:00:00', '%H:%M:%S').time(), datetime.strptime('04:00:00', '%H:%M:%S').time()) #10pm-4am

# Function to check the time period
def get_time_period():
    current_time = today.time()
    if morning_period[0] <= current_time <= morning_period[1]:
        return 'Morning'
    elif afternoon_period[0] <= current_time <= afternoon_period[1]:
        return 'Afternoon'
    elif evening_period[0] <= current_time <= evening_period[1]:
        return 'Evening'
    else:
        return 'Late-Night'
    

days_of_wk = {
              '0' : 'Sunday',
              '1' : 'Monday',
              '2' : 'Tuesday',
              '3' : 'Wednesday',
              '4' : 'Thursday',
              '5' : 'Friday',
              '6' : 'Saturday',
              }

if __name__ == '__main__':
    pass
    #print(today.strftime("%d/%m/%Y, %H:%M:%S"))