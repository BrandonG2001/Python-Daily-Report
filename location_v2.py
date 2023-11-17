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
        if rev_geolocate.address == None:
            #ic('My Location Failed to Use Hardware Address')
            raise Exception
        hardware_address = str(rev_geolocate.address)
        ic(hardware_address)
        # a lot more info than what i need but in case i want it
        #house, street, city, county, state, zipcode, country = hardware_address.split(', ')
        country = hardware_address.split(', ')[-1]
        zipcode = hardware_address.split(', ')[-2]
        state = hardware_address.split(', ')[-3]
        county = hardware_address.split(', ')[-4]
        city = hardware_address.split(', ')[-5]
        #street = hardware_address.split(', ')[-6]
        #house = hardware_address.split(f', {street}')[0]
        #print('Using Hardware Location')
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
    my_location(debugging=True)