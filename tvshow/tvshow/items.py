# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TvshowItem(scrapy.Item):
    title=scrapy.Field()
    yiming=scrapy.Field()
    year=scrapy.Field()
    country=scrapy.Field()
    tag=scrapy.Field()
    language=scrapy.Field()
    date=scrapy.Field()
    chapter=scrapy.Field()
    duration=scrapy.Field()
    director=scrapy.Field()





