# -*- coding: utf8 -*-

import json

import requests
from app import dao

UNIDADE_MEDIDA = 'R$'


class AbstractScraping():
    def client(self):
        client = dao.Client()
        return client

    def db(self):
        client = self.client()
        return client.getDb()


class Webscraping(AbstractScraping):
    def __init__(self, url):
        self.url = url

    def response(self):
        r = requests.get(self.url)
        return r

    def parse(self, collection):
        dados = json.loads(self.response().content)
        if 'dados' == collection:
            self.parse_dados(dados)
        else:
            self.parse_link(dados)

    def parse_link(self, value):
        results = {}
        for d in value:
            results[d] = value[d]
        print results

    def parse_dados(self, value):
        results = []
        if UNIDADE_MEDIDA == value['unidade_medida']['unidade_medida']:
            link = {}
            link['id'] = value['id']
            link['nome'] = value['nome_estendido']
            link['url'] = value['url']
            results.append(link)
        self.db()['dados'].insert(results)

    def parse_serie(self, value):
        results = []

class WebSpider(AbstractScraping):
    def run(self):
        dados = self.db()['serie'].find()
        for dado in dados[:1]:
            scraping = Webscraping(dado['url'])
            scraping.parse(dado['id'])
