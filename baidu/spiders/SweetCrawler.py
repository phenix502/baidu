#!/usr/bin/python
#-*-coding:utf-8-*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from baidu.items import BaiduItem

import re

class sweetCrawler(CrawlSpider):
	name = "sweet"
	allowed_domains = ["music.baidu.com"]
	num = range(0, 1000, 50)
	start_urls = []
	for i in num:
		urls = "http://music.baidu.com/tag/%E7%94%9C%E8%9C%9C?start={0}&size=50".format(i)
	# start_urls = ["http://music.baidu.com/tag/%E7%94%9C%E8%9C%9C"]
		start_urls.append(urls)

	rules = (

                # allow in
        Rule(SgmlLinkExtractor(allow= ('.+/tag/%E7%94%9C%E8%9C%9C.+$') ), ),
        Rule(SgmlLinkExtractor(allow= ('music\.baidu\.com/song/.+',)),callback = 'parse_lyric'),
        
		)
		

        
	def parse_lyric(self, response):
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
		songName = hxs.select('//ul[@class="path-list clearfix"]/li[4]/text()').extract()[0]
		item['songName'] = songName
		return item


	

		 
