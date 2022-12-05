from flask import Blueprint, render_template, request
import app.transit.GoogleRoutes as GoogleRotues

views = Blueprint('views', __name__)


route = {
    'start': '',
    'destination': ''
}
@views.route("/", methods=["GET", "POST"])
def home():
    #On form submission, process input
    if request.method == 'POST':
        if request.form['submit'] == 'Submit Route':
            route['start'] = request.form['start']
            route['destination'] = request.form['destination']
            return GoogleRotues.getRoute(route['start'], route['destination'])
    return render_template('index.html', 
        template_start = route['start'], 
        template_destination = route['destination'],
        getLocation = False if route['start'] else True)
    
#Endpoint used to post user location to be used
#as the route start.
@views.route('/location', methods=["GET", "POST"])
def location():
    if request.method == 'POST':
        route['start'] = request.json['address']
    return route['start']