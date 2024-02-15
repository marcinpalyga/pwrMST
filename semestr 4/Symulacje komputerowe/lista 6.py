import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

def poisson_process(lam = 3, T = 10):
    times = np.array([0])
    t = 0
    I = 0
    while t <= T:
        U = np.random.uniform()
        t = t - 1/lam * np.log(U)
        I += 1
        times = np.append(times, t)
    ys = [i for i in range(len(times))]
    for i in range(len(times)-1):
        t = np.linspace(times[i], times[i+1])
        y = np.linspace(ys[i], ys[i])
        plt.plot(t, y, c='black')
    plt.xlabel('t')
    plt.ylabel('N(t)')
    plt.title('Realizacja procesu Poissona')
    plt.show()

def pois_dist(lam = 3, T = 5, n=10000):
    vals = np.empty(n)
    for i in range(n):
        t = 0
        I = 0
        while t <= T:
            U = np.random.uniform()
            t = t - 1/lam * np.log(U)
            I += 1
        vals[i] = I
    fig, ax = plt.subplots(1, 2, figsize= (14, 5))
    ax[0].hist(vals, bins='sqrt', density=True, label= 'Histogram wartości procesu Poissona', color='r')
    ax[1].hist(poisson.rvs(lam*T, size=10000), bins='sqrt', density = True, label='Rozkład Poissona', color='black')
    fig.legend(loc='outside upper right')
    plt.show()
    
poisson_process()
pois_dist()