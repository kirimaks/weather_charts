# -*- coding: utf-8 -*-
import scrapy
import os.path
import sys

mod_path = os.path.abspath(__file__)
basedir = str.join("/", mod_path.split("/")[:-2])
print(basedir)
sys.path.append(basedir)

from items import WeatherScraperItem
from datetime import datetime


class PogodaSpider(scrapy.Spider):
    name = "pogoda"
    allowed_domains = ["pogoda.yandex.ru"]
    start_urls = (
        'https://pogoda.yandex.ru/sochi',
    )

    def __init__(self, chart_id=None, *pargs, **kwargs):
        scrapy.Spider.__init__(self, *pargs, **kwargs)
        assert(chart_id)
        self.chart_id = chart_id

    def parse(self, response):
        item = WeatherScraperItem()

        temp = response.xpath("/html/body/div[2]/div[1]/div[3]/div[2]/text()").extract()[0]
        temp = temp.split(":")[-1]
        temp = temp.strip().strip("+")

        item['temp'] = temp
        item['time'] = str(datetime.now())

        return item
