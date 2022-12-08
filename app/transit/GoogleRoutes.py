
import requests
#import os.path

travel_methods = ['driving','walking','transit'] #traveling methods
fileObject = open("KEY.txt", "r") #Gets file that contains the API Key
data = fileObject.read() #reads API key

origin = input("Start: ")
destin = input("Destination: ") #gets user input of origin and destinatiion

destin = destin.strip() #Removes leading and trailing spaces to prevent formatting issues
origin = origin.strip()

origin = origin.replace(",","")
destin = destin.replace(",","") #removes commas from the origin and destination
origin = origin.replace(" ","%2C%20C")
destin = destin.replace(" ","%2C%20C") #removes spaces and replaces it with formating for the request string

for index in range(len(travel_methods) ):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+ origin +"&destinations="+ destin +"&mode=" + travel_methods[index] +"&units=imperial&key=" + data #replaces data with API key to run locally, or make a file named KEY.txt with API in it

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload) #get API response

    getter = response.json() 
    if(getter['rows'][0]['elements'][0]['status'] == "ZERO_RESULTS"):#check for valid distance
        print("Zero results to travel by " + travel_methods[index])
    else:
        if(index == 0): #only places destination and origin once
            print(getter['destination_addresses'][0])
            print(getter['origin_addresses'][0])
            print("\n")

        print(travel_methods[index])#form of travel this distance is for
        print(getter['rows'][0]['elements'][0]['distance']['text'])#distance
        print(getter['rows'][0]['elements'][0]['duration']['text'])#travel time
    print("\n")