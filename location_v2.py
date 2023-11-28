from winsdk.windows.devices.geolocation import Geolocator, GeolocationAccessStatus  # pip install winsdk
from asyncio import run as async_run
from httpx import get as req_get
from geopy.geocoders import Nominatim
from icecream import ic


async def get_hw_coords():
        locator = Geolocator()
        access_status = await locator.request_access_async()
        if access_status != GeolocationAccessStatus.ALLOWED:
            raise Exception
        pos = await locator.get_geoposition_async()      
        return [pos.coordinate.latitude, pos.coordinate.longitude]
    
def get_hardware_loc():
    return async_run(get_hw_coords())


def my_location(debugging=False): 
    if debugging:
        ic.enable()
    else:
        ic.disable()

    # try to get hw coords first
    try:
        latitude, longitude = get_hardware_loc()
        geolocator = Nominatim(user_agent="PythonDailyReport")
        rev_geolocate = geolocator.reverse((latitude, longitude))
        #ic(rev_geolocate.raw)
        if rev_geolocate.address == None:
            #ic('My Location Failed to Use Hardware Address')
            raise Exception
        location_dict = rev_geolocate.raw['address']
        #ic(location_dict)
        if 'city' in location_dict.keys():
            city = location_dict['city']
        else:
            city = location_dict['county']
            
        #zipcode = location_dict['postcode']
        state = location_dict['state']
        country = location_dict['country']
    # use ip address location
    except:
        ip_add = req_get('https://api.ipify.org').text
        url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
        geo_requests = req_get(url)
        geo_data = geo_requests.json()
        city = geo_data['city']
        state = geo_data['region']
        country = geo_data['country']
        latitude = geo_data['latitude']
        longitude = geo_data['longitude']
        #print('Using IP Address Location')

    return {'city' : city,
            'state': state,
            'country': country,
            'latitude': latitude,
            'longitude': longitude
            }

if __name__ == '__main__':
    print(my_location(debugging=True))