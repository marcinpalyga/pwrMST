import random
import matplotlib.pyplot as plt
import math

a = -14.5
b = 14.5
lista = []

def Tworzenie_dysku(a,b):
    """ Zaprezentowałem dyski za pomocą listy zagnieżdżonej,
    wybieramy losowe współrzędne dysków z zakresu w ten sposób, aby
    nie wyleciały poza płaszczyznę"""
    for i in range(100):
        lista.append([random.uniform(a,b),random.uniform(a,b),0.5])
    return lista

def Rysowanie_dysków(lista):
    """ Tworzymy wykres na który nanoszą sie dyski """
    for a in range(len(lista)):
        circle = plt.Circle((lista[a][0],lista[a][1]),lista[a][2])
        plt.gca().add_patch(circle)
    plt.xlim(-15,15)
    plt.ylim(-15,15)
    plt.show()

def Znajdowanie_kolizji(lista):
    """Gdy odległość między dwoma środkami dysków jest mniejsza od 1,
    mamy kolizję, więc do listy przypisujemy numery dysków, które mają kolizję"""
    lista2 = []
    for i in range(len(lista)):
        for u in range(len(lista)):
            if math.sqrt((lista[u][0] - lista[i][0]) ** 2 + (lista[u][1] - lista[i][1]) ** 2) < 1 and i != u:
                lista2.append(['kolizja',i,u])
    return True, lista2

def Rozsuwanie_o_wektor(lista):
    for i in range(len(lista)):
        a = input("Podaj wektor")
        lista[i] += a

def Rozsuwanie_kolizji(lista):
    """Dla każdego z poniższych przypadków tworzymy wersję rozsuwania dysków"""
    control = 0
    while control < 10**6:
        for i in range(len(lista)):
            for u in range(len(lista)):
                if math.sqrt((lista[u][0] - lista[i][0]) ** 2 + (lista[u][1] - lista[i][1]) ** 2) < 1 and i != u:
                    print('kolizja',i,u)
                    #gdy obydwa w środku:
                    if abs(lista[i][0]) <= 13.5 and abs(lista[i][1]) <= 13.5 and abs(lista[u][0]) <= 13.5 and abs(lista[u][1]) <= 13.5:
                        if lista[u][0] > lista[i][0]:
                            lista[u][0]+= 0.5
                            lista[i][0]-= 0.5
                        else:
                            lista[u][0]-= 0.5
                            lista[i][0]+= 0.5

                #gdy jeden w środku a drugi na zewnątrz:
                    elif abs(lista[i][0]) > 13.5 and abs(lista[u][0]) < 13.5:
                        if lista[u][0] > 0:
                            lista[u][0] -= 1
                        else:
                            lista[u][0] += 1
                    elif abs(lista[i][1]) > 13.5 and abs(lista[u][1]) < 13.5:
                        if lista[u][1] > 0:
                            lista[u][1] -= 1
                        else:
                            lista[u][1] += 1
                    elif abs(lista[u][0]) > 13.5 and abs(lista[i][0]) < 13.5:
                        if lista[i][0] > 0:
                            lista[i][0] -= 1
                        else:
                            lista[i][0] += 1
                    elif abs(lista[u][1]) > 13.5 and abs(lista[i][1]) < 13.5:
                        if lista[i][1] > 0:
                            lista[i][1] -= 1
                        else:
                            lista[i][1] += 1
                    #gdy dwa na zewnątrz

                    elif lista[i][1] > 13.5:
                        lista[u][1] -= 1
                    elif lista[i][1] < -13.5:
                        lista[u][1] += 1
                    elif lista[i][0] > 13.5:
                        lista[u][0] -= 1
                    elif lista[i][0] < -13.5:
                        lista[u][0] += 1
                else:
                    control += 1
    return lista
lista = Tworzenie_dysku(a,b)
print(lista)
print(Rysowanie_dysków(lista))
print(Znajdowanie_kolizji(lista))
print(Rozsuwanie_kolizji(lista))
print(Rysowanie_dysków(lista))


def split(lista):
    zakres = 0
    while zakres < 10**6:
        for i in range(len(lista)):
            for u in range(len(lista)):
                    odl = ((lista[u][0]-lista[i][0])**2 + (lista[u][1]-lista[i][1])**2)**0.5
                    if odl < 1:
                        if abs(lista[i][0]) <= 13.5 and abs(lista[i][1]) <= 13.5 and abs(lista[u][0]) <= 13.5 and abs(lista[u][1]) <= 13.5:
                            if lista[u][0] > lista[i][0]:
                                lista[u][0]+= 0.5
                                lista[i][0]-= 0.5
                            else:
                                lista[u][0]-= 0.5
                                lista[i][0]+= 0.5

                    #gdy jeden w środku a drugi na zewnątrz:
                        elif abs(lista[i][0]) > 13.5 and abs(lista[u][0]) < 13.5:
                            if lista[u][0] > 0:
                                lista[u][0] -= 1
                            else:
                                lista[u][0] += 1
                        elif abs(lista[i][1]) > 13.5 and abs(lista[u][1]) < 13.5:
                            if lista[u][1] > 0:
                                lista[u][1] -= 1
                            else:
                                lista[u][1] += 1
                        elif abs(lista[u][0]) > 13.5 and abs(lista[i][0]) < 13.5:
                            if lista[i][0] > 0:
                                lista[i][0] -= 1
                            else:
                                lista[i][0] += 1
                        elif abs(lista[u][1]) > 13.5 and abs(lista[i][1]) < 13.5:
                            if lista[i][1] > 0:
                                lista[i][1] -= 1
                            else:
                                lista[i][1] += 1
                        #gdy dwa na zewnątrz

                        elif lista[i][1] > 13.5:
                            lista[u][1] -= 1
                        elif lista[i][1] < -13.5:
                            lista[u][1] += 1
                        elif lista[i][0] > 13.5:
                            lista[u][0] -= 1
                        elif lista[i][0] < -13.5:
                            lista[u][0] += 1
                    else:
                        zakres += 1
    return lista




def split(lista):
    ''' funkcja która po wykryciu kolizji przesuwa je w zależności od ich współrzędnych '''
    zakres = 0
    while zakres < 10**6:
        for i in lista:
            for u in lista:
                    odl = ((u[0]-i[0])**2 + (u[1]-i[1])**2)**0.5
                    if odl < 1 and u != i:
                        if i[0] > 14.5: #przypadki gdy dyski znajdują się przy granicach wykresów, przesuwamy wtedy drugi z dysków do środka wykresu 
                            u[0] -= 1
                        elif i[0] < -14.5:
                            u[0] += 1
                        elif i[1] > 14.5:
                            u[1] -= 1
                        elif i[1] < -14.5:
                            u[1] += 1
                        elif abs(i[0]) <= 14.5 and abs(i[1]) <= 14.5 and abs(u[0]) <= 14.5 and abs(u[1]) <= 14.5: #przypadki gdy dyski znajdują na tyle daleko od granicy, że nie grozi wypadnięcie poza wykres
                            if u[0] > i[0]:
                                u[0]+= 0.5
                                i[0]-= 0.5
                            else:
                                u[0]-= 0.5
                                i[0]+= 0.5
            
                    else:
                        zakres += 1
    return lista
