
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

def getRoute(origin, destin):
    payload={}
    headers = {}
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+ origin +"&destinations="+ destin +"&mode=driving&units=imperial&key=" + "data"
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text