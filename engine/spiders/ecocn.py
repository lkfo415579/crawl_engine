import scrapy
import uniout
import codecs
import sys
from scrapy import Selector
class courtSpider(scrapy.Spider):
    name = "ecocn"
    website = "http://www.ecocn.org"
    allowed_domains = ["ecocn.org"]
    start_urls = [
        "http://www.ecocn.org/article-1-1.html"
    ]
    custom_settings = {
        'DOWNLOAD_DELAY': '0.0',
    }
    #start = 1
    #loop = 36534040
    #
    for i in range(2, 4000):
        start_urls.append("http://www.ecocn.org/article-"+str(i)+"-1.html")
    
    def handle_splited(self,html):
        output = []
        for line in html:
            sel = Selector(text=line, type="html")
            sen = sel.xpath('//text()').extract()
            #print line
            if (len(sen) != 0):
                #print sen
                output.append(''.join(sen))
        return [x.strip() for x in output]
        
    def parse(self,response):
        web = response.url
        title = response.selector.xpath('//div[@class="h hm"]/h1/text()').extract()
        text = response.selector.xpath('//td[@id="article_content"]/text()').extract()
        author = response.selector.xpath('//p[@class="xg1"]/text()').extract()
        text = self.handle_splited(text)
        title = self.handle_splited(title)
        author = self.handle_splited(author)
        
        
        with codecs.open('ecocn.txt', 'a','utf-8') as the_file:
            the_file.write("$"+"".join(title)+"\n")
            the_file.write("@"+web +"\n")
            the_file.write("#"+"".join(author) +"\n")
            the_file.write("\n".join(text))
            the_file.write("\n")