## WebScraping Python + BS4 + Telegram telepot  ![Badge](https://img.shields.io/badge/Python-BS4-%237159c1?style=for-the-badge&logo=ghost)
 scraping que realiza busca por nova incidência de vaga. Para cada nova vaga postada, ao se atualizar o timer, uma mensagem com o link da vaga é mandado via telegram.

### Dependências 

- python == 3+
- beautifulsoup4==4.10.0


### Como rodar:

- Siga os passos da documentação do python-telegram-bot para geração do ID: https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot
- instale o BeautifulSoup4 através do comando: pip install beautifulsoup4 
- é necessário ter o python instalado em sua máquina, bem como um debbuger para interpretar o código. 


### URLs para seleção:

- o script funciona através da URL de busca dos respectivos sites. Portanto, é necessário que este passo seja feito corretamente. 

Para o site 'Emprega Campinas': 
- na barra de pesquisa, insira a palavra chave para a busca. ex: 'produção'
- em seguida, copie a URL da página atual
- adicione no campo 'page', entre as aspas (" ")

Para o site 'Vagas.com': 
- na barra de pesquisa, insira a palavra chave + a cidade para a busca. ex: 'produção' 'campinas'
- em seguida, copie a URL da página atual
- adicione no campo 'page', entre as aspas (" ")



Projeto independente open-source desenvolvido em Python 3 com Linux Ubuntu 20.0
