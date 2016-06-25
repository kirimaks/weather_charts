from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
import routes
import models

# Routes and settings.
app = Flask(__name__)
config.add_config(app)
routes.add_routes(app)

# Database.
db = SQLAlchemy(app)
models.make_models(db)
db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
