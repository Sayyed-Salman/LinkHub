import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config():
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or "very secret key xuxu"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        "sqlite:///" + os.path.join(base_dir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
