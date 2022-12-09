import requests

token = 'pk.eyJ1IjoibmF0aGFuY294c29uIiwiYSI6ImNsYmU2cXZ5bzA4aDEzb3A2bHpxYWUyamIifQ.58NhtDAZyuYiPpkk633pEw'

"""
Makes API requeset to mapbox reverse geocoding using the given latitude and longitude,
and returns the first address result as a string.
"""
def reverseGeocode(lat, lng):
    response = requests.request('GET', 
        f'https://api.mapbox.com/geocoding/v5/mapbox.places/{lng},{lat}.json?access_token={token}',
        headers={},
        data={})
    return response.json()['features'][0]['place_name']

"""
Returns a dictionary of the form:
{
    'lat': ...,
    'lng': ...
}
Where lat and lng are the coordinates of the address provided
"""
def geocode(addr):
    response = requests.request('GET', 
        f'https://api.mapbox.com/geocoding/v5/mapbox.places/{addr}.json?access_token={token}',
        headers={},
        data={}).json()
    result = {
        'lng': response['features'][0]['center'][0],
        'lat': response['features'][0]['center'][1]
    }
    return result