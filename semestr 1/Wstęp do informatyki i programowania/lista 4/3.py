import math

def drugi_wzor(x, y):
    z2 = y * math.sqrt((x/y)**2 + 1)    #obliczamy wartość wyrażenia używając obu wzorów
    return z2
print(drugi_wzor(9.8**201, 10.2**199))
def pierwszy_wzor(x, y):
    z1 = math.sqrt(x**2+y**2)
    return z1
print(pierwszy_wzor(9.8**201, 10.2**199))
    #lepiej korzystać z drugiego wzoru ponieważ przy pierwszym python wyrzuca błąd

