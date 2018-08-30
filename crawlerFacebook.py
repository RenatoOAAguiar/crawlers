import json
import urllib3
import codecs
import random
import string
import time

appId = '1176112342531462'
appSecret = '10895659c1511e6514ff43668e5724f8'
accessToken = 'access_token=' + appId + '|' + appSecret
nextItem = ''
texto = ''

idPostagem = '1174910665991251'

url = 'https://graph.facebook.com/v2.7/' + idPostagem + '/comments?' + accessToken

while 1:
    http = urllib3.ProxyManager("https://server:port/")
    response = http.request('GET', url)
    dados = json.loads(response.data.decode("utf-8"))

    for item in dados["data"]:
        with open('facebook/' + '1174910665991251' +'.txt', 'a', encoding='utf-8') as f:
                f.write(item["message"] + '\n')

    if "next" in dados["paging"] and len(dados["paging"]["next"]) > 0:
        url = dados["paging"]["next"]
        time.sleep(1)
    else:
        url = ''

    if url == '':
        break
