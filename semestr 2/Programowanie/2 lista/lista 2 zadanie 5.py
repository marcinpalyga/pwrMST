from PIL import Image


def znakwodny(oryginal_nazwa, znak_wodny_nazwa, nowy, rozmiar):

    oryginal = Image.open(oryginal_nazwa)        #otwieramy obrazek i znak wodny
    znak_wodny = Image.open(znak_wodny_nazwa)
    znak_wodny_rozmiar = znak_wodny.resize(rozmiar)        #nadajemy obu obrazom ten sam wymiar
    oryginal_rozmiar = oryginal.resize(rozmiar)
    blend = Image.blend(oryginal_rozmiar, znak_wodny_rozmiar, 0.45)  #łączymy oba obrazy gdzie ostatni parametr funkcji to stała, od której zależy przezroczytość znaku wodnego
    blend.save(nowy, "JPEG")   
    Image.open(oryginal_nazwa).show()
    Image.open(nowy).show()


znakwodny("oryginal_nazwa","znak_wodny_nazwa","nowy",(500, 500))