import random
import matplotlib.pyplot as plt
import math 
def disc():
    '''prezentacja dysków jak listę list, gdzie współrzędna x i y są losowo wybierane tak aby nie wypadły poza wykres '''
    lista = []
    for i in range(100):
        dysk = [random.uniform(-14.5, 14.5), random.uniform(-14.5, 14.5), 0.5]
        lista.append(dysk)
    return lista
def plot(lista):
    ''' funkcja która odpowiada za naniesienie 100 dysków na płaszczyznę '''
    for elem in range(len(lista)):
        dysk = plt.Circle((lista[elem][0], lista[elem][1]), lista[elem][2])
        plt.gca().add_patch(dysk)
    plt.xticks((-15, 15))
    plt.yticks((-15, 15))
    plt.grid()
    plt.show()

def collision(lista):
    ''' funkcja wykrywająca kolizje między dyskami i zapisująca te kolizje w liście'''
    lista1 = []
    for elem in lista:
        for el in lista:
            if el != elem:
                odl = ((elem[0]-el[0])**2 + (elem[1]-el[1])**2)**0.5
                if odl < 1:
                    lista1.append([elem, el])
    return lista1
    
def move(dysk, wektor):
    ''' funkcja przesuwająca pojedynczy dysk o podany wektor '''
    dysk[0] = dysk[0] + wektor[0]
    dysk[1] = dysk[1] + wektor[1]
    return dysk

def split(lista):
    ''' funkcja która po wykryciu kolizji przesuwa je w zależności od ich współrzędnych '''
    zakres = 0
    while zakres < 10**6:
        for i in lista:
            for u in lista:
                    odl = ((u[0]-i[0])**2 + (u[1]-i[1])**2)**0.5
                    if odl < 1 and u != i:
                        if i[0] > 14: #przypadki gdy dyski znajdują się przy granicach wykresów, przesuwamy wtedy drugi z dysków do środka wykresu 
                            move(u, [-1,0])
                        elif i[0] < -14:
                            move(u, [1,0])
                        elif i[1] > 14:
                            move(u, [0,-1])
                        elif i[1] < -14:
                            move(u, [0,1])
                        elif abs(i[0]) <= 14 and abs(i[1]) <= 14 and abs(u[0]) <= 14 and abs(u[1]) <= 14: #przypadki gdy dyski znajdują na tyle daleko od granicy, że nie grozi wypadnięcie poza wykres
                            if u[0] > i[0]:
                                move(u, [0.5, 0])
                                move(i, [-0.5, 0])
                            else:
                                move(i, [0.5, 0])
                                move(u, [-0.5, 0])
            
                    else:
                        zakres += 1
    return lista
                    
print(plot(disc()))
print(collision(disc()))
print(plot(split(disc())))
