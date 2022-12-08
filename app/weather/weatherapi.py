import http.client

conn = http.client.HTTPSConnection("weatherbit-v1-mashape.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "6890be5119msh9ed3c155319ec9fp1b664cjsn3cc16cb3bf3a",
    'X-RapidAPI-Host': "weatherbit-v1-mashape.p.rapidapi.com"
    }

conn.request("GET", "/forecast/minutely?lat=35.5&lon=-78.5&units=imperial", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))