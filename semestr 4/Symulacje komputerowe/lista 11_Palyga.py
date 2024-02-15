import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

#zadanie 1
def brownian(n, t):
    x0 = 0
    times = np.linspace(0, t, n)
    dt = np.diff(times)
    results = np.array([x0])
    for t in dt:
        x0 += np.random.normal(scale=np.sqrt(t))
        results = np.append(results, x0)
    return results

#1D
trajectory = brownian(1000, 10)
# plt.plot(trajectory)
# plt.title('Ruch Browna 1D')
# plt.show()

#2D
trajectories = [brownian(1000, 10) for i in range(2)]

# plt.plot(trajectories[0], trajectories[1])
# plt.title('Ruch Browna 2D')
# plt.show()

#3D
trajectories = [brownian(1000, 10) for i in range(3)]

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.set_title('Ruch Browna 3D')
# ax.plot(trajectories[0], trajectories[1], trajectories[2])
# plt.show()

#zadanie 2
vals = [brownian(1000,10) for i in range(1000)]
results = np.var(vals, axis=0)

# plt.plot(range(10), results[::100])
# plt.xlabel('t')
# plt.ylabel('E[X^2]')
# plt.show()

#zadanie 3
times = np.linspace(0, 10000, 10000)
lim = np.sqrt(2*times*np.log(np.log(times)))

# plt.plot(brownian(10000,10000))
# plt.plot(lim)
# plt.plot(-lim)
# plt.show()

#zadanie 4
#proces gamma

x0 = 0
t = 100
n = 1000
times = np.linspace(0, t, n)
dt = np.diff(times)
results = np.array([x0])
for t in dt:
    x0 += np.random.gamma(shape=t, scale=1)
    results = np.append(results, x0)

# plt.plot(times, results)
# plt.title('Proces Gamma')
# plt.show()

#variance gamma

x0 = 0
t = 100
n = 1000
times = np.linspace(0, t, n)
dt = np.diff(times)
results = np.array([x0])
for t in dt:
    x0 += np.random.normal(loc= 0, scale = np.random.gamma(shape=t, scale=1))
    results = np.append(results, x0)

plt.plot(times, results)
plt.title('Proces Variance Gamma')
plt.show()

#stabilny symetryczny

x0 = 0
t = 100
n = 1000
times = np.linspace(0, t, n)
dt = np.diff(times)
results = np.array([x0])
for t in dt:
    x0 += st.levy_stable.rvs(2, 0, scale = t**(1/2))
    results = np.append(results, x0)

plt.plot(times, results)
plt.title(r'Proces stabilny, $\alpha$ = 2')
plt.show()