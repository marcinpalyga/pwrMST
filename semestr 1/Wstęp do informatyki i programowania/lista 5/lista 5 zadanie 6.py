def sortowanie(n):
    lista=[]
    if (type(n[0])==str):
        n = n.lower()        
    for char in n: #pętla zamieniająca każdą literę słowa na kod ascii
        x = ord(char)
        lista.append(x) #lista zapisująca każdy kod ascii litery
        for i in range(len(lista)-1): #pętla sprawdzająca czy lista jest posortowana
            if (x>=48 and x<=57) or (x>=65 and x<=90) or (x>=97 and x<=122): #usuwamy znaki specjalne ze słów
                if lista[i]>=lista[i+1]:
                    continue
                else:
                    return False
    return True
                            

print(sortowanie('hEa'))
