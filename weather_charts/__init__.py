from flask import Flask, current_app
import weather_charts.config as conf

app = Flask(__name__)
app.config.from_object(conf)

import weather_charts.routes
