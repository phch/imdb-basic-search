# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class IMDbMovie(scrapy.Item):
    rank = scrapy.Field()
    title = scrapy.Field()
    year = scrapy.Field()
    main_people = scrapy.Field()
    rating = scrapy.Field()
