from httpx import get as req_get
from datetime import datetime, timedelta
from icecream import ic

def get_space_launches(us_only=True):
    launch_information = []
    base_url = 'https://fdo.rocketlaunch.live/json/launches/next/5'
    response = req_get(base_url)
    data = response.json()
    results = data['result']

    if results is None:
        launch_information.append(["No Scheduled Launches Found","No Livestream"])
        return launch_information

    for result in results:
        t0_full = result['t0']
        if t0_full != None:
            livestream_url = "https:" + str(result['quicktext']).split('https:')[1]
            livestream_url = livestream_url.split(" ")[0]
            # start to parse launch time
            t0_test = t0_full.split("Z")[0]
            t0_test = t0_test.replace("T", " ")
            launch_datetime = datetime.strptime(t0_test, "%Y-%m-%d %H:%M") - timedelta(hours=5)

            launch_time = launch_datetime.strftime("%m/%d/%Y, %H:%M")

            if  result['pad']['location']['statename'] == None:
                location = f"{result['pad']['location']['name']}, {result['pad']['location']['country']}"
            
            else:
                location = f"{result['pad']['location']['name']}, {result['pad']['location']['statename']}"


            descr = result['launch_description']
            day_of_wk = launch_datetime.strftime("%A")
            month_desc = launch_datetime.strftime("%B")
            day_str = launch_datetime.strftime("%d")
            descr_formatted = descr.split(' on ')[0] + ' on ' + day_of_wk + ", " + month_desc + " " + day_str + ' at ' + str(int(launch_datetime.strftime('%I'))) + launch_datetime.strftime(':%M %p')

            
            launch_speech = (
    f"""{result['name']}:
   {descr_formatted}
   Location : {location}""")
            #print(launch_speech)
            if us_only:
                if 'United States' in result['pad']['location']['country']:
                    launch_information.append([launch_speech, livestream_url, launch_time])
            else:
                launch_information.append([launch_speech, livestream_url, launch_time])

    return launch_information
