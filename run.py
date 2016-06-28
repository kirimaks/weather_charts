from app import application
from flask_script import Manager

import scheduler.tasker     # Start scheduler

manager = Manager(application)

if __name__ == "__main__":
    manager.run()
