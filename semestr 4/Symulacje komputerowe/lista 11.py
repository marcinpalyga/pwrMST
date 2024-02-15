import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

def motion(times):
    delta_t = np.diff(times)
    results = np.cumsum(np.random.normal(scale=np.sqrt(delta_t), size = len(times)-1))
    results = np.insert(results, 0, 0)
    return results

ts = np.linspace(0, 5, 1000)
# sample = motion(ts)
# plt.plot(sample)
# plt.title('Ruch Browna 1D')
# plt.show()

# samples = [motion(ts) for i in range(2)]
# plt.plot(samples[0], samples[1])
# plt.title('Ruch Browna 2D')
# plt.show()

# samples = [motion(ts) for i in range(3)]
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.plot(samples[0], samples[1], samples[2])
# ax.set_title('Ruch Browna 3D')
# plt.show()


sample = [motion(ts) for i in range(1000)]
variance = np.var(sample, axis=0)
# plt.plot(ts, variance)
# plt.show()

ts = np.linspace(0,1000,1000)
sup = np.sqrt(2*ts*np.log(np.log(ts)))
inf = -np.sqrt(2*ts*np.log(np.log(ts)))
# plt.plot(motion(ts))
# plt.plot(sup)
# plt.plot(inf)
# plt.show()

def gamma_process(times):
    delta_t = np.diff(times)
    results = np.cumsum(np.random.gamma(shape =np.sqrt(delta_t), size = len(times)-1))
    results = np.insert(results, 0, 0)
    return results

ts = np.linspace(0, 5, 1000)
sample = gamma_process(ts)
# plt.plot(sample)
# plt.title('Proces Gamma')
# plt.show()

def var_gamma_process(times):
    delta_t = np.diff(times)
    results = np.cumsum(np.random.normal(loc = 0, scale = np.random.gamma(shape=delta_t), size = len(times)-1))
    results = np.insert(results, 0, 0)
    return results

ts = np.linspace(0, 5, 1000)
sample = var_gamma_process(ts)
# plt.plot(sample)
# plt.title('Proces Variance Gamma')
# plt.show()

def levy_stable_process(times):
    delta_t = np.diff(times)
    results = np.cumsum(st.levy_stable.rvs(2, 0, scale = delta_t**1/2, size = len(times)-1))
    results = np.insert(results, 0, 0)
    return results

ts = np.linspace(0, 5, 1000)
sample = levy_stable_process(ts)
# plt.plot(sample)
# plt.title('Proces stabilny')
# plt.show()