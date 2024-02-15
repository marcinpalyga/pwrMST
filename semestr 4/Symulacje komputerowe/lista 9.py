import numpy as np
import matplotlib.pyplot as plt

#zadanie 1

def meas_set(lam = 10):
    omega = np.array([1,2,3,4,5,6,7,8,9,10])
    N = np.random.poisson(lam*len(omega))
    measure = np.random.choice(omega, size = N)
    return measure

# y = meas_set()
# x = range(y.size)
# plt.scatter(x,y)
# plt.show()

def meas_cube(lam = 100):
    omega = 2 
    N = np.random.poisson(lam*omega**3)
    x = np.random.uniform(0, omega, size = N)
    y = np.random.uniform(0, omega, size = N)
    z = np.random.uniform(0, omega, size = N)
    return x, y, z

# x,y,z = meas_cube()
# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.scatter(x,y,z)
# plt.show()

def meas_circ(lam = 100):
    r = 2
    N = np.random.poisson(lam*np.pi*r**2)
    xs = np.empty(N)
    ys = np.empty(N)
    for i in range(N):
        x, y = np.random.uniform(-r , r, size = 2)
        while x**2+y**2>r**2:
            x, y = np.random.uniform(-r , r, size = 2)
        xs[i] = x
        ys[i] = y
    return xs,ys

# xs, ys = meas_circ()
# plt.scatter(xs,ys)
# plt.show()

#zadanie 2
def func(x, lam = 100):
    return lam*np.exp(-np.abs(x)**2)

def thin_meas(lam = 100, r = 3):
    lam_max = lam
    N = np.random.poisson(lam_max*np.pi*r**2)
    xs = np.empty(N)
    ys = np.empty(N)
    for i in range(N):
        x, y = np.random.uniform(-r , r, size = 2)
        while x**2+y**2>r**2:
            x, y = np.random.uniform(-r , r, size = 2)
        if np.random.uniform()*lam_max <= func(np.sqrt(x**2+y**2)):
            xs[i] = x
            ys[i] = y
    return xs, ys

xs, ys = thin_meas()
plt.scatter(xs,ys)
plt.show()

def rand_meas(lam = 500, r=0.3):
    x, y = np.random.uniform(r-1, 1-r, size = 2)
    while x**2+y**2>r**2:
        x, y = np.random.uniform(r-1, 1-r, size = 2)
    N = np.random.poisson(lam*np.pi*r**2)
    xs = np.empty(N)
    ys = np.empty(N)
    for i in range(N):
        x1, y1 = np.random.uniform(-r, r, size=2)
        while x1**2+y1**2>r**2:
            x1, y1 = np.random.uniform(-r, r, size=2)
        xs[i] = x+x1
        ys[i] = y+y1
    return xs, ys

# xs, ys = rand_meas()
# plt.scatter(xs,ys)
# plt.xlim(-1,1)
# plt.ylim(-1,1)
# plt.show()