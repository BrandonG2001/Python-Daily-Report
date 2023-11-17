#import requests
from requests import get
from personal_information import OPEN_WEATHER_MAP_API_KEY
from personal_information import TOMORROW_IO_API_KEY 
from personal_information import WEATHER_SOURCE
from icecream import ic
from location_v2 import my_location
from time_period import tomorow


Weather_codes = {
      "0": "Unknown",
      "1000": "Clear, Sunny",
      "1100": "Mostly Clear",
      "1101": "Partly Cloudy",
      "1102": "Mostly Cloudy",
      "1001": "Cloudy",
      "2000": "Fog",
      "2100": "Light Fog",
      "4000": "Drizzle",
      "4001": "Rain",
      "4200": "Light Rain",
      "4201": "Heavy Rain",
      "5000": "Snow",
      "5001": "Flurries",
      "5100": "Light Snow",
      "5101": "Heavy Snow",
      "6000": "Freezing Drizzle",
      "6001": "Freezing Rain",
      "6200": "Light Freezing Rain",
      "6201": "Heavy Freezing Rain",
      "7000": "Ice Pellets",
      "7101": "Heavy Ice Pellets",
      "7102": "Light Ice Pellets",
      "8000": "Thunderstorm"
    }




def fetch_curr_weather(my_loc):
    """
    :param my_loc: dict with keys -> city, state, country, latitude, longitude 
    :return: weather
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    units_format= '&units=imperial'
    coords = f'lat={my_loc["latitude"]}&lon={my_loc["longitude"]}'
    complete_url = base_url + coords + "&appid=" + OPEN_WEATHER_MAP_API_KEY + units_format

    response = get(complete_url)

    city_weather_data = response.json()
    #print(city_weather_data)

    if city_weather_data["cod"] != "404":
        #print(f'weather data from city_weather_data {city_weather_data}')
        main_data = city_weather_data["main"]
        #print(main_data)
        #ic(main_data)
        #ic(city_weather_data)
        feels_like = main_data['feels_like']
        weather_description = city_weather_data["weather"][0]['description']
        # weather_description = weather_description_data["description"]
        current_temperature = main_data["temp"]
        # current_pressure = main_data["pressure"]
        current_humidity = main_data["humidity"]
        wind_data = city_weather_data["wind"]
        wind_speed = wind_data["speed"]
        if round(current_temperature) != round(feels_like):
            final_response = f"""
   The weather in {my_loc['city']} is currently {weather_description}. 
   It is currently {round(current_temperature)}°F, but it feels like {round(feels_like)}."""
            
        else:
            final_response = f"""
   The weather in {my_loc['city']} is currently {weather_description}. 
   It is currently {round(current_temperature)}°F, with a {round(current_humidity)}% humidity and {round(wind_speed)} mph winds."""
        return final_response

    else:
        return "Sorry Sir, I couldn't find the city in my database. Please try again"
    

def fetch_forecast_weather(my_loc):
    tomorrow_str = tomorow.strftime('%Y-%m-%d')
    # Define the OpenWeatherMap API URL
    complete_url = f'https://api.openweathermap.org/data/2.5/forecast?lat={my_loc["latitude"]}&lon={my_loc["longitude"]}&appid={OPEN_WEATHER_MAP_API_KEY}&units=imperial'

    # Send an HTTP GET request to the API
    response = get(complete_url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Find the forecast for tomorrow
        min_temps = []
        max_temps = []
        found_data = False
        
        for forecast in data['list']:
            if forecast['dt_txt'].split()[0] == tomorrow_str:
                found_data = True
                main_data = forecast["main"] 
                weather_description_data = forecast["weather"][0]
                weather_description = weather_description_data["description"]
                #tom_temperature = main_data["temp"]
                wind_data = forecast["wind"]
                tom_wind = wind_data["speed"]
                max_temps.append(main_data['temp_max'])
                min_temps.append(main_data['temp_min'])
                final_response = f"""
   The weather in {my_loc['city']} will be {weather_description} 
   with a high of {round(max(max_temps))}°F, and a low of {round(min(min_temps))},"""
        if found_data == False:
            final_response = f'No data found for {my_loc["city"]} on {tomorrow_str}.'
    else:
        print(f'Error {response.status_code}: Unable to fetch data')
        final_response = f'No data found for {my_loc["city"]} on {tomorrow_str}.'

    return final_response



def fetch_forecast_weather_v2(my_loc):
    url = f'https://api.tomorrow.io/v4/weather/forecast?location={my_loc["latitude"]},{my_loc["longitude"]}&units=imperial&apikey={TOMORROW_IO_API_KEY}'
    response = get(url)
    if response.status_code == 200:
        #print(response.text)
        data = response.json()
        data = data['timelines']
        data = data['daily']
        data = data[1]
        date = data['time']
        data = data['values']
        temp_max = data['temperatureMax']
        temp_min = data['temperatureMin']
        humidity = data['humidityAvg']
        weather_code_1 = data['weatherCodeMax']
        weather_code_2 = data['weatherCodeMin']
        weather_descr_1 = Weather_codes[str(int(weather_code_1))]
        weather_descr_2 = Weather_codes[str(int(weather_code_2))]
        if weather_descr_1 != weather_descr_2:
            weather_descr = weather_descr_1 + ' ' + weather_descr_2
        else:
            weather_descr = weather_descr_1
            
        final_response = f"""
   The weather in {my_loc['city']} will be {weather_descr} 
   with a high of {round(temp_max)}°F, and a low of {round(temp_min)},"""
        """print()
        print('DATE : ', date)
        print('Max Temp : ',temp_max)
        print('Min Temp : ',temp_min)
        print('Humidity : ',humidity)
        print('Weather Code 1 : ',weather_code_1)
        print('Weather Code 2 : ',weather_code_2)
        print()
        print(data.keys())"""
        return final_response
    
    elif response.status_code == 403:
        return 'API Key Not Valid'
    else:
        return 'SOMETHING WENT WRONG WITH TOMMOROW.io'


def fetch_curr_weather_v2(my_loc): 
    url = f'https://api.tomorrow.io/v4/weather/realtime?location={my_loc["latitude"]},{my_loc["longitude"]}&units=imperial&apikey={TOMORROW_IO_API_KEY}'
    response = get(url)
    if response.status_code == 200:
        #print(response.text)
        data = response.json()
        data = data['data']
        date = data['time']
        data = data['values']
        
        curr_temp = data['temperature']
        humidity = data['humidity']
        feels_like = data['temperatureApparent']
        windspeed = data['windSpeed']
        code = data['weatherCode']
        
        #print(windspeed)

        if int(windspeed) > 5:
            windspeed_str =  f' and {round(windspeed)} mph winds.'
        else:
            windspeed_str =  '.'
        #print()
        #print('DATE : ', date)
        #print('Curr Temp : ',curr_temp)
        #print('Feels Like Temp : ',feels_like)
        #print('Weather Code 1 : ',Weather_codes[str(int(code))])
        #print('Weather Code 2 : ',weather_code_2)
        #print()
        #print(data.keys())
        
        if round(curr_temp) != round(feels_like):
                    final_response = f"""
    The weather in {my_loc['city']} is currently {Weather_codes[str(int(code))]}. 
    It is currently {round(curr_temp)}°F, but it feels like {round(feels_like)}."""
                    
        else:
            final_response = f"""
    The weather in {my_loc['city']} is currently {Weather_codes[str(int(code))]}. 
    It is currently {round(curr_temp)}°F, with a {round(humidity)}% humidity{windspeed_str}"""
    
        return final_response
    
    elif response.status_code == 429:
        return 'API Limit Reached for Tommorow.io'
    elif response.status_code == 403:
        return 'API Key Not Valid'
    else:
        return 'SOMETHING WENT WRONG WITH TOMMOROW.io'


def get_all_weather(source=WEATHER_SOURCE):
    my_loc = my_location()
    if source == 'openweathermap':
        curr_wether = fetch_curr_weather(my_loc)
        tom_weather = fetch_forecast_weather(my_loc)
    elif source == 'Tommorow.io':    
        curr_wether = fetch_curr_weather_v2(my_loc)
        tom_weather = fetch_forecast_weather_v2(my_loc)
    return_dict = {'Current Weather' : curr_wether,
                "Tomorrow's Weather" : tom_weather
                }
    return return_dict




if __name__ == '__main__':    
    print(get_all_weather())
    