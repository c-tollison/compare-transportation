from flask import Blueprint, render_template, request
import app.geocoding.geocoding as geocoding
from app.transit.GoogleRoutes import getRoutes
from app.weather.weatherapi import getWeather

views = Blueprint('views', __name__)




@views.route("/", methods=["GET", "POST"])
@views.route("/location", methods=["POST"])
def home():
    route = {
        'start': '',
        'destination': ''
    }
    routes = {}
    weather = {}
    #On form submission, process input
    if request.path == '/' and request.method == 'POST':
        if request.form['submit'] == 'Submit Route':
            route['start'] = request.form['start']
            route['destination'] = request.form['destination']
            routes = getRoutes(route['start'], route['destination'])
            weather = getWeather(route['start'])
    # Sets route['start'] to the address obtained by
    # reverse geocoding the given coordinates 
    if request.path == '/location':
        lat = request.json['latitude']
        lng = request.json['longitude']
        addr = geocoding.reverseGeocode(lat, lng)
        route['start'] = addr
        return {'addr': addr}
    return render_template('index.html', 
        template_start = route['start'], 
        template_destination = route['destination'],
        getLocation = False if route['start'] else True,
        template_routes = routes if routes else False,
        template_weather = weather if weather else False)