import matplotlib.pyplot as plt
import numpy as np
import time

#Zadanie 1
C_alfa = 4
alfa = 3

def p(x):
    return C_alfa*x**alfa

vals = []
for i in range(100000):
    u1 = np.random.uniform(0,1)
    u2 = np.random.uniform(0, C_alfa)
    while u2 > p(u1):
        u1 = np.random.uniform(0,1)
        u2 = np.random.uniform(0,C_alfa)
    vals.append(u1)


x = np.linspace(0,1, 100)
#plt.hist(vals, bins=1000, density=True)
#plt.plot(x,p(x))
#plt.show()

#zadanie 2
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

C = 1

def p(x):
    return C*np.sin(x)

start = time.perf_counter()
vals = []
for i in range(100000):
    u1 = np.random.uniform(0,np.pi/2)
    u2 = np.random.uniform(0, C)
    while u2 > p(u1):
        u1 = np.random.uniform(0,np.pi/2)
        u2 = np.random.uniform(0, C)
    vals.append(u1)
end = time.perf_counter()

#print(end-start)
#x = np.linspace(0,np.pi/2, 100)
#plt.hist(vals, bins=1000, density=True)
#plt.plot(x,p(x))
#plt.show()

C = 1 
def p(x):
    return C*np.sin(np.sqrt(x))/(2*np.sqrt(x))

start = time.perf_counter()
vals = []
for i in range(100000):
    u1 = np.random.uniform(0,(np.pi/2)**2)
    u2 = np.random.uniform(0, C)
    while u2 > p(u1):
        u1 = np.random.uniform(0,(np.pi/2)**2)
        u2 = np.random.uniform(0, C)
    vals.append(np.sqrt(u1))
end = time.perf_counter()

#print(end-start)
#x = np.linspace(0,np.pi/2, 100)
#plt.hist(vals, bins=1000, density=True)
#plt.plot(x, np.sin(x))
#plt.show()

#zadanie 3
C = np.sqrt(2*np.pi//np.e)

def p(x):
    return 2/(np.sqrt(2*np.pi))*np.exp(-x**2/2)
def g(x):
    return np.e**(-x)

vals = []
for i in range(100000):
    u1 = np.random.exponential(1)
    u2 = np.random.uniform(0, C)
    while C * u2 * g(u1) > p(u1):
        u1 = np.random.exponential(1)
        u2 = np.random.uniform(0, C)
    vals.append(u1)

x = np.linspace(0,4, 100)
plt.hist(vals, bins=1000, density=True)
plt.plot(x,p(x))
plt.show()