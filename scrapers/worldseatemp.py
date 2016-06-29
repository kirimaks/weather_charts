import logging
import requests
from lxml import html
import re

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_temp_worldseatemp():
    url = "http://worldseatemp.com/ru/Russia/Sochi/"

    resp = requests.get(url)
    tree = html.fromstring(resp.content)

    try:
        water_temp = tree.xpath('//*[@id="current"]/div/table/tr/td[2]/text()')[0]
        temp = re.findall(r"\d*\.?\d+", water_temp)[0]
    except:
        logger.critical("No data awaliable, return 0")
        temp = 0

    temp = float(temp)

    return temp

if __name__ == "__main__":
    out = get_temp_worldseatemp()
    print(out)
