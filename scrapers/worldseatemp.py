import requests
from lxml import html
import re


def get_temp_worldseatemp():
    url = "http://worldseatemp.com/ru/Russia/Sochi/"

    resp = requests.get(url)
    tree = html.fromstring(resp.content)

    water_temp = tree.xpath('//*[@id="current"]/div/table/tr/td[2]/text()')[0]

    temp = re.findall(r"\d*\.?\d+", water_temp)[0]
    assert(temp)
    return temp

if __name__ == "__main__":
    out = get_temp_worldseatemp()
    print(out)
