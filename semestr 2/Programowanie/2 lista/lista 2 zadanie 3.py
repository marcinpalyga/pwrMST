import os
from zipfile import ZipFile
import datetime
print(datetime.date.today())
def zip(sciezka):               
    lista_sciezek = []
    data = str(datetime.date.today())
    nazwa_zip = data + '_' + os.path.basename(sciezka) + '.zip'
    for zrodlo, sciezka, pliki in os.walk(sciezka):   #pętla zapisująca w liście każdy podfolder i plik należący do podanego folderu
        for nazwa_pliku in pliki:
            sciezka_pliku = os.path.join(zrodlo, nazwa_pliku)
            lista_sciezek.append(sciezka_pliku)
    with ZipFile(nazwa_zip, 'w') as zip: #zapisujemy nasz zip z podaną nazwą zawierającą datę zapisania
        for element in lista_sciezek:
            zip.write(element)
    
zip('sciezka')