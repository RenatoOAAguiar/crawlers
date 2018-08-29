"""# -- coding: utf-8 --"""

import scrapy
import random
import string
import time
from urllib.parse import unquote

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    
    def parse(self, response):
        for a in response.css("div.widget--info__text-container"):
            url = str(a.css("::attr(href)").extract_first())
            url = url.split("&u=")[1]
            url = url.split("&key=")[0]
            url = unquote(url)
            yield scrapy.Request(url, callback=self.second)

    def second(self, response):
        texto = ''
        #print("RESPONSE: " + str(response.css("div")))
        for body in response.css("div.mc-article-body"): 
            for item in body.css("p.content-text__container ::text, meta ::text, h1 ::text, h2 ::text, strong ::text, h4 ::text").extract():
                texto += item + '\n'

        if len(texto) > 0:
            with open('g1/' + ''.join([random.choice(string.ascii_lowercase) for i in range(12)]) +'.txt', 'a', encoding='utf-8') as f:
                f.write(texto)
        
    def __init__(self, pergunta=''):
        if pergunta == '':
            return
        start_urls = []
        for item in range(1, 800):
            start_urls.append('https://g1.globo.com/busca/?q=' + pergunta + '&order=relevant&page=' + str(item))
        
        self.start_urls = start_urls
