def win_to_unix(sciezka):
    koniec_win = b'\r\n'  #zapisujemy koncowki linii windowsa i unixa w systemie bitowym
    koniec_unix = b'\n'
    with open(sciezka, 'rb') as plik: #otwieramy podany plik
        tekst = plik.read()

    zmiana = tekst.replace(koniec_win, koniec_unix) #zamieniamy koncowki linii w pliku i go zapisujemy
    with open(sciezka, 'wb') as plik:
        plik.write(zmiana)

win_to_unix( "sciezka" )

def unix_to_win(sciezka):  #druga funkcja dziala analogicznie do pierwszej
    koniec_win = b'\r\n'
    koniec_unix = b'\n'
    with open(sciezka, 'rb') as plik:
        tekst = plik.read()

    zmiana = tekst.replace(koniec_unix, koniec_win)
    with open(sciezka, 'wb') as plik:
        plik.write(zmiana)

unix_to_win( "sciezka" )

