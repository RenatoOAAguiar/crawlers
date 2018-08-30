import scrapy
import random
import string

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://www.medium.com/search/posts?q=mark']
    
    def parse(self, response):
        for a in response.css("div.postArticle-content"):
        #for a in response.css("div.postItem"):
            yield scrapy.Request(a.css("::attr(href)").extract_first(), callback=self.second)

    #def start_requests(self):
    #    return [FormRequest("https://medium.com/brasil/search?q=politica", formdata={'pageSize' : 50}, callback=self.parse)]
    
    def second(self, response):
        print()
        with open(''.join([random.choice(string.ascii_lowercase) for i in range(12)]) +'.txt', 'a', encoding='utf-8') as f:
            for item in response.css("div.sectionLayout--insetColumn p::text").extract():
                f.write(item)
        