import random
import matplotlib.pyplot as plt
import math 
def dyski():
    '''Funkcja odpowiedzialna za zapisanie 100 dysków o promieniu 0.5 do listy, gdzie współrzędne są losowo wybierane z zakresu(-14.5,14.5)'''
    lista = []
    for i in range(100):
        dysk = [random.uniform(-14.5, 14.5), random.uniform(-14.5, 14.5), 0.5]
        lista.append(dysk)
    return lista
def wykres(lista):
    '''Funkcja reprezentująca dyski na wykresie'''
    for i in range(len(lista)):
        dysk = plt.Circle((lista[i][0], lista[i][1]), lista[i][2])
        plt.gca().add_patch(dysk)
    plt.xticks((-15, 15))
    plt.yticks((-15, 15))
    plt.grid()
    plt.title('Kolizja dysków')
    plt.show()

def wykrywanie_kolizji(lista):
    '''Funkcja wykrywa kolizję między parami dysków i zapisuje pary w liście'''
    lista1 = []
    for i in lista:
        for u in lista:
            if u != i:
                odl = ((i[0]-u[0])**2 + (i[1]-u[1])**2)**0.5
                if odl < 1:
                    lista1.append([i, u])
    return True, lista1
    
def przesun(dysk, wektor):
    '''Funkcja przesuwa dany dysk o podany wektor'''
    dysk[0] = dysk[0] + wektor[0]
    dysk[1] = dysk[1] + wektor[1]
    return dysk

def rozsuwanie_dyskow(lista):
    '''Funkcja wykrywająca kolizję dysków i rozsuwająca je w sposób zależny od ich położenia'''
    control = 0
    while control < 10**6:
        for i in lista:
            for u in lista:
                    odl = ((u[0]-i[0])**2 + (u[1]-i[1])**2)**0.5
                    if odl < 1 and u != i:
                        if i[0] > 14: #kiedy dyski kolidują ze sobą na skraju wykresu przesuwamy jeden z nich do środka
                            przesun(u, [-1,0])
                        elif i[0] < -14:
                            przesun(u, [1,0])
                        elif i[1] > 14:
                            przesun(u, [0,-1])
                        elif i[1] < -14:
                            przesun(u, [0,1])
                        elif abs(i[0]) <= 14 and abs(i[1]) <= 14 and abs(u[0]) <= 14 and abs(u[1]) <= 14: #kiedy dyski znajdują się w środku wykres rozsuwamy je w przeciwne strony
                            if u[0] > i[0]:
                                przesun(u, [0.5, 0])
                                przesun(i, [-0.5, 0])
                            else:
                                przesun(i, [0.5, 0])
                                przesun(u, [-0.5, 0])
            
                    else:
                        control += 1
    return lista
                    
print(wykres(dyski()))
print(wykrywanie_kolizji(dyski()))
print(wykres(rozsuwanie_dyskow(dyski())))
