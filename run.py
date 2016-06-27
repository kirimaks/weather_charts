import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from app import application
from flask_script import Manager
import scheduler.tasks      # Import and run.

manager = Manager(application)

if __name__ == "__main__":
    manager.run()
