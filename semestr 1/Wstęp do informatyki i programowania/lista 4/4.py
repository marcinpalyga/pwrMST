import math
a = c = 1
result = []
x = int(10**7.4)
y = int(10**8.5)
i = int(math.fabs(y-x)/100)
for b in range(x, y, i):
        x1 = (1/(2*a))*(-b + math.sqrt(b**2 - 4*a*c))
        x2 = (1/(2*a))*(-b - math.sqrt(b**2 - 4*a*c))
        result.append(x1)
        result.append(x2)
print('Pierwsze wzory:')
print(result)
result1 = []
for b in range(x, y, i):                 #dla 100 wartości z przedziału obliczamy wartości x1 i x2 i przedstawiamy w postaci listy
    x1 = (1/(2*a))*(-b - math.sqrt(b**2 - 4*a*c))
    x2 = c/(a*x1)
    result1.append(x1)
    result1.append(x2)
print('Drugie wzory:')
print(result1) #lepiej używać drugich wzorów ze względu na utratę wartości liczb znaczących
