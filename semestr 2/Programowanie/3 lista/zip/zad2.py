# Zadanie 2 Lista 2


###### SPOSÓB WYWOŁANIA PROGRAMU
#   python zad2.py (ścieżka wejściowa) (ścieżka wyjściowa) (szerokość miniatury) (wysokość miniatury)
##### WSZYSTKIE ŚCIEŻKI NALEŻY PODAĆ Z PODWÓJNYMI NAWIASAMI (C:\\example zamiast C:\example)


from PIL import Image
import sys


def generate_miniature(input_path: str, output_path: str, width: int, height: int) -> None:

    # Opens given image. Thrwos an error if is given incorrect path
    try:
        image = Image.open(input_path)
    except OSError as err:
        print(err)
        return

    # Creating miniature
    image.thumbnail((width, height))

    # Saves miniature. Thrwos an error if is given incorrect path
    try:
        image.save(output_path)
    except OSError as err:
        print(err)

def main():

    # # Checks whether given number of arguments is not 5
    # if len(sys.argv) != 5:
    #     print(f'Given incorrect number of arguments. Expected 5, given {len(sys.argv)}')

    generate_miniature(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))


main()