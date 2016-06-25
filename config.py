import os.path

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def add_config(app):
    app.config["DEBUG"] = False
    app.config["SECRET_KEY"] = "bugaga"

    # Database.
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://dfcxhwvghrjcut:ADw_Vg6BtHPuxdhaq_7jPGRgfX@ec2-176-34-103-75.eu-west-1.compute.amazonaws.com/d94bmnricksn05"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
