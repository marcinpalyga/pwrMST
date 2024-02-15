def nwd_lista(l):
    def nwd(a, b):                 #funkcja która oblicza NWD dwóch liczb
        while b:
            a, b = b, a%b
        return a
    n =1
    f = l[0]
    while n != len(l):           #pętla która sprawdza NWD kolejnych par w liście
        f = nwd(f,l[n])
        if  f == 1:
            return 1
        else:
            n = n + 1          
    return f

l = [24,6,4, 12]
print(nwd_lista(l))
