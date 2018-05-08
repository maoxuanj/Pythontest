# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html



from scrapy.item import Item,Field
class TencentItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()       #职位名称
    catalog = Field()    #职位类别
    workLocation = Field()   #工作地点
    recruitNumber =Field()         #招聘人数
    detaliLink = Field() #链接
    publishtime = Field()#招聘时间



