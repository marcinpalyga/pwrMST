def fib(n):             #funkcja zwraca wartość ciągu Fibonacciego w zależności od podanego n
    if n == 0:          #dla n = 0 funkcja zwraca 0
        return 0
    elif n == 1:        #dla n = 1 funkcja zwraca 1
        return 1
    else:               #w innych przypadkach(dla n >=2) funkcja zwraca wartość obliczoną według danego wzoru
        return fib(n-2) + fib(n-1)

print(fib(5))
        
