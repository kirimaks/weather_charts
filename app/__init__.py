from flask import Flask
import app.app_conf as conf

application = Flask(__name__, template_folder="../templates")
application.config.from_object(conf)

import app.routes
