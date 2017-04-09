import scrapy
import uniout
import codecs
import sys
import datetime
from scrapy import Selector
class techSpider(scrapy.Spider):
    name = "tech"
    website = "https://techcrunch.com/"
    allowed_domains = ["techcrunch.com"]
    start_urls = [
        "https://techcrunch.com/2006/01/01/"
    ]
    #start = 1
    #loop = 36534040
    #
    count = datetime.date(2006, 01, 01)
    for i in range(1, 1000):
        #start_urls.append("https://www.ncbi.nlm.nih.gov/pubmed/"+str(i).zfill(7)+"/")
        count += datetime.timedelta(days=1)
        start_urls.append("https://techcrunch.com/"+count.strftime('%Y/%m/%d/'))

    def handle_splited(self,html):
        output = []
        for line in html:
            sel = Selector(text=line, type="html")
            sen = sel.xpath('//text()').extract()
            #print line
            output.append(''.join(sen))
        return [x.strip() for x in output]
        
    def mini_parse(self,response):
        web = response.url
        title = response.selector.xpath('//h1[@class="alpha tweet-title"]//text()').extract()
        author_date = response.selector.xpath('//div[@class="byline"]').extract()
        text = response.selector.xpath('//div[@class="article-entry text"]').extract()
        author_date = self.handle_splited(author_date)
        text = self.handle_splited(text)
        
        with codecs.open('tech.txt', 'a','utf-8') as the_file:
            the_file.write("$"+"".join(title)+"\n")
            the_file.write("@"+web +"\n")
            the_file.write("#"+"".join(author_date) +"\n")
            the_file.write("\n".join(text))
            the_file.write("\n")
            
    def parse(self,response):
        urls = response.selector.xpath('//h2[@class="post-title"]/a/@href').extract()
        #print urls
        for url in urls:
            yield scrapy.Request(url, callback=self.mini_parse)
        