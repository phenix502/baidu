#!/usr/bin/python
#-*-coding:utf-8-*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from baidu.items import BaiduItem

import re

class sweetCrawler(BaseSpider):
	name = "sweet"
	allowed_domains = ["music.baidu.com"]
	start_urls = ["http://music.baidu.com/song/44062514"]
	
        
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		item = BaiduItem()
		content = hxs.select('//*[@id="lyricCont"]/text()')
	
		print('\n')
		lyric = ''
		for word in content:
			print word.extract() 
			lyric += word.extract()

		print lyric
		return item

		 
