"""# -- coding: utf-8 --"""

import scrapy
import random
import string
import time
from googletrans import Translator

translator = Translator()
proxy = 'http://proxylatam.indra.es:8080'

class BlogSpider(scrapy.Spider):
    name = 'blogspider',
    custom_settings = {
        'HTTPPROXY_ENABLED': True
    }
    start_urls = [
        'https://www.medium.com/search/posts?q=formula indy&limit=400',
        'https://www.medium.com/search/posts?q=geography&limit=400',
        'https://www.medium.com/search/posts?q=history&limit=400',
        'https://www.medium.com/search/posts?q=queen&limit=400',
        'https://www.medium.com/search/posts?q=elvis presley&limit=400',
        'https://www.medium.com/search/posts?q=redis&limit=400',
        'https://www.medium.com/search/posts?q=cars&limit=400',
        'https://www.medium.com/search/posts?q=rubens barrichello&limit=400',
        'https://www.medium.com/search/posts?q=ferrari&limit=400'
        ]
    
    def parse(self, response):
        for a in response.css("div.postArticle-content"):
            yield scrapy.Request(a.css("::attr(href)").extract_first(), callback=self.second, meta={'proxy': proxy})

    def second(self, response):
        texto = ''
        final = ''
        for body in response.css("div.sectionLayout--insetColumn"): 
            for item in body.css("p ::text, h1 ::text, strong ::text, h4 ::text").extract():
                #translator.detect(item)
                texto += item + '\n'
                if len(texto) >= 3000:
                    time.sleep(0.3)
                    final += translator.translate(texto, dest='pt').text
                    texto = ''
        if len(texto) > 0:
            time.sleep(0.3)       
            final += translator.translate(texto, dest='pt').text   
            with open('newfiles/' + ''.join([random.choice(string.ascii_lowercase) for i in range(12)]) +'.txt', 'a', encoding='utf-8') as f:
                f.write(final)
        
        