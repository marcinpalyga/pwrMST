from PIL import Image

def miniatura(sciezka, nazwa_miniatury, rozmiar):

    original_rozmiar = list(Image.open(sciezka).size)
    if rozmiar[0] < original_rozmiar[0] and rozmiar[1] < original_rozmiar[1]: #sprawdzamy czy rozmiar obrazka jest większy od rozmiaru miniatury
        thumbnail = Image.open(sciezka).resize(tuple(rozmiar))  #zmieniamy rozmiar obrazka na podany dla miniatury
        thumbnail.save(nazwa_miniatury, "JPEG")
        Image.open(sciezka).show()
        Image.open(nazwa_miniatury).show()
    else:
        print("Rozmiar miniatury jest większy niż oryginału")


miniatura('sciezka', 'nazwa_miniatury', [100, 100])