from bs4 import BeautifulSoup
import requests
import time

page = requests.get("https://empregacampinas.com.br/?s=marketing")
soup = BeautifulSoup(page.content, 'html.parser')
lista = []
lista_aux = [0]

for link in soup.find_all("a", {"class": "thumbnail"}):
    lista.append(link.get('href'))

for links in lista:
    print(links)

print('o primeiro item da lista é: ', lista[0])
print("o tamanho da lista completa é: ", len(lista))

while True:
    if lista_aux[0] != lista[0]:
        print('há atualização')
        lista_aux.append(lista[0])
        time.sleep(15000)