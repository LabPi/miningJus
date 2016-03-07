# -*- coding: utf8 -*-

from pymongo import MongoClient


# Faz a conexão com o banco de dados
class Client():
    url = 'mongodb://localhost:27017/'
    dbname = 'dadosgov'

    def getDb(self):
        client = MongoClient(self.url)
        return client[self.dbname]
