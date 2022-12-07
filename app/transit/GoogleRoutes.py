from flask import url_for
import requests

# fileObject = open("KEY.txt", "r") #Gets file that contains the API Key
# data = fileObject.read() #reads API key

# origin = input("Start: ")
# destin = input("Destination: ") #gets user input of origin and destinatiion


# origin = origin.replace(",","")
# destin = destin.replace(",","") #removes commas from the origin and destination
# origin = origin.replace(" ","%2C%20C")
# destin = destin.replace(" ","%2C%20C") #removes spaces and replaces it with formating for the request string

# url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+ origin +"&destinations="+ destin +"&mode=driving&units=imperial&key=" + data #replaces data with API key to run locally, or make a file named KEY.txt with API in it

# payload={}
# headers = {}

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text) ##prints JSON output to command line


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
Driving, walking, and bicycling keys will always be included,
while transit is only included if results are found.
"""
def getRoute(origin, destin):
    key = 'API_KEY'
    payload={}
    headers = {}
    baseUrl = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destin}&units=imperial&key={key}"
    driving = requests.request("GET", baseUrl+'&mode=driving', headers=headers, data=payload)
    walking = requests.request("GET", baseUrl+'&mode=walking', headers=headers, data=payload)
    bicycling = requests.request("GET", baseUrl+'&mode=bicycling', headers=headers, data=payload)
    transit = requests.request("GET", baseUrl+'&mode=transit', headers=headers, data=payload)
    results = {
        'driving': {
            'duration': driving.json()['rows'][0]['elements'][0]['duration']['text'],
            'distance': driving.json()['rows'][0]['elements'][0]['distance']['text'],
            'method': 'Driving'
        },
        'walking': {
            'duration': walking.json()['rows'][0]['elements'][0]['duration']['text'],
            'distance': walking.json()['rows'][0]['elements'][0]['distance']['text'],
            'method': 'Walking'
        },
        'bicycling': {
            'duration': bicycling.json()['rows'][0]['elements'][0]['duration']['text'],
            'distance': bicycling.json()['rows'][0]['elements'][0]['distance']['text'],
            'method': 'Biking'
        }
    }
    if not transit.json()['rows'][0]['elements'][0]['status'] == 'ZERO_RESULTS':
        results['transit'] = {
            'duration': transit.json()['rows'][0]['elements'][0]['duration']['text'],
            'distance': transit.json()['rows'][0]['elements'][0]['distance']['text'],
            'method': 'Transit'
        }
    return results

    #"https://maps.googleapis.com/maps/api/distancematrix/json?origins="+ origin +"&destinations="+ destin +"&mode=driving&units=imperial&key=" + key