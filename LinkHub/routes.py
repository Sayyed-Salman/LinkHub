from flask import Blueprint
from flask import render_template
from flask import request, flash, redirect, url_for
from LinkHub import db
from LinkHub.models import Link
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
    return render_template('base.html', data=Link.query.order_by(Link.id.desc()))


@home_blueprint.route("/testserver")
def test():
    return render_template('base.html', data=data)


@home_blueprint.route("/addresource", methods=["GET", "POST"])
def add_resource():
    if request.method == 'POST':
        if not request.form['description'] or not request.form['name'] or not request.form['link'] or not request.form['email']:
            flash('Please enter all fields', 'error')
        else:
            desc = request.form['description']
            name = request.form['name']
            link = request.form['link']
            email = request.form['email']

            resource = Link(name, desc, link, email)
            db.session.add(resource)
            db.session.commit()

            return redirect(url_for('home.index_sus'))
    return render_template('addresource.html')
