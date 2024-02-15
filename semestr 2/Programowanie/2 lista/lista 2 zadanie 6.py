def lista(rownanie):
    wynik = []
    liczba = '' 
    for znak in rownanie: #pętlą zapisujemy w liście każdy znak operacji pomijając spacje 
        if znak == '+' or znak == '-' or znak == '*':
            wynik.append(liczba)
            wynik.append(znak)
            liczba = ''
        elif znak == ' ':
            continue
        else:
            liczba += znak
    wynik.append(liczba)
    return wynik

def slupek(rownanie):

    znaki = lista(rownanie) 
    print('{:>20}'.format(znaki[0])) #formatujemy tekst za pomocą wcześniej utworzonej listy aby wynik przedstawiony był w słupku
    print('{}{:>19}'.format(znaki[1], znaki[2]))
    print('-'*20)
    print('{:>20}'.format(round(eval(rownanie), 4)))

slupek('rownanie')