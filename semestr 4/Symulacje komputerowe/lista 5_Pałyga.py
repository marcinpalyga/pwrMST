import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
import time

#Zadanie 1 Box-Muller
start = time.perf_counter()
u1 = np.random.uniform(0,1, size = 5000)
u2 = np.random.uniform(0,1, size = 5000)
xs = np.sqrt(-2*np.log(u1))*np.cos(2*np.pi*u2)
ys = np.sqrt(-2*np.log(u1))*np.sin(2*np.pi*u2)
end = time.perf_counter()
print(f'Czas metody Boxa-Mullera: {end-start}')
#plt.hist2d(xs, ys, bins = 50, cmap='jet', density=True)
#plt.title('Histogram 2D')
#plt.colorbar()
#plt.show()

#x = np.linspace(-5,5,500)
#fig, ax = plt.subplots(1, 2, figsize = (6,3))
#ax[0].hist(xs, bins = 20, density = True)
#ax[0].plot(x, norm.pdf(x), c='red')
#ax[0].set_title('Gęstość zmiennej X')
#ax[1].hist(ys, bins = 20, density = True)
#ax[1].plot(x, norm.pdf(x), c='red')
#ax[1].set_title('Gęstość zmiennej Y')
#plt.show()

#Zadanie 1 Marsaglia
xs = []
ys = []
start = time.perf_counter()
for i in range(5000):
    v1 = np.random.uniform(-1,1)
    v2 = np.random.uniform(-1,1)
    r2 = v1**2 + v2**2
    while r2>1:
        v1 = np.random.uniform(-1,1)
        v2 = np.random.uniform(-1,1)
        r2 = v1**2 + v2**2
    xs.append(np.sqrt((-2*np.log(r2))/r2)*v1)
    ys.append(np.sqrt((-2*np.log(r2))/r2)*v2)
end = time.perf_counter()
print(f'Czas metody Marsaglii: {end-start}')

#plt.hist2d(xs, ys, bins = 50, cmap='jet', density=True)
#plt.title('Histogram 2D')
#plt.colorbar()
#plt.show()
#x = np.linspace(-5,5,500)
#fig, ax = plt.subplots(1, 2, figsize=(8,3))
#ax[0].hist(xs, bins = 20, density = True)
#ax[0].plot(x, norm.pdf(x), c='red')
#ax[0].set_title('Gęstość zmiennej X')
#ax[1].hist(ys, bins = 20, density = True)
#ax[1].plot(x, norm.pdf(x), c='red')
#ax[1].set_title('Gęstość zmiennej Y')
#plt.show() 

#zadanie 2 2D
from scipy.linalg import cholesky
cov_matrix = np.array([[1, 0.5], [0.5, 2]])
A = cholesky(cov_matrix, lower=False)
Z = np.random.normal(loc=0, scale=1, size=(10**5, 2))
X = Z @ A
# plt.hist2d(X[:,0], X[:,1], bins = 50, cmap='jet', density = True)
# plt.colorbar()
# x = np.linspace(-5,5,500)
# fig, ax = plt.subplots(1, 2, figsize=(8,3))
# ax[0].hist(X[:,0], bins = 20, density = True)
# ax[0].plot(x, norm.pdf(x,scale = np.sqrt(cov_matrix[0,0])), c='red')
# ax[0].set_title('Gęstość zmiennej X')
# ax[1].hist(X[:,1], bins = 20, density = True)
# ax[1].plot(x, norm.pdf(x,scale = np.sqrt(cov_matrix[1,1])), c='red')
# ax[1].set_title('Gęstość zmiennej Y')
# plt.show()


#zadanie 2 3D
cov_matrix = np.array([[25,15,-5], [15,18,0], [-5,0,11]])
A = cholesky(cov_matrix, lower=False)
Z = np.random.normal(loc=0, scale=1, size=(10**5, 3))
X = Z @ A
# plt.scatter(X[:,0], X[:,1], X[:,2])
# x = np.linspace(-20,20,500)
# fig, ax = plt.subplots(1, 3, figsize=(8,3))
# ax[0].hist(X[:,0], bins = 20, density = True)
# ax[0].plot(x, norm.pdf(x, scale = np.sqrt(cov_matrix[0,0])), c='red')
# ax[0].set_title('Gęstość zmiennej X')
# ax[1].hist(X[:,1], bins = 20, density = True)
# ax[1].plot(x, norm.pdf(x, scale = np.sqrt(cov_matrix[1,1])), c='red')
# ax[1].set_title('Gęstość zmiennej Y')
# ax[2].hist(X[:,2], bins = 20, density = True)
# ax[2].plot(x, norm.pdf(x, scale = np.sqrt(cov_matrix[2,2])), c='red')
# ax[2].set_title('Gęstość zmiennej Z')
# plt.show()
