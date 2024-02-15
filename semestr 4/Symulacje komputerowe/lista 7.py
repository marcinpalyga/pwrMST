import numpy as np
import matplotlib.pyplot as plt

def lam_f(t, lam=2):
    return lam*t 

#zad 1
def poisson(T, lam):
    results = []
    t = 0
    lmax = lam_f(T)
    while t <= T:
        t += np.random.exponential(1/lmax)
        u = np.random.uniform()
        while lmax * u >= lam_f(t):
            t += np.random.exponential(1/lmax)
            u = np.random.uniform()
        results.append(t)
    return results

results= poisson(10, 2)
x_axis = np.linspace(0,10)
ys = [i for i in range(0, len(results)-1)]
for i in range(0, len(results)-1):
    x = np.linspace(results[i], results[i+1], 10)
    y = np.linspace(ys[i], ys[i], 10)
    plt.plot(x, y, c='blue')
plt.plot(x_axis, x_axis**2, c='black')
plt.xlabel('t')
plt.ylabel('N_t')
plt.show()

#zad 2
def m_t(t, lam):
    return lam*t 

def inv_poisson(T, lam):
    results = np.array([0])
    N = np.random.poisson(m_t(T, lam))
    u = np.random.uniform(size=N)
    results = np.append(results, u*T)
    return sorted(results)

results= inv_poisson(10, 2)
x_axis = np.linspace(0,10)
ys = [i for i in range(0, len(results)-1)]
for i in range(0, len(results)-1):
    x = np.linspace(results[i], results[i+1], 10)
    y = np.linspace(ys[i], ys[i], 10)
    plt.plot(x, y, c='blue')
plt.plot(x_axis, 2*x_axis, c='black')
plt.xlabel('t')
plt.ylabel('N_t')
plt.show()

#zad 3
def sum_poisson(pois_1, pois_2):
    return sorted(pois_1 + pois_2)
# results = sum_poisson(poisson(10, 2), poisson(10, 2)) 
# x_axis = np.linspace(0,10)
# ys = [i for i in range(0, len(results)-1)]
# for i in range(0, len(results)-1):
#     x = np.linspace(results[i], results[i+1], 10)
#     y = np.linspace(ys[i], ys[i], 10)
#     plt.plot(x, y, c='blue')
# plt.plot(x_axis, 2*x_axis**2, c='black')
# plt.xlabel('t')
# plt.ylabel('N_t')
# plt.show()

#zad 4
def mark_poisson(T, lam):
    nt = poisson(T, lam)
    marker = np.random.choice([1,2], size = len(nt), p=[0.7,0.3])
    nt_1 = np.array(nt)[marker == 1]
    nt_2 = np.array(nt)[marker == 2]
    return nt, nt_1, nt_2


# res_1, res_2, res_3 = mark_poisson(10, 1)
# x_axis = np.linspace(0,10)
# ys = [i for i in range(0, len(res_1)-1)]
# for i in range(0, len(res_1)-1):
#     x = np.linspace(res_1[i], res_1[i+1], 10)
#     y = np.linspace(ys[i], ys[i], 10)
#     plt.plot(x, y, c='blue')
# plt.plot(x_axis, x_axis**2, c='black')
# plt.xlabel('t')
# plt.ylabel('N_t')
# plt.show()

# ys = [i for i in range(0, len(res_2)-1)]
# for i in range(0, len(res_2)-1):
#     x = np.linspace(res_2[i], res_2[i+1], 10)
#     y = np.linspace(ys[i], ys[i], 10)
#     plt.plot(x, y, c='blue')
# plt.plot(x_axis, 0.7*x_axis**2, c='black')
# plt.xlabel('t')
# plt.ylabel('N_t')
# plt.show()

# ys = [i for i in range(0, len(res_3)-1)]
# for i in range(0, len(res_3)-1):
#     x = np.linspace(res_3[i], res_3[i+1], 10)
#     y = np.linspace(ys[i], ys[i], 10)
#     plt.plot(x, y, c='blue')
# plt.plot(x_axis, 0.3*x_axis**2, c='black')
# plt.xlabel('t')
# plt.ylabel('N_t')
# plt.show()