# -*- coding: utf-8 -*-
import scrapy
from ..items import  CariconItem

class CarSpider(scrapy.Spider):
    name = "car"
    #allowed_domains = ["http://car.bitauto.com/qichepinpai/"]
    start_urls = ['http://car.bitauto.com/qichepinpai']

    def parse(self, response):
        self.logger.info("-"*40 + response.url)
        #self.logger.info(response.css(".lazy::attr(data-original)").extract())
        for it in response.css(".list_pic img"):
            pic = CariconItem()
            pic["image_urls"] = it.css("::attr(src)").extract()
            pic["alt"] = it.css("::attr(alt)").extract_first()
            #self.logger.info(pic)
            yield pic
