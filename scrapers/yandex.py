import logging
from lxml import html
import requests

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_temp_yandex():
    url = "https://pogoda.yandex.ru/sochi"

    resp = requests.get(url)
    tree = html.fromstring(resp.content)

    try:
        water_temp = tree.xpath("//div[@class='current-weather__water']/text()")[0]
        water_temp = water_temp.split(":")[-1].strip().strip("+")
        water_temp = float(water_temp)
    except:
        logger.critical("No data avaliable, return 0")
        water_temp = 0

    assert(water_temp)

    return water_temp


if __name__ == "__main__":
    buff = get_temp_yandex()
    print(buff)
