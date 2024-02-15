import matplotlib.pyplot as plt
import numpy as np

# zadanie 1
# rozkład normalny
def characteristic(theta, x):
    values = np.sum(np.exp(1j*theta*x))
    return values/len(x)

N=1000
t = np.linspace(-4,4,N)
sample = np.random.normal(loc=2, size=N)
empirical = []
for value in t:
    empirical.append(characteristic(value, sample))
theoretical = np.exp(2j*t- 0.5*t**2) 

# plt.plot(t, np.real(empirical), label = 'Empiryczna wartość')
# plt.plot(t, np.real(theoretical), label = 'Teoretyczna wartość')
# plt.legend()
# plt.title('Część rzeczywista funkcji charakterystycznej')
# plt.show()

# plt.plot(t, np.imag(empirical), label = 'Empiryczna wartość')
# plt.plot(t, np.imag(theoretical), label = 'Teoretyczna wartość')
# plt.legend()
# plt.title('Część urojona funkcji charakterystycznej')
# plt.show()


#Exp(2)

N=1000
t = np.linspace(-4,4,N)
sample = np.random.exponential(scale=0.5, size=N)
empirical = []
for value in t:
    empirical.append(characteristic(value, sample))
theoretical = 2/(2-1j*t) 

# plt.plot(t, np.real(empirical), label = 'Empiryczna wartość')
# plt.plot(t, np.real(theoretical), label = 'Teoretyczna wartość')
# plt.legend()
# plt.title('Część rzeczywista funkcji charakterystycznej')
# plt.show()

# plt.plot(t, np.imag(empirical), label = 'Empiryczna wartość')
# plt.plot(t, np.imag(theoretical), label = 'Teoretyczna wartość')
# plt.legend()
# plt.title('Część urojona funkcji charakterystycznej')
# plt.show()

# zadanie 2
# N(0,1)
lam = 100
ns = np.random.poisson(lam)
value = 0
times = []
for i in range(ns):
    value += np.random.exponential(scale=lam)
    times.append(value)

ys = []
value = 0
for i in range(ns):
    value += np.random.normal()
    ys.append(value)

# plt.step(times, ys)
# plt.title('Złożony proces Poissona')
# plt.show()

# C(0,1)
lam = 100
ns = np.random.poisson(lam)
value = 0
times = []
for i in range(ns):
    value += np.random.exponential(scale=lam)
    times.append(value)

ys = []
value = 0
for i in range(ns):
    value += np.random.standard_cauchy()
    ys.append(value)

# plt.step(times, ys)
# plt.title('Złożony proces Poissona')
# plt.show()

#zadanie 3
def process(T=10):
    results = np.array([0])
    lam = 1
    t = 0
    while t <= T:
        u = np.random.uniform(0,1)
        t = t - np.log(u)/lam
        results = np.append(results, t)
    return results

intervals = process()
def risk_process(T, intervals, u=5, c=0.5, lam=1):
    times = np.linspace(0, T, 1000)
    damages = np.random.uniform(np.random.exponential(scale = lam, size = len(intervals)))
    idxs = []
    for time in intervals:
        for t in times:
            if time<t:
                idxs.append(list(times).index(t))
                break
    income = c*times
    damage_idx = list(zip(damages, idxs))
    for damage, idx in damage_idx:
        income[idx:] -= damage
    values = u + income
    return times, values

ts, ys = risk_process(10, intervals)

plt.plot(ts, ys)
plt.xlabel('t')
plt.ylabel('Kapitał')
plt.title('Proces ryzyka')
plt.show()

def risk(T, u=5, c=0.5, lam=1):
    result = 0
    for i in range(1000):
        intervals = process(T=T)
        times, values = risk_process(T, intervals)
        if np.any(values<0):
            result += 1
    return result/1000

bankrupcy = []
for t in [1,3,5]:
    bankrupcy.append(risk(t))
print(f'Ryzyko niewypłacalności w czasie 1: {bankrupcy[0]}')
print(f'Ryzyko niewypłacalności w czasie 3: {bankrupcy[1]}')
print(f'Ryzyko niewypłacalności w czasie 5: {bankrupcy[2]}')


