import numpy as np
import matplotlib.pyplot as plt
input=np.array([1,2,3,4,4,3,2,1])
y=np.fft.fft(input)

plt.figure(figsize=(7,8))
plt.subplot(2,1,1)
plt.grid()
plt.title("Magnitude Spectrum")
plt.ylabel("|X(k)|")
plt.stem(np.abs(y),use_line_collection=True)


plt.subplot(2,1,2)
plt.grid()
plt.title("Phase Spectrum")
plt.xlabel("k")
plt.ylabel(r'$\angle{H(k)}$')
plt.stem(np.angle(y),use_line_collection=True)
plt.show()
