import matplotlib.pyplot as plt
import math

def silnia(n):
    if n < 2:                            #funkcja rekurencyjnie opisująca silnię
        return 1
    else:
        return n * silnia(n-1)

def suma(x,n):                            #funkcja licząca n-tą sumę częściową danego x
    lista=[]
    for i in range(0, n+1):               #dla każdego n w podanym zakresie pętla oblicza wynik działania
        a = x**i/silnia(i)
        lista.append(a)                   #wynik zostaje zapisany we wcześniej utworzonej liście
    czesciowa = 0
    for a in lista:
        czesciowa += a                    #każda liczba z listy zostaje zsumowana i funkcja zwraca nam wynik
    return czesciowa

def blad(x, n):                            #funkcja licząca błąd względny według wzoru
    b = math.fabs(math.exp(x)-suma(x, n))/math.exp(x)
    return b
def bladlista(x, n):                    #funkcja zapisująca błąd względny danego x aby utworzyć oś Y na wykresie
    lista1=[]
    for n in range(0, n+1):
        c = math.fabs(math.exp(x)-suma(x, n))/math.exp(x)
        lista1.append(c)
    return lista1

osx = list(range(0,61))


print('Dla x=2 suma częściowa i błąd względny wynoszą: ')
print(suma(2,60))
print(blad(2, 60))
plt.plot(osx, bladlista(2,60))
plt.ylabel('Błąd względny')
plt.xlabel('N')
plt.title('x=2')
plt.show()

print('Dla x=-2 suma częściowa i błąd względny wynoszą: ')
print(suma(-2,60))
print(blad(-2, 60))
plt.plot(osx, bladlista(-2,60))
plt.ylabel('Błąd względny')
plt.xlabel('N')
plt.title('x=-2')
plt.show()


print('Dla x=10 suma częściowa i błąd względny wynoszą: ')
print(suma(10,60))
print(blad(10, 60))
plt.plot(osx, bladlista(10,60))
plt.ylabel('Błąd względny')
plt.xlabel('N')
plt.title('x=10')
plt.show()


print('Dla x=-10 suma częściowa i błąd względny wynoszą: ')
print(suma(-10,60))
print(blad(-10, 60))
plt.plot(osx, bladlista(-10,60))
plt.ylabel('Błąd względny')
plt.xlabel('N')
plt.title('x=-10')
plt.show()


plt.plot(osx, bladlista(2,60),label = str(2))
plt.plot(osx, bladlista(-2,60),label = str(-2))
plt.plot(osx, bladlista(10,60), label = str(10))
plt.plot(osx, bladlista(-10,60), label = str(-10))
plt.ylabel('Błąd względny')
plt.xlabel('N')
plt.legend()
plt.yscale('log')
plt.show()


