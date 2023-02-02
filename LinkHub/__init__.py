from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app():
    """
    Initialize the core application
    """

    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    from LinkHub.models import Link

    # with app.app_context():
    #     db.create_all()

    from LinkHub.routes import home_blueprint, new_blueprint
    app.register_blueprint(home_blueprint)
    app.register_blueprint(new_blueprint)

    return app
