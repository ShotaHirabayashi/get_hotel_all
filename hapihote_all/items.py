# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HapihoteAllItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    A_hotel_name = scrapy.Field()
    B_adress = scrapy.Field()
    C_tel = scrapy.Field()
    pass
