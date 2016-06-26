#!/bin/bash

BASE_DIR=`dirname $(realpath $0)`
echo $BASE_DIR

cd $BASE_DIR

scrapy crawl pogoda -a chart_id=$1
