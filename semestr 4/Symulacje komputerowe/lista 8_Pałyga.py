import numpy as np
import matplotlib.pyplot as plt

#zadanie 1
n=100
results = np.empty(n)
x0 = 0
p_matrix = np.array([[0.1, 0.2, 0.7],[0.5, 0.2, 0.3],[0.3, 0.4, 0.3]])
for i in range(n):
    results[i] = x0
    p_values = p_matrix[x0]
    x0 = np.random.choice([0,1,2], p = p_values)


x_axis = np.linspace(0, 100, 101)
plt.ylim(-0.1, 2.1)
plt.xlabel('t')
plt.title('Łańcuch Markowa w czasie dyskretnym')
plt.stairs(results, x_axis)
plt.show()

#zadanie 2
N = 25
times = np.empty(N)
t = 0
results = np.empty(N)
p_matrix = np.array([[0.1, 0.2, 0.7],[0.5, 0.2, 0.3],[0.3, 0.4, 0.3]])
lam_matrix = np.array([1,2,0.5])
x0 = 0
for i in range(N):
    t += np.random.exponential(lam_matrix[x0])
    times[i] = t
    results[i] = x0
    p_values = p_matrix[x0]
    x0 = np.random.choice([0,1,2], p = p_values)

times = np.append(times, times[-1])
plt.ylim(-0.1, 2.1)
plt.title('Łańcuch Markowa w czasie ciągłym')
plt.ylabel('t')
plt.stairs(results, times)
plt.show()