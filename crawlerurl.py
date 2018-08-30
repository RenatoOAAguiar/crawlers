"""# -- coding: utf-8 --"""

import scrapy
import random
import string
import time

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.medium.com/search/posts?q=reforma politica&limit=400']
    
    def parse(self, response):
        for a in response.css("div.postArticle-content"):
            yield scrapy.Request(a.css("::attr(href)").extract_first(), callback=self.second)

    def second(self, response):
        texto = ''
        for body in response.css("div.sectionLayout--insetColumn"): 
            for item in body.css("p ::text, h1 ::text, strong ::text, h4 ::text").extract():
                #translator.detect(item)
                texto += item + '\n'
        if len(texto) > 0:   
            with open('newfiles/' + ''.join([random.choice(string.ascii_lowercase) for i in range(14)]) +'.txt', 'a', encoding='utf-8') as f:
                f.write(texto)
        
        