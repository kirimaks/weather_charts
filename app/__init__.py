import os
import sys
from flask import Flask

mod_dir = os.path.dirname(__file__)


import app.app_conf as conf

application = Flask(__name__, template_folder="../templates")
application.config.from_object(conf)

import app.routes
