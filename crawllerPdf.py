"""# -- coding: utf-8 --"""

import scrapy
import random
import string
import time

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://nous.life/?s=&post_type=product']
    #http://nous.life/page/2/?s&post_type=product
    
    def parse(self, response):
        for a in response.css("p.product-title"):
            yield scrapy.Request(a.css("::attr(href)").extract_first(), callback=self.second)

    def second(self, response):
        seletor = response.css("div.product-summary ::attr(href)").extract_first()
        yield scrapy.Request("http://nous.life" + str(seletor), callback=self.third)
   
    def third(self, response):
        print("Resposta :")
        print(response)
        with open('pdf/' + ''.join([random.choice(string.ascii_lowercase) for i in range(14)]) + '.pdf', 'wb') as f:
            f.write(response.body)
        
        