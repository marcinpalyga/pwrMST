import matplotlib.pyplot as plt
import numpy as np

#zadanie 1
#zbior{1,...,10}
lamb = 10
omega = np.array([i+1 for i in range(10)])
n_omega = np.random.poisson(lam = lamb*len(omega))
p_values = np.random.choice(omega, size=n_omega)
x_axis = np.array([i for i in range(len(p_values))])

# plt.scatter(x_axis, p_values)
# plt.show()

#sześcian
a = 4
n_omega = np.random.poisson(lam = lamb*a**3)
axes = [np.random.uniform(low = 0, high = a, size = n_omega) for i in range(3)]

# fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
# ax.scatter(axes[0], axes[1], axes[2])
# plt.show()

#koło
r = 3
lamb = 50
n_omega = np.random.poisson(lam = lamb*np.pi*r**2)
xs = np.empty(n_omega)
ys = np.empty(n_omega)
for i in range(n_omega):
    x = np.random.uniform(low = -r, high = r)
    y = np.random.uniform(low = -r, high = r)
    while x**2 + y**2 > r**2:
        x = np.random.uniform(low = -r, high = r)
        y = np.random.uniform(low = -r, high = r)
    xs[i] = x
    ys[i] = y

# fig, ax = plt.subplots()
# ax.set_aspect('equal')
# ax.scatter(xs,ys, s=5)
# plt.show()

#zadanie 2
r=2
def lamb_func(lamb, x):
    return lamb*np.exp(-1*np.abs(x)**2)
lamb = 400
lamb_max = lamb
n_t = np.random.poisson(lamb_max*np.pi*r**2)
xs = np.empty(n_t)
ys = np.empty(n_t)
distances = np.empty(n_t)
for i in range(n_t):
    x = np.random.uniform(low = -r, high = r)
    y = np.random.uniform(low = -r, high = r)
    while x**2 + y**2 > r**2:
        x = np.random.uniform(low = -r, high = r)
        y = np.random.uniform(low = -r, high = r)
    xs[i] = x
    ys[i] = y
    distances[i] = np.sqrt(x**2+y**2)
    
thinning = [np.random.uniform()*lamb_max <= lamb_func(lamb, dist) for dist in distances]
x_axis = xs[thinning]
y_axis = ys[thinning]

# fig, ax = plt.subplots()
# ax.set_aspect('equal')
# ax.scatter(x_axis,y_axis, s=5)
# plt.show()

#zadanie 3

r = 0.3
lamb = 500
x = np.random.uniform(-1+r, 1-r)
y = np.random.uniform(-1+r, 1-r)
while x**2 + y**2 > (1-r)**2:
    x = np.random.uniform(-1+r, 1-r)
    y = np.random.uniform(-1+r, 1-r)
n_omega = np.random.poisson(lamb*np.pi*r**2)
xs = np.empty(n_omega)
ys = np.empty(n_omega)
for i in range(n_omega):
    X = np.random.uniform(-r, r)
    Y = np.random.uniform(-r, r)
    while X**2 + Y**2 > r**2:
        X = np.random.uniform(-r, r)
        Y = np.random.uniform(-r, r)
    xs[i] = X+x
    ys[i] = Y+y

# t = np.linspace(0, 2*np.pi, 100)
# fig, ax = plt.subplots()
# ax.set_aspect('equal')
# ax.scatter(xs,ys, s=5)
# ax.plot(np.cos(t), np.sin(t))
# plt.show()