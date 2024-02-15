import time

def fibr(n): #funkcja rekurencyjnie licząca ciąg fibonacciego i zwracają listę n wyrazów
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibr(n-2) + fibr(n-1)
def lista(n):
    lista = []
    for i in range(0, n+1):
        lista.append(fibr(i))
    return lista
print(lista(30))
    
start = time.time() #liczymy czas wykonania funkcji
fibr(30)
end = time.time()
time = end - start
print(time) 
