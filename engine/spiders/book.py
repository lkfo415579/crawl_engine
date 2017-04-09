import scrapy
import uniout
import codecs

class BookSpider(scrapy.Spider):
    name = "book"
    website = "http://www.tingvoa.com"
    allowed_domains = ["www.tingvoa.com"]
    start_urls = [
        "http://www.tingvoa.com/bookworm/"
    ]

    def parse(self, response):
        '''filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)'''
         #bookname = response.selector.xpath('//h5/a/text()').extract()
        book_urls = response.selector.xpath('//h5/a/@href').extract()
        web = self.website
        print book_urls[:2]
        book_urls = [web+"/"+url for url in book_urls]
        for url in book_urls:
            yield scrapy.Request(url, callback=self.mid_parse)
        
        '''with codecs.open('bookname.txt', 'w','utf-8') as the_file:
            the_file.write("\n".join(bookname))
        print bookname'''
        
    def mid_parse(self,response):
        #next_step = response.selector.xpath('//div[@class="newslist"]').extract()
        next_step = response.selector.xpath('//div[@class="newslist"]/dl/dt/span/a/@href').extract()
        next_step = next_step[1:]
        middle_step = []
        #import sys
        for url in next_step:
            tmp = url.split("/")
            tmp[-1] = tmp[-1][:-5] +"_3.html"
            middle_step.append(self.website+"/".join(tmp))
        for url in middle_step:
            yield scrapy.Request(url, callback=self.final_parse) 
        #print middle_step[:-5]
        #print next_step
    def final_parse(self,response):
        title = response.selector.xpath('//div[@id="entrytitle"]/h1/text()').extract()
        title = title[0]
        text = response.selector.xpath('//div[@id="entrybody"]/p/text()').extract()
        text = text[3:]
        
        with codecs.open('book_text.txt', 'a','utf-8') as the_file:
            the_file.write("$"+title+"\n")
            the_file.write("\n".join(text))
            the_file.write("\n")
        #print bookname
        
        
        