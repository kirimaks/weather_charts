import os.path

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def add_config(app):
    app.config["DEBUG"] = False
    app.config["SECRET_KEY"] = "bugaga"

    # Database.
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1234@localhost/weather"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
