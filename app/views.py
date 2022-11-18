from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route("/", methods=["GET", "POST"])
def home():
    route = {}
    if len(request.form) > 0:
        route['start'] = request.form['currentLocation']
        route['destination'] = request.form['destination']
    return render_template('index.html', template_route=route)
