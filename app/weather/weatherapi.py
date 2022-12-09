import http.client
import requests
from app.geocoding.geocoding import geocode

key = '387c49fc493dd57cb8ec17126798e9ff'

def getWeather(addr):
    coords = geocode(addr)
    # headers = {
    #     'X-RapidAPI-Key': "6890be5119msh9ed3c155319ec9fp1b664cjsn3cc16cb3bf3a",
    #     'X-RapidAPI-Host': "weatherbit-v1-mashape.p.rapidapi.com"
    # }
    baseUrl = 'https://api.openweathermap.org'
    conn = http.client.HTTPSConnection("api.openweathermap.org")
    conn.request("GET", f"/data/2.5/weather?lat={34.7717118}&lon={-82.5062394}&appid={key}", headers={})
    # res = conn.getresponse()
    # data = res.read()
    response = requests.get(f"{baseUrl}/data/2.5/weather?lat={coords['lat']}&lon={coords['lng']}&appid={key}", headers={}, data={}).json()
    response['main']['temp'] = response['main']['temp'] - 273
    response['main']['temp'] = round((response['main']['temp'] * (9/5)) + 32)
    return response


#################################################
"""
Example Response
{
  "coord": {
    "lon": 10.99,
    "lat": 44.34
  },
  "weather": [
    {
      "id": 501,
      "main": "Rain",
      "description": "moderate rain",
      "icon": "10d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 298.48,
    "feels_like": 298.74,
    "temp_min": 297.56,
    "temp_max": 300.05,
    "pressure": 1015,
    "humidity": 64,
    "sea_level": 1015,
    "grnd_level": 933
  },
  "visibility": 10000,
  "wind": {
    "speed": 0.62,
    "deg": 349,
    "gust": 1.18
  },
  "rain": {
    "1h": 3.16
  },
  "clouds": {
    "all": 100
  },
  "dt": 1661870592,
  "sys": {
    "type": 2,
    "id": 2075663,
    "country": "IT",
    "sunrise": 1661834187,
    "sunset": 1661882248
  },
  "timezone": 7200,
  "id": 3163858,
  "name": "Zocca",
  "cod": 200
} 
"""
#Icon images found here
#var iconurl = "http://openweathermap.org/img/w/" + iconcode + ".png";