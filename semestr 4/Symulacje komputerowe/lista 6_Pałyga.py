import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson


def process():
    results = np.array([0])
    lam = 2
    T = 4
    t = 0
    i = 0
    while t <= T:
        u = np.random.uniform(0,1)
        t = t - np.log(u)/lam
        results = np.append(results, t)
        i += 1
    return results, i-1

results, values = process()
ys = [i for i in range(0, len(results)-1)]
for i in range(0, len(results)-1):
    x = np.linspace(results[i], results[i+1], 10)
    y = np.linspace(ys[i], ys[i], 10)
    plt.plot(x, y, c='r')

plt.title('Proces Poissona')
plt.xlabel('t')
plt.ylabel('N(t)')
plt.show()

def dist():
    values = np.empty(10000)
    for i in range(10000):
        results, ns = process()
        values[i] = ns
    return values

data = dist()
r = poisson.rvs(2*4, size=10000)
fig, ax = plt.subplots(1, 2, figsize= (14, 3))
ax[0].hist(data, bins='sqrt', density=True, label= 'Histogram wartości procesu Poissona')
ax[0].legend()
ax[1].hist(r, bins='sqrt', density = True, label='Rozkład Poissona')
ax[1].legend()
plt.show()