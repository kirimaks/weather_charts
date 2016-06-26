from flask import Flask
import weather_charts.config as conf

app = Flask(__name__)
app.config.from_object(conf)

import weather_charts.routes
