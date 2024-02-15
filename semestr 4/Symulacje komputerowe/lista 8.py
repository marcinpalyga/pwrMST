import numpy as np
import matplotlib.pyplot as plt

#zadanie 1

def markow_d(states=6):
    results = np.empty(50)
    x0 = 0
    prob_matrix = []
    for i in range(states):
        arr = np.random.random(states)
        prob_matrix.append(arr/arr.sum())
    prob_matrix=np.asarray(prob_matrix)
    for i in range(50):
        results[i] = x0
        ps = prob_matrix[x0]
        x0 = np.random.choice([i for i in range(states)], p = ps)
    return results

# results = markow_d()
# x_axis = np.linspace(0, 50, 51)
# plt.ylim(-0.1, 5.1)
# plt.ylabel('t')
# plt.stairs(results, x_axis)
# plt.show()

#zadanie 2
def markow_c(states=4):
    times = np.empty(30)
    t = 0
    x0 = 0
    prob_matrix = []
    results = np.empty(30)
    for i in range(states):
        arr = np.random.random(states)
        prob_matrix.append(arr/arr.sum())
    prob_matrix=np.asarray(prob_matrix)
    lambdas = np.array(np.random.randint(0, 4, size = states))
    for i in range(30):
        t += np.random.exponential(lambdas[x0])
        times[i] = t
        results[i] = x0
        ps = prob_matrix[x0]
        x0 = np.random.choice([i for i in range(states)], p = ps)
    return results, times

# results, times = markow_c()
# times = np.append(times, times[-1])
# plt.ylim(-0.1, 3.1)
# plt.ylabel('t')
# plt.stairs(results, times)
# plt.show()