# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import pymongo
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log

import re 

class BaiduPipeline(object):
        def __init__(self):
                """ Initiate a MongoDB connection, a create the settings['MONGODB_COLLECTION'] collection. """
                connection = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
                db = connection[settings['MONGODB_DB']]
                self.collection = db[settings['MONGODB_COLLECTION']]

        def process_item(self, item, spider):

                print item['songName']
                print '\n'
                self.collection.insert(dict(item))
                log.msg("Item wrote to MongoDB database %s/%s" %
                    (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
                    level=log.DEBUG, spider=spider)
                return item
