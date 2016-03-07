# -*- coding: utf8 -*-

import json
import requests

from crawler import webscraping


class Main():
    base_url = 'http://api.pgi.gov.br/api/1/serie'

    # retorna o tipo da requisição feita
    def content_type(self, header):
        headers = header.split(";")
        return headers[0]

    def scraping(self):
        r = self.response(self.base_url)
        content_type = self.content_type(r.headers['content-type'])
        if 'application/json' == content_type:
            scraping = webscraping.Webscraping()
            scraping.parse(r.content)

    def response(self, url):
        r = requests.get(url)
        return r

    def spider(self):
        spider = webscraping.WebSpider()
        spider.run()


if __name__ == '__main__':
    print 'Iniciando a mineração de dados'
    main = Main()
    # scraping = main.scraping()
    spider = main.spider()
else:
    print 'Este arquivo não é o __main__'
