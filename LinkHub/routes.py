from flask import Blueprint
from flask import render_template
home_blueprint = Blueprint('home', __name__)
new_blueprint = Blueprint('new', __name__, url_prefix="/projects")

data = [
    {
        "name": "Ben Ten",
        "description": "IR Practical 3 Code",
        "link": "https://www.google.com"
    },
    {
        "name": "Mike Oxlong",
        "description": "How to make pancakes.",
        "link": "https://www.google.com"
    },
    {
        "name": "Dicks Dinker",
        "description": "How to grow your plants an inch longer ;)",
        "link": "https://www.google.com"
    },
    {
        "name": "Blob Biter",
        "description": "The only article you will need.",
        "link": "https://www.google.com"
    },
    {
        "name": "Tren Bolate",
        "description": "Gains max.",
        "link": "https://www.google.com"
    },
    {
        "name": "Mein Kamph",
        "description": "How to reach the golden number (7mil.)",
        "link": "https://www.google.com"
    },
]


@home_blueprint.route("/")
def index_sus():
    return render_template('base.html')


@home_blueprint.route("/testserver")
def test():
    return render_template('base.html', data=data)


@home_blueprint.route("/addresource")
def add_resource():
    return render_template('addresource.html')
