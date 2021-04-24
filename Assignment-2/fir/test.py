import numpy as np
import matplotlib.pyplot as plt
#If using termux
import subprocess
import shlex
#end if


#THIS PROGRAM FINDS THE FIR COEFFICIENTS FOR A BANDPASS FILTER USING THE
#KAISER WINDOW AND THE DESIGN SPECIFICATIONS

#Filter number
L = 114

#Sampling freqency (kHz)
Fs = 48 

#Constant used to get the normalized digital freqencies
const = 2*np.pi/Fs

#The permissible filter amplitude deviation from unity
delta = 0.15

#Bandpass filter specifications (kHz)

#Passband F_p2 < F_p1
F_p1 = 3 + 0.6*(L-107)
F_p2 = 3 + 0.6*(L-109)

#Transition band
delF = 0.3

#Stopband F_s2 < F_p21 F_p1 < F_s1
F_s1 = F_p1 + 0.3
F_s2 = F_p2 - 0.3

#Normalized digital filter specifications (radians/sec)
omega_p1 = const*F_p1
omega_p2 = const*F_p2

omega_c = (omega_p1+omega_p2)/2
omega_l = (omega_p1-omega_p2)/2

omega_s1 = const*F_s1
omega_s2 = const*F_s2
delomega = 2*np.pi*delF/Fs


#The Kaiser window design
A = -20*np.log10(delta)
N = np.ceil((A-8)/(4.57*delomega))
#N = np.ceil(0.9222*np.pi/delomega)

N = 100
n = np.arange(-N,N+1)
hlp = np.sin(n*omega_l)/(n*np.pi)
hlp[N] = omega_l/np.pi

#The Bandpass filter
hbp = 2*hlp*np.cos(n*omega_c)

#The lowpass filter plot
omega = np.arange(-np.pi/2,np.pi/200+np.pi/2,np.pi/200)

Hlp = np.abs(np.polyval(hlp,np.exp(-1j*omega)))
plt.figure(1)
plt.plot(omega/np.pi,Hlp)
plt.xlabel('$\omega/\pi$')
plt.ylabel('$|H_{lp}(\omega)|$')
plt.savefig('../figs/fir/lowpass.pdf')
plt.savefig('../figs/fir/lowpass.eps')
#plt.show()

#abs(polyval(hlp,exp(-j*0.015*pi)))

#The bandpass filter plot
omega = np.arange(-np.pi/2,np.pi/200+np.pi/2,np.pi/200)

Hbp = np.abs(np.polyval(hbp,np.exp(-1j*omega)))
plt.figure(2)
plt.plot(omega/np.pi,Hbp)
plt.xlabel('$\omega/\pi$')
plt.ylabel('$|H_{bp}(\omega)|$')
plt.savefig('../figs/fir/bandpass.pdf')
plt.savefig('../figs/fir/bandpass.eps')
#plt.show()

fir_coeff = hbp
#print(fir_coeff)

np.savetxt('fir_coeff.dat',fir_coeff,delimiter=',')
