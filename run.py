from weather_charts import app
from flask_script import Manager
from jobs import scheduler

manager = Manager(app)
scheduler.start()

if __name__ == "__main__":
    manager.run()
