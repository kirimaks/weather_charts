from lxml import html
import requests


def get_water_temp():
    url = "https://pogoda.yandex.ru/sochi"
    resp = requests.get(url)
    tree = html.fromstring(resp.content)

    water_temp = tree.xpath("//div[@class='current-weather__water']/text()")[0]
    water_temp = water_temp.split(":")[-1].strip().strip("+")

    assert(water_temp)

    return water_temp
