import scrapy
from leader.items import LeaderItem

class Newsspider(scrapy.Spider):
    """
    A class to scrape the limerick Leader will parse and collect 
    Links from the limerick Leader
    """
    name = "News"
    allowed_domains = ['limerickleader.ie']
    start_urls = [
            'http://www.limerickleader.ie/sezioni/131/news'
            ]

    def parse (self, response):
        for links in response.xpath('//div'):
            items = LeaderItem()
            items['title'] = links.xpath('//a/text()').extract()
            items['link'] = links.xpath('//a/@href').extract()
            yield items
