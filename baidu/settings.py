# Scrapy settings for baidu project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'baidu'

SPIDER_MODULES = ['baidu.spiders']
NEWSPIDER_MODULE = 'baidu.spiders'

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "mydb"
MONGODB_COLLECTION = "song_sweet"
ITEM_PIPELINES = ['baidu.pipelines.BaiduPipeline',]

# DOWNLOAD_DELAY = 3

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'baidu (+http://www.yourdomain.com)'
