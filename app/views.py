from flask import Blueprint, render_template, request, redirect, url_for

views = Blueprint('views', __name__)


route = {
    'start': '',
    'destination': ''
}
@views.route("/", methods=["GET", "POST"])
def home():
    if not route['start']:
        return render_template('index.html', getLocation = True)
    if request.method == 'POST':
        if request.form['submit'] == 'Submit Route':
            route['start'] = request.form['currentLocation']
            route['destination'] = request.form['destination']
    return render_template('index.html', 
        template_start = route['start'], 
        template_destination = route['destination'],
        getLocation = False if route['start'] else True)
    

@views.route('/location', methods=["GET", "POST"])
def location():
    if request.method == 'POST':
        route['start'] = request.json['address']
    return route['start']
    