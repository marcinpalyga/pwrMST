import argparse
from scipy.integrate import odeint
import numpy as np 
import matplotlib.pyplot as plt

def init_argparse():                      
    parser = argparse.ArgumentParser()
    parser.add_argument('-N', type=int, default=1000)  
    parser.add_argument('-S0', type=int, default=999)
    parser.add_argument('-E0', type=int, default=1)  
    parser.add_argument('-I0', type=int, default=0)
    parser.add_argument('-R0', type=int, default=0)
    parser.add_argument('-beta', type=float, default=1.34)
    parser.add_argument('-sigma', type=float, default=0.19)
    parser.add_argument('-gamma', type=float, default=0.34)
    return parser

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
    y0 = [S0, E0, I0, R0]
    t = np.linspace(0, 100, 200)
    seir = odeint(func, y0, t, args=(float(beta), float(sigma), float(gamma)))
    plt.plot(t, seir)
    plt.xlabel('Czas')
    plt.ylabel('Liczebność grupy')
    plt.show()
    plt.clf()

if __name__ == '__main__':
    args = init_argparse().parse_args()
    seir(**vars(args)) 
    
