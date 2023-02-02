from flask import Blueprint
from flask import render_template
home_blueprint = Blueprint('home', __name__)
new_blueprint = Blueprint('new', __name__, url_prefix="/projects")


@home_blueprint.route("/")
def index_sus():
    return render_template('base.html')


@home_blueprint.route("/testserver")
def test():
    return render_template('base.html')
