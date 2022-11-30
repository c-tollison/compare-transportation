from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

userLocation = {
    'latitude': '',
    'longitude': '31.2123323'
}

@views.route("/", methods=["GET", "POST"])
def home():
    route = {}
    if len(request.form) > 0:
        route['start'] = request.form['currentLocation']
        route['destination'] = request.form['destination']
    return render_template('index.html', template_route=route, template_userLocation=userLocation)


@views.route('/location', methods=["POST"])
def userLocation():
    latitude = request.json['latitude']
    longitude = request.json['longitude']
    userLocation['latitude'] = latitude
    userLocation['longitude'] = longitude
    return render_template('index.html', template_userLocation=userLocation)