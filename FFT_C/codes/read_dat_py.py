import struct
import matplotlib.pyplot as plt
import numpy as np
#If using termux
import subprocess
import shlex
#end if

N = 8    #N point FFT
f= np.loadtxt("C:\\Users\\tejas\\projects\\codes\\fft_values.dat")
print(type(f))
real_X=f[0::2]
imag_X = f[1::2]
plt.plot(f)
plt.show()
X = np.array(real_X)+1j*np.array(imag_X)
plt.figure(figsize=(7,8))
plt.subplot(2,1,1)
plt.grid()
plt.title("Magnitude Spectrum")
plt.ylabel("|X(k)|")
plt.stem(np.abs(X),use_line_collection=True)


plt.subplot(2,1,2)
plt.grid()
plt.title("Phase Spectrum")
plt.xlabel("k")
plt.ylabel(r'$\angle{H(k)}$')
plt.stem(np.angle(X),use_line_collection=True)
plt.show()
#If using termux
plt.savefig('../figs/fft_c.pdf')
plt.savefig('../figs/fft_c.eps')
#subprocess.run(shlex.split("termux-open ../figs/fft_c.pdf"))
#else
plt.show()
