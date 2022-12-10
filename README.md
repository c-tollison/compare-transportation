# compare-transportation

Final project for cpsc-3720

Create an environment and start it:
<br>
Mac:
<br>

```
$ python3 -m venv venv
$ . venv/bin/activate
```

Windows:
<br>

```
$ py -3 -m venv venv
$ venv\Scripts\activate
```

After enviroment is running, install dependencies:
<br>

```
$ pip install -r requirements.txt
```

run application locally:
<br>

```
$ flask --app app/main run
```

The app will be hosted on here:
<br>
[Port 5000](http://127.0.0.1:5000/)

User Stories Can Be Found In 'Compare Transportation User Stories'.docx

APIs Used:
- Geocoding API: https://docs.mapbox.com/api/search/geocoding/
- Google Maps APIs
- OpenWeather API: https://openweathermap.org/current

Scope:
  A website that compares different transportation methods and routes
  by distance and duration given a starting point and destination
  by the user. Also provides current weather conditions to help
  the user further compare travel methods.
