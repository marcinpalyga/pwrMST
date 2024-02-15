import os
from zipfile import ZipFile
import datetime
import time
def zip(sciezka, rozszerzenie):
    str_sciezka = str(sciezka)           
    data = str(datetime.date.today())   #zapisujemy dzisiejsza date
    os.mkdir('c:\\copy-' + data)   #tworzymy folder z podana nazwa
    lista = []
    nazwa = data + '_' + os.path.basename(sciezka) + '.zip'  #tworzymy nazwe zipu  
    for root, sciezka, pliki in os.walk(sciezka):        #petla w ktorej zapisujemy kazdy plik z podanym rozszerzeniem i czasem od ostatniej modyfikacji krotszym niz 3 dni do listy
        for plik in pliki:
            nazwa_pliku, rozszerzenie_pliku = os.path.splitext(plik) #zmienna zapisujaca rozszerzenie kazdego pliku z podanej sciezki
            os.chdir(str_sciezka)
            czas_zmiany = os.path.getmtime(plik)   #zmienne zapisujace czas modyfikacji  i czas lokalny
            czas_teraz = time.mktime(time.localtime())
            roznica = round(czas_teraz - czas_zmiany) 
            if rozszerzenie_pliku == rozszerzenie and roznica < 259200: #warunek ograniczajacy zapisywanie plikow w zipie
                sciezka_pliku = os.path.join(root, plik)
                lista.append(sciezka_pliku)
    os.chdir('c:\\copy-' + data) #zmiana sciezki aby zip zrobil sie w odpowiednim folderze
    with ZipFile(nazwa, 'w') as zip:  #zapisujemy zip
        for element in lista:
            zip.write(element)
zip('sciezka', 'rozszerzenie')


