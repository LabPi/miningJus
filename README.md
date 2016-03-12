# miningJus

## Tema

Software para controle de gastos do governo federal

## Objetivo do Projeto

Esse projeto visa atender as necessidade dos brasileiros de saber sobre gastos do governo. 
Trazendo a informação de quanto está sendo gasto e onde está sendo gasto os recursos públicos.

## Método de Trabalho

O software será desenvolvido em etapas, sendo elas:

* Web Scraping para extração de todos os dados, em formato JSON, que tratam de recuros financeiros do site [Portal Brasileiro dos Dados Abertos](http://dados.gov.br), atráves da [API](http://api.pgi.gov.br) disponibilizada pelo mesmo
* Aplicativo mobile para visualização dados processados pelo Web Scraping

### Web Scraping

Aplicação desenvolvida em python para extrair dados de sites apartir de uma url.
Nessa primeira versão o software é capaz apenas de processar páginas em formato json, nas proximas versões ele já será capaz de extrair informação de mais formatos web.
O crawler ficará rodando em busca de novas informações. Apartir da lista já existente no banco de dados irá verificar se ouve mudanças no conteudo encontrado,  não existindo o conteudo, ele adiciona essa nova informação, quando existe, ele altera o documento, mas ainda mantendo os dados antigos para visualização e comparações futuras.

