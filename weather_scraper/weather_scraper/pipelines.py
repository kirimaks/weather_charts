# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sys
import os.path

abspath = os.path.abspath(__file__)
basedir = basedir = str.join("/", abspath.split('/')[:-3])
sys.path.append(basedir)

from weather_charts.database import db_session
from weather_charts.models import Data


class WeatherScraperPipeline(object):
    def process_item(self, item, spider):
        temp = item["temp"]
        chart_id = spider.chart_id
        assert(chart_id)
        data = Data(indicator=temp, chart_id=chart_id)

        db_session.add(data)
        db_session.commit()

        return item
