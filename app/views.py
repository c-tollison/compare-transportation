from flask import Blueprint, render_template, request
import app.geocoding.geocoding as geocoding

views = Blueprint('views', __name__)


route = {
    'start': '',
    'destination': ''
}
@views.route("/", methods=["GET", "POST"])
@views.route("/location", methods=["POST"])
def home():
    #On form submission, process input
    if request.path == '/' and request.method == 'POST':
        if request.form['submit'] == 'Submit Route':
            route['start'] = request.form['start']
            route['destination'] = request.form['destination']
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
        getLocation = False if route['start'] else True)