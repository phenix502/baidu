#!/usr/bin/python
#-*-coding:utf-8-*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from baidu.items import BaiduItem

import re

class sweetCrawler(BaseSpider):
	name = "sweet"
	allowed_domains = ["music.baidu.com"]
	start_urls = ["http://music.baidu.com/song/1102942"]
	
        
	def parse(self, response):
		hxs = HtmlXPathSelector(response)
		item = BaiduItem()
		content = hxs.select('//*[@id="lyricCont"]/text()')
       
                ##lyric
		lyric = ''
		for word in content:
			lyric += word.extract()
		item['lyric'] = lyric

		## hot: define how popular the song
		hot = hxs.select('//span[@class="num"]/text()').extract()[0]
		item['hot'] = hot 

		## singer
		singer = hxs.select('//span[@class="author_list"]/a/text()').extract()[0]
		patt = '\s'
		item['singer'] = re.sub(patt,'',singer)
		
		## songName       
		songName = hxs.select('//h2/span[1]/text()').extract()[0]
		item['songName'] = songName
		return item


		 
