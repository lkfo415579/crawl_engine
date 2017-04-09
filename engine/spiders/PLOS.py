import scrapy
import uniout
import codecs
import sys
class sol_sapoSpider(scrapy.Spider):
    name = "PLOS"
    website = "http://www.journals.plos.org/"
    allowed_domains = ["sol.sapo.pt"]
    start_urls = [
        "http://journals.plos.org/plosone/article?id=info%3Adoi/10.1371/journal.pone.0162945"
    ]
    #start = 162944
    #loop = 160000
    for i in range(1, 60000):
        start_urls.append("http://journals.plos.org/plosone/article?id=info%3Adoi/10.1371/journal.pone.0"+str(59413-i).zfill(6)+"/")

    def parse(self, response):
        '''filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)'''
        #title = response.selector.xpath('//span[@style="color: #000000;"]/text()').extract()
        title = response.selector.xpath('//h1[@id="artTitle"]/text()').extract()
        title = title[0]
        #print title
        core_text = response.selector.xpath('//div[@id="artText"]/div//*[string-length(text()) > 0]/text()').extract()
        #name = response.selector.xpath('name(//div[@id="artText"]/div//p[string-length(text()) > 0]//* )').extract()
        #print name
        tmp = [x.strip() for x in core_text if x.strip() != "" ]
        core_text = []
        small_ball = ""
        for line in tmp:
            if len(line) > 15:
                try:
                    if small_ball != "":
                        core_text[-1] = str(core_text[-1]) + small_ball + line
                        small_ball = ""
                        continue
                except:
                    pass
                core_text.append(line)
            else:
                small_ball = line
        
        #title = core_text[0]
        #core_text = [x for x in core_text if x.strip() != ""]
        #print core_text
        #big_text = response.selector.xpath("//div[contains(@class, 'column-group half-left-padding')]/div[@class='slab-400 all-100']/p/text()").extract()
        web = self.website
        #print core_text
        try:
            with codecs.open('PLOS3.txt', 'a','utf-8') as the_file:
                #the_file.write("\n".join(title))
                the_file.write("@"+response.url+"\n")
                the_file.write("$"+title+"\n")
                the_file.write("\n".join(core_text))
                the_file.write("\n")
        except:
            pass
        
        