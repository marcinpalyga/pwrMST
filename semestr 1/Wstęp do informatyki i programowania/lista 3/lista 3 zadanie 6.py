import math

def newton(n, k):
    return int((math.factorial(n))/(math.factorial(k)*math.factorial(n-k)))   #funckja licząca dwumian Newtona


def pascal(row):
    result = []
    for i in range(row):            #w zależności od od rzędu trojkąta Pascala funkcja liczy kolejne dwumiany Newtona w rzędzie i zapisuje w zmiennej
        number = []
        for j in range(i + 1):
            number.append(newton(i, j))
        result.append(number)
    return result

print(pascal(10))
