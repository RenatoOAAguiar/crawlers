"""# -- coding: utf-8 --"""

import scrapy
import random
import string
import time

proxy = 'http://server:port'

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    custom_settings = {
        'HTTPPROXY_ENABLED': True
    }
    start_urls = ['http://machado.mec.gov.br/obra-completa-lista?limitstart=0']
    for i in range(1,10):
        start_urls.append('http://machado.mec.gov.br/obra-completa-lista?start=' + str(i * 12))
    
    def parse(self, response):
        for a in response.css("div.download"):
            yield scrapy.Request('http://machado.mec.gov.br' + a.css("::attr(href)").extract_first(), callback=self.second, meta={'proxy': proxy})
   
    def second(self, response):
        print("Resposta :")
        print(response)
        with open('pdfMachado/' + ''.join([random.choice(string.ascii_lowercase) for i in range(14)]) + '.pdf', 'wb') as f:
            f.write(response.body)
        
        