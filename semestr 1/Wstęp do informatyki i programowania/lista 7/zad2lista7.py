from zad1lista7 import Rocket

def main():

    rakieta = Rocket(10, 10)

    for x, y in zip(range(5), range(5)):
        rakieta.przesun(x + 1, -y - 1)
        print(f'Pozycja statku po przesunięciu: {rakieta.pozycja()}')

if __name__ == '__main__':
    main()
