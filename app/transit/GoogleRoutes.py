import requests

"""
Inputs are both address strings and the response is a dictionary formatted as follows:
{
    'driving': {
        'duration': '___ min'
        'distance': '___ miles'
        'method': 'Driving'
    }
    ...
}
Driving, walking, and biking keys will always be included
while transit is only included if results are found.
"""
def getRoutes(origin, destin):
    key = 'API_KEY' #API_KEY
    baseUrl = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=' #base endpoint url
    
    results = {} #dictionary to be returned
    travel_methods = ['driving', 'walking', 'transit', 'bicycling'] #traveling methods
    
    for travel_method in travel_methods: #loop through available travel methods
        url = f"{baseUrl}{origin}&destinations={destin}&mode={travel_method}&units=imperial&key={key}" #Formatted request url
        
        payload={}
        headers = {}

        response = requests.get(url, headers=headers, data=payload).json()
        if not response['rows'][0]['elements'][0]['status'] == "ZERO_RESULTS": #check for valid distance
            results[travel_method] = {
                'duration': response['rows'][0]['elements'][0]['duration']['text'], #travel time
                'distance': response['rows'][0]['elements'][0]['distance']['text'], #distance
                'method': travel_method.title() #title case travel method
            }
    return results