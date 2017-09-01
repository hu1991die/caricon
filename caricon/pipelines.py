# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CariconPipeline(object):
    def process_item(self, item, spider):
        return item
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.http import Request
from scrapy.exceptions import DropItem
import os

class MyImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        #url_file_name= request.url.split('/')[-1]
        #image_guid = hashlib.sha1(to_bytes(url)).hexdigest()
        alt_name=request.meta["alt"]
        return 'full/%s%s' % (alt_name, os.path.splitext(request.url)[-1])

    def get_media_requests(self, item, info):
        yield Request(item["image_urls"][0], meta={'alt':item["alt"]})