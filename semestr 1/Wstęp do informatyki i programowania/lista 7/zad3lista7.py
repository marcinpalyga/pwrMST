from zad1lista7 import Rocket
import random

def lista(n):

    rakiety = []
    
    for i in range(n):
        rakiety.append(Rocket(random.uniform(-10, 10), random.uniform(-10, 10)))

    return rakiety

def main():

    flota = lista(5)
    for rakieta in flota:
        print(f'Pozycja rakiety nr {flota.index(rakieta) + 1} : {rakieta.pozycja()}')

    while True:

        index = int(input('Podaj numer statku, który chcesz wybrać (1-5): '))
        xwektor = random.uniform(-5,5)
        ywektor = random.uniform(-5,5)
        print(f'Losowy wektor przez który statek będzie przesuwany {xwektor}, {ywektor}')

        flota[index - 1].przesun(xwektor, ywektor)

        for rakieta in flota:
            print(f'\nPozycja rakiety nr {flota.index(rakieta) + 1} : {rakieta.pozycja()}')
            for rakieta in flota[flota.index(rakieta) + 1:]:
                 print(f'Odległość rakiety nr {flota.index(rakieta)} do rakiety nr {flota.index(rakieta) + 1} wynosi: {rakieta.dystans(rakieta)}')
        

if __name__ == '__main__':
    main()

