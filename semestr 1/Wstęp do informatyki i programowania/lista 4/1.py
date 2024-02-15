print(7/100*100-7)                 #sprawdzamy wynik tego działania

def blad(i):
    result = []
    for i in range(1, i+1):        #funkcja tworzy pętle gdzie po kolei sprawdza wynik działania dla każdej liczby naturalnej
        if i/100*100-i != 0:
            result.append(i)       #jeśli wynik działania nie jest równy 0 liczba zostaje dodana do wcześniej utworzonej listy   
    return result
print(blad(100))
