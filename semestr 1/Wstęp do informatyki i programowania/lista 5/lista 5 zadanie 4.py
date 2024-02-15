import time

def fibi(n): #funkcja iteracyjnie licząca ciąg fibonacciego i zwracająca listę n wyrazów
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
    return a
def lista(n):
    lista = []
    for i in range(0, n+1):
        lista.append(fibi(i))
    return lista
print(lista(30))

start = time.time() #liczymy czas wykonania funkcji
fibi(30)
end = time.time()
time = end - start
print(time)

