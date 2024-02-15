import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import cauchy

#Cauchy
def h(x):
    return 1/(1 + x**2)

vals = []
for i in range(100000):
    x = np.random.uniform(0,1)
    y = np.random.uniform(-1,1)
    while x**2 > h(y/x):
        x = np.random.uniform(0,1)
        y = np.random.uniform(-1,1)
    vals.append(y/x)

#x = np.linspace(cauchy.ppf(0.01), cauchy.ppf(0.99), 1000)
#plt.hist(vals, bins=x, density = True)
#plt.plot(x, h(x)/np.pi)
#plt.show()

#Normalny

def g(x):
    return np.e**(-x**2/2)

vals = []
for i in range(100000):
    x = np.random.uniform(0,1)
    y = np.random.uniform(-1,1)
    while x**2 > g(y/x):
        x = np.random.uniform(0,1)
        y = np.random.uniform(-1,1)
    vals.append(y/x)
 
x = np.linspace(-5,5, 1000)
plt.hist(vals, bins=x, density = True)
plt.plot(x, g(x)/np.sqrt(2*np.pi), c='orange')
plt.show()