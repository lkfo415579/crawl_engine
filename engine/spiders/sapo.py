import scrapy
import uniout
import codecs

class SAPOSpider(scrapy.Spider):
    name = "sapo"
    website = "http://rr.sapo.pt"
    allowed_domains = ["rr.sapo.pt"]
    start_urls = [
        "http://rr.sapo.pt/noticia/4500/"
    ]
    for i in range(4501, 300000):
        start_urls.append('http://rr.sapo.pt/noticia/'+str(i)+'/')

    def parse(self, response):
        '''filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)'''
        title = response.selector.xpath('//h1/text()').extract()
        title = title[0]
        core_text = response.selector.xpath('//span[@class="large fw-500"]/text()').extract()
        big_text = response.selector.xpath("//div[contains(@class, 'column-group half-left-padding')]/div[@class='slab-400 all-100']/p/text()").extract()
        web = self.website
        #print big_text
        try:
            with codecs.open('sapo.txt', 'a','utf-8') as the_file:
                #the_file.write("\n".join(title))
                the_file.write("@"+response.url+"\n")
                the_file.write("$"+title+"\n")
                the_file.write("\n".join(big_text))
                the_file.write("\n")
        except:
            pass
        
        