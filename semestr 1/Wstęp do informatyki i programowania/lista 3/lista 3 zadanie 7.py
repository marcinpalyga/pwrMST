import math
a = float(input('Podaj współczynnik a funkcji kwadratowej: '))
b = float(input('Podaj współczynnik b funkcji kwadratowej: '))
c = float(input('Podaj współczynnik c funkcji kwadratowej: '))


def kwadratowa(a, b, c):
    delta = float(b**2 - 4*a*c)                          #zmienna która zapisuje deltę
    if a == 0:
        return 'To jest funkcja liniowa'                #przypadek kiedy funkcja nie jest kwadratowa
    elif delta < 0:
        return 'Delta ujemna, funkcja nie ma pierwiastków rzeczywistych'    #przypadek kiedy funkcja nie ma pierwiastków
    elif delta > 0:
        return float((-b + math.sqrt(delta))/(2*a)), float((-b - math.sqrt(delta))/(2*a))  #funkcja zwraca wartości pierwiastków
    elif delta == 0:
        return 'Funkcja ma pierwiastek podwójny równy', float((-b - math.sqrt(delta))/(2*a))
    
print(kwadratowa(a, b, c))
