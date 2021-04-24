  
import numpy as np  
import matplotlib.pyplot as plt

N = 4
for eps in np.arange(0.35,0.6,0.05): 
    Omega1 = np.arange(0,1,0.01)
    H1 = 1/np.sqrt(1 + eps**2*np.cos(N*np.arccos(Omega1))**2)
    Omega2 = np.arange(1,3.01,0.01) # 0:0.01:2
    H2 = 1/np.sqrt(1 + epsilon**2*np.cosh(N*np.arccosh(Omega2))**2)
    H = np.concatenate((H1,H2))
    Omega = np.concatenate((Omega1,Omega2))
    plt.plot(Omega,H)
plt.legend()
plt.savefig("vary_epsilon.eps")
plt.show()
