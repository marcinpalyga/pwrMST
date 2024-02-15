from scipy.integrate import odeint
import numpy as np 
import matplotlib.pyplot as plt
import sys

def seir(N, S0, E0, I0, R0, beta, sigma, gamma): 
    def func(y, t, beta, sigma, gamma):
        S, E, I, R = y
        N = S + E + I + R 
        dSdt = -(float(beta)*S*I)/N
        dEdt = (float(beta)*S*I)/N - float(sigma)*E
        dIdt = float(sigma)*E - float(gamma)*I
        dRdt = float(gamma)*I
        dy = [dSdt, dEdt, dIdt, dRdt]
        return dy

    beta0 = float(beta)  
    sigma0 = float(sigma)
    gamma0 = float(gamma)

    for i in range(3): 
        y0 = [S0, E0, I0, R0] 
        t = np.linspace(0, 100, 200) 
        seir = odeint(func, y0, t, args=(beta0, sigma0, gamma0)) 
        plt.plot(t, seir)
        plt.xlabel('Czas')
        plt.ylabel('Liczebność grupy')
        plt.show() 
        plt.clf()
        beta0 += 1 
    beta0 = float(beta)
    
    for i in range(3): 
        y0 = [S0, E0, I0, R0] 
        t = np.linspace(0, 100, 200) 
        seir = odeint(func, y0, t, args=(beta0, sigma0, gamma0)) 
        plt.plot(t, seir)
        plt.xlabel('Czas')
        plt.ylabel('Liczebność grupy')
        plt.show() 
        plt.clf()
        sigma0 += 0.3 
    sigma0 = float(sigma) 

    for i in range(3): 
        y0 = [S0, E0, I0, R0] 
        t = np.linspace(0, 100, 200) 
        seir = odeint(func, y0, t, args=(beta0, sigma0, gamma0)) 
        plt.plot(t, seir)
        plt.xlabel('Czas')
        plt.ylabel('Liczebność grupy')
        plt.show()
        plt.clf()
        gamma0 += 0.3 
    gamma0 = float(gamma) 


if __name__ == '__main__':
    seir(*sys.argv[1:]) 

