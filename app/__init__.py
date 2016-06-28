from flask import Flask
import app.app_conf as conf
from app.filters import moscow_tz

application = Flask(__name__, template_folder="../templates",
                    static_folder="../static")
application.config.from_object(conf)

application.jinja_env.filters['moscow_tz'] = moscow_tz

import app.routes
