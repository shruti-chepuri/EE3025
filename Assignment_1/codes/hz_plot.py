import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches

#If using termux
import subprocess
import shlex
#end if


# Plot the complex z-plane given zeros and poles

z= np.array([-1j,1j])
p= np.array([-0.5,0])

ax = plt.subplot(111)
# Addzero axes    
plt.axvline(0)
plt.axhline(0)

# Plot the zeros and poles
zeros = plt.plot(z.real, z.imag, 'o',color='black')
poles = plt.plot(p.real, p.imag, 'x',color='black')

unit_circle = patches.Circle((0,0), radius=1, fill=False,color='black', ls='dashed')
ax.add_patch(unit_circle)
             
x = np.linspace(-2,2,100)  
    
#Coloring the Roc      
y1 = np.sqrt(16-x**2)
y2 = -np.sqrt(16-x**2)
plt.fill_between(x, y1, y2, color='#cd970e')
    
boundary = patches.Circle((0,0), radius=0.5, fill=False,color='black')
ax.add_patch(boundary)
roc = patches.Circle((0,0), radius=0.5,color='white', ls='solid')
ax.add_patch(roc)

plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))
plt.title("H(z)")
plt.text(0,0.1,"z=0")
plt.text(0.6,0,"|z|>0.5")
plt.text(0,1.1,"z=1j")
plt.text(0,-1.1,"z=-1j")
plt.text(-0.6,-0.2,"z=-0.5")

#if using termux
plt.savefig('../figs/z_plane.pdf')
plt.savefig('../figs/z_plane.eps')
subprocess.run(shlex.split("termux-open ../figs/z_plane.pdf"))
#end if
#plt.show()
