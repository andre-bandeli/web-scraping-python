from bs4 import BeautifulSoup
import requests
import time
#import telepot

#bot_chatID = 'your id'
#bot = telepot.Bot('your code')

page = requests.get("https://empregacampinas.com.br/?s=marketing")
soup = BeautifulSoup(page.content, 'html.parser')
lista = []
lista_aux = [0]

def get_equals(str1, str2):
    str1 = lista[0]
    str2 = lista_aux[0]
    if str1 == str2:
        return True


while True:
    for link in soup.find_all("a", {"class": "thumbnail"}):
        lista.append(link.get('href'))

    last_url = lista[0]
    new_url = lista_aux[0]
    a = get_equals(last_url, new_url)
    if a != True:
        for links in lista:
            #bot.sendMessage(1142090567, links)
            lista_aux[0] = lista[0]
            print(links)
    #time.sleep(15)

