import scrapy
import uniout
import codecs
import sys
class bnptSpider(scrapy.Spider):
    name = "bnpt"
    website = "http://www.bnportugal.pt/"
    allowed_domains = ["bnportugal.pt"]
    start_urls = [
        "http://www.bnportugal.pt/index.php?option=com_content&view=article&id=1187&catid=166%3A2016&Itemid=1197&lang=pt"
    ]
    for i in range(1, 1200):
        start_urls.append("http://www.bnportugal.pt/index.php?option=com_content&view=article&id="+str(i)+"&catid=166%3A2016&Itemid=1197&lang=pt")

    def parse(self, response):
        '''filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)'''
        #title = response.selector.xpath('//span[@style="color: #000000;"]/text()').extract()
        #title = response.selector.xpath('//span[@style="color: #000000;"]/text()').extract()
        #title = title[0]
        #print title
        core_text = response.selector.xpath('//td[@id="content"]//text()').extract()
        title = core_text[0]
        core_text = [x for x in core_text if x != "\r\n"][1:]
        #print core_text
        #big_text = response.selector.xpath("//div[contains(@class, 'column-group half-left-padding')]/div[@class='slab-400 all-100']/p/text()").extract()
        web = self.website
        #print core_text
        try:
            with codecs.open('bnpt.txt', 'a','utf-8') as the_file:
                #the_file.write("\n".join(title))
                the_file.write("@"+response.url+"\n")
                the_file.write("$"+title+"\n")
                the_file.write("\n".join(core_text))
                the_file.write("\n")
        except:
            pass
        
        