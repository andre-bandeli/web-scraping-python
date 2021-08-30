from bs4 import BeautifulSoup
import requests

page = requests.get("https://empregacampinas.com.br/?s=marketing")
soup = BeautifulSoup(page.content, 'html.parser')
lista = []

for link in soup.find_all("a", {"class": "thumbnail"}):
    lista.append(link.get('href'))

for links in lista:
    print(links)
        



print("o tamanho da lista completa é: ", len(lista))

