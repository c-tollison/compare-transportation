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