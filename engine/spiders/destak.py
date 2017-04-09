import scrapy
import uniout
import codecs
import sys
class destakSpider(scrapy.Spider):
    name = "destak"
    website = "http://destak.pt"
    allowed_domains = ["destak.pt"]
    start_urls = [
        "http://destak.pt/artigo/1/"
    ]
    for i in range(1, 276200):
        start_urls.append(website+"/artigo/"+str(i)+'/')

    def parse(self, response):
        '''filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)'''
        title = response.selector.xpath('//div[@id="col1"]/h2/text()').extract()
        title = title[0]
        core_text = response.selector.xpath('//div[@class="text"]//text()').extract()
        #print core_text
        #big_text = response.selector.xpath("//div[contains(@class, 'column-group half-left-padding')]/div[@class='slab-400 all-100']/p/text()").extract()
        web = self.website
        #print core_text
        try:
            with codecs.open('destak.txt', 'a','utf-8') as the_file:
                #the_file.write("\n".join(title))
                the_file.write("@"+response.url+"\n")
                the_file.write("$"+title+"\n")
                the_file.write("\n".join(core_text))
                the_file.write("\n")
        except:
            pass
        
        