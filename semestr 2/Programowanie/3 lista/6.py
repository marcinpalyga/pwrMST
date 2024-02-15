import webbrowser
from bs4 import BeautifulSoup
import requests

def wikipedia():
    strona = requests.get('https://en.wikipedia.org/wiki/Special:Random') #losujemy strone
    zawartosc = strona.content #zapisujemy jej zawartosc w zmiennej
    link = strona.url #zapisujemy url wylosowanej strony
    soup = BeautifulSoup(zawartosc, 'html.parser') 
    tytul = str(soup.find_all('title')) #z zawartosci wyszukujemy tytulu strony
    print(tytul)
    odp = input("Czy lubisz tytul strony? ").upper() #sprawdzamy czy tytul podoba sie uzytkownikowi
    if odp == 'Y':  #jesli tytul sie podoba wyswietlamy strone
        webbrowser.open(link)
    else: #jesli tytul sie nie podoba funkcja wywoluje sie po raz kolejny
        wikipedia()
wikipedia()