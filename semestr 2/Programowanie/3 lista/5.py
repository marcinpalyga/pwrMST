def nawiasy():
    otwierajace = ['[', '{', '(', '<']  #tworzymy listy mozliwych nawiasow otwierajacych i zamykajacych
    zamykajace = [']', '}', ')', '>']
    lista = []
    wyrazenie = input("Podaj wyrazenie: ")    #podajemy nasze wyrazenie jako input z klawiatury uzytkownika
    for element in wyrazenie:
        if element in otwierajace:    #w petli dla kazdego elementu wyrazenia zapisujemy je w zaleznosci od tego czy jest to nawias otwierajacy czy zamykajacy
            lista.append(element)       #jesli jest to nawias otwierajacy to dodajemy go do listy
        elif element in zamykajace:
            if len(lista) > 0 and otwierajace[zamykajace.index(element)] == lista[-1]:
                lista.pop()  #jesli jest to nawias zamykajacy sprawdzamy czy w liscie znajduja sie inne wyrazenia i porownujemy nasz nawias z ostatnim elementem z listy
            else:
                return 'Wyrazenie nie jest poprawne' #jesli nawias otwierajacy i zamykajacy ktore znajduja sie obok siebie nie sa takie same to wyrazenie nie jest poprawne
    if len(lista) == 0: #jesli udalo nam sie wyrzucic kazdy nawias otwierajacy i nie ma wiecej elementow w wyrazeniu to jest ono poprawne
        return 'Wyrazenie jest poprawne'
    else:
        return 'Wyrazenie nie jest poprawne' #jesli zostal jakis nawias otwierajacy to wyrazenie nie jest poprawne

print(nawiasy())