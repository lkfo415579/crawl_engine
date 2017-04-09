import scrapy
import uniout
import codecs
import sys
from scrapy import Selector
class courtSpider(scrapy.Spider):
    name = "court"
    website = "http://www.court.gov.mo/"
    allowed_domains = ["court.gov.mo"]
    start_urls = [
        "http://www.court.gov.mo/sentence/pt/1"
    ]
    custom_settings = {
        'DOWNLOAD_DELAY': '0.0',
    }
    #start = 1
    #loop = 36534040
    #
    for i in range(2, 30000):
        start_urls.append("http://www.court.gov.mo/sentence/pt/"+str(i))

    '''def parse(self, response):
        book_urls = response.selector.xpath('//p[@class="title"]/a/@href').extract()
        web = self.website
        print book_urls[:2]
        book_urls = [web+url for url in book_urls]
        for url in book_urls:
            yield scrapy.Request(url, callback=self.mid_parse)'''
            
    def handle_splited(self,html):
        output = []
        for line in html:
            sel = Selector(text=line, type="html")
            sen = sel.xpath('//text()').extract()
            #print line
            output.append(''.join(sen))
        return [x.strip() for x in output]
        
    def parse(self,response):
        web = response.url
        data = response.selector.xpath('//body/text()').extract()

        with codecs.open('court.pt', 'a','utf-8') as the_file:
            the_file.write("@"+web +"\n")
            the_file.write("".join(data)+"\n")
        web = web.split('/')
        url = 'http://www.court.gov.mo/sentence/zh/'+web[-1]
        yield scrapy.Request(url, callback=self.C_parse)
            
    def C_parse(self,response):
        web = response.url
        data = response.selector.xpath('//body/text()').extract()

        with codecs.open('court.zh', 'a','utf-8') as the_file:
            the_file.write("@"+web +"\n")
            the_file.write("".join(data)+"\n")