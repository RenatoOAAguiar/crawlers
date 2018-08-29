import scrapy
import random
import string
import json
import codecs

def writeTofile(fileName,text):
    with codecs.open(fileName,'w','utf-8') as outfile:
        outfile.write(text)

class BlogSpider(scrapy.Spider):
    name='medium_scrapper'
    handle_httpstatus_list = [401,400]
    
    autothrottle_enabled=True
    
    def start_requests(self):
        
        start_urls = ['https://www.medium.com/search/posts?q=facebook']
        
        for url in start_urls:
            yield scrapy.Request(url,method='POST',callback=self.parse)
    
    def parse(self,response):
              
        response_data=response.text
        response_split=response_data.split("while(1);</x>")
       
        response_data=response_split[1]
        filename="medium.json"
        writeTofile(filename,response_data)
        
        with codecs.open(filename,'r','utf-8') as infile:
            data=json.load(infile)
        #Check if there is a next tag in json data
        if 'paging' in data['payload']:
            data=data['payload']['paging']
            if 'next' in data:
                #Make a post request
                print("In Paging, Next Loop")
                data=data['next']
                formdata={
                        'ignoredIds':data['ignoredIds'],
                        'page':data['page'],
                        'pageSize':data['pageSize']
                        }               

                yield scrapy.Request('https://www.medium.com/search/posts?q=facebook',method='POST',body=json.dumps(formdata),callback=self.parse)  