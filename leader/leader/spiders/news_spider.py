import scrapy
from leader.items import LeaderItem

class Newsspider(scrapy.Spider):
    """
    A class to scrape the limerick Leader will parse and collect 
    Links from the site
    """
    name = "News"
    allowed_domains = ['limerickleader.ie']# a list of approved domains to follow 
    start_urls = [
            'http://www.limerickleader.ie/sezioni/131/news'
            ]# starting points 
    

    def parse(self, response):
        for links in response.xpath('//h2[@class="titolo vc_title"]'):
            items = LeaderItem()
            items['title'] = links.xpath('a/text()').extract()
            items['link'] = links.xpath('a/@href').extract()
            for url in items['link']:
                print url
                request = scrapy.Request(url, callback=self.parsebody) # create a request for each link 
                request.meta['items'] = items # shallow copies items to pass to next method 
                yield request

    def parsebody(self,response): # parses bodytext 
        items = response.meta['items']
        for text in response.xpath('//div[@class="GN4_body"]'):
            items['body'] =text.xpath('p/text()').extract()        
            yield items

