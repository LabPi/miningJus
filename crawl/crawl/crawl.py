# coding: utf-8 -*-

from datetime import datetime
from lxml import html
import requests

BASE_URL = 'http://dados.gov.br/dataset'

def check_list(item, values):
    # Verifica a ocorrencia do 'item' dentro de um 'list'
    # Retorna 'True' ou 'False'
    for value in values:
        if item == value:
            return False
    return True


class Crawler():
    def __init__(self, url):
        # Marca o tempo de inicio da requisição
        print 'GET %s' % ( url )
        self.start = datetime.now()
        self.url = url
        
    # Finaliza a aplicação
    def __del__(self):
        # Tempo de execução
        self.final = datetime.now()
        print 'Tempo Gasto: %s' % (self.final - self.start)
        
    # Executa o requisição na 'url' e executa o 'parse' da aplicação
    def run(self):
        # faz a requisição na url e atribui a 'r' o resultado
        r = requests.get(self.url)
        # verifica se requisição foi feita com sucesso
        if r.status_code != 200:
            return []
        # atribui o conteudo a 'page'
        self.page = r.content
        # verifica se a requisição é uma aplicação html
        content_type = r.headers['content-type'].split(';')[0]
        # apartir do tipo da requisição faz a 'parse' do conteudo
        if content_type == 'text/html':
            self.parse_html()
    
    # Pega todos os 'links' da requisição formatados como 'url'
    def getter_links_url(self, values):
        links_url = []
        # vare o resultado da busca xml
        for elt in values:
            link = elt.attrib['href']
            # verifica se a 'url' já existe na lista de 'links'
            if check_list(link, links_url):
                if link.find('http') < 0:
                    link = ''.join([self.path_url(), link])
                else:
                    link = url
                # adiciona um novo item no final da lista
                links_url.append(link)
        return links_url
    
    def parse(self, xpath):
        results = self.parse_xpath(xpath)
        links = self.getter_links_url(results)
        return links
        
    def parse_xpath(self, xpath):
        # transforma a requisição em xml
        tree = html.fromstring(self.page)
        # faz a busca no conteudo da aplicação
        return tree.xpath(xpath)
    
    def parse_html(self):
        # cria a regra de busca no formato xml
        xpath = '//*[@id="content"]/div[3]/div/section[1]//div/ul/li//div/h3/a'
        links = self.parse(xpath)
        if not links:
            xpath = '//*[@id="dataset-resources"]/ul/li/a'
            links = self.parse(xpath)
        
        for l in links:
            self.crawler(l)
    
    def path_url(self):
        # retorna o dominio da requisição
        splits = self.url.replace("://", '/').split('/')
        protocol = splits[0]
        base = ''.join([protocol, '://', splits[1]])
        return base
    
    @classmethod
    def crawler(self, url):
        Crawler(url).run()
        
        
if __name__ == "__main__":
    def nl():
        # cria uma nova linha
        print 
    start = datetime.now()
    print 'Inicio Aplicação: %s' % (start)
    nl()
    
    crawl = Crawler(BASE_URL)
    crawl.run()
    
    nl()
    final = datetime.now()
    print 'Final: %s' % (final)
    print 'Tempo Gasto: %s' % (final - start)
