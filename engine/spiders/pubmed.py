import scrapy
import uniout
import codecs
import sys
from scrapy import Selector
class pubmedSpider(scrapy.Spider):
    name = "pubmed"
    website = "https://www.ncbi.nlm.nih.gov/"
    allowed_domains = ["ncbi.nlm.nih.gov"]
    start_urls = [
        "https://www.ncbi.nlm.nih.gov/pubmed/00000001"
    ]
    #start = 1
    #loop = 36534040
    #
    for i in range(2153990, 10004040):
        start_urls.append("https://www.ncbi.nlm.nih.gov/pubmed/"+str(i).zfill(7)+"/")

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
        title = response.selector.xpath('//div[@class="rprt abstract"]/h1').extract()
        text = response.selector.xpath('//div[@class="rprt abstract"]/div[@class="abstr"]/div').extract()
        author = response.selector.xpath('//div[@class="rprt abstract"]/div[@class="auths"]').extract()
        text = self.handle_splited(text)
        title = self.handle_splited(title)
        author = self.handle_splited(author)
        
        
        with codecs.open('pubmed.txt', 'a','utf-8') as the_file:
            the_file.write("$"+"".join(title)+"\n")
            the_file.write("@"+web +"\n")
            the_file.write("#"+"".join(author) +"\n")
            the_file.write("\n".join(text))
            the_file.write("\n")