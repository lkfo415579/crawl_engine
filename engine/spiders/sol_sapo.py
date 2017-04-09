import scrapy
import uniout
import codecs
import sys
class sol_sapoSpider(scrapy.Spider):
    name = "sol_sapo"
    website = "http://www.sol.sapo.pt/"
    allowed_domains = ["sol.sapo.pt"]
    start_urls = [
        "http://sol.sapo.pt/artigo/100/"
    ]
    for i in range(1, 521000):
        start_urls.append("http://sol.sapo.pt/artigo/"+str(i)+"/")

    def parse(self, response):
        '''filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)'''
        #title = response.selector.xpath('//span[@style="color: #000000;"]/text()').extract()
        title = response.selector.xpath('//div[@class="large-9 medium-8 column artic_content"]/header/h1/text()').extract()
        title = title[0]
        #print title
        core_text = response.selector.xpath('//div[@class="large-8  column corpo"]//text()').extract()
        #title = core_text[0]
        core_text = [x for x in core_text if x.strip() != ""]
        #print core_text
        #big_text = response.selector.xpath("//div[contains(@class, 'column-group half-left-padding')]/div[@class='slab-400 all-100']/p/text()").extract()
        web = self.website
        #print core_text
        try:
            with codecs.open('sol_sapo.txt', 'a','utf-8') as the_file:
                #the_file.write("\n".join(title))
                the_file.write("@"+response.url+"\n")
                the_file.write("$"+title+"\n")
                the_file.write("\n".join(core_text))
                the_file.write("\n")
        except:
            pass
        
        