def anagram(a, b):
    lista1=[] 
    lista2=[]
    for i in a: #pętla dopisująca do pierwszej listy wszystkie litery słowa
        lista1.append(i)
    for k in b: #pętla dopisująca do drugiej listy wszystkie litery słowa
        lista2.append(k)
    lista1.sort() #sortujemy obie listy
    lista2.sort()
    if lista1==lista2: #jeśli listy są takie same to słowa są anagramami
        return 'Słowa są anagramami'
    else:
        return 'Słowa nie są anagramami'
print(anagram('mataaa','taama'))
