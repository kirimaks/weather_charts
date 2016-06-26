# -*- coding: utf-8 -*-
import scrapy
from weather_scraper.items import WeatherScraperItem
from datetime import datetime


class PogodaSpider(scrapy.Spider):
    name = "pogoda"
    allowed_domains = ["pogoda.yandex.ru"]
    start_urls = (
        'https://pogoda.yandex.ru/sochi',
    )

    def __init__(self, chart_id, *pargs, **kwargs):
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
