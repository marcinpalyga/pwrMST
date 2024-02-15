import cv2 as cv
from PIL import Image
import qrcode

def generator(strona):
    qr = qrcode.QRCode()
    qr.add_data(strona)    #tworzymy kod qr z podanej strony
    qr.make(fit = True)
    kod = qr.make_image()
    kod.save("qrcode.jpg")  #zapisujemy kod na dysku
    obraz = Image.open('sciezka do kodu qr') #pokazujemy wytworzony kod qr
    obraz.show()

generator('strona')

def czytnik(image):
    qr = cv.imread(image)   #odczytujemy kod qr
    czytnik_qr = cv.QRCodeDetector()    
    strona, tablica, kod = czytnik_qr.detectAndDecode(qr)   #z funkcji zwracajacej trzy zmienne zapisujemy link strony i go wyswietlamy
    print("Zakodowana strona to: " + strona)

czytnik('sciezka do kodu qr')