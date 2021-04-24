import numpy as np
#If using termux
import subprocess
import shlex
#end if

def lattice(c,v):
  u=np.flip(v)
  m=len(v)
  K=v
  C=c
  while( m>1 and K[m-2]!=1):
    c-=C[m-1]*u
    v= (v-K[m-2]*u)/(1-K[m-2]**2)
    m-=1
    v= v[:m]
    c= c[:m]
    u=np.flip(v)

    if m>1 :
      K[m-2]=v[m-1]
  return C,K
c = np.array([0, 0.44, 0.36, 0.02])
v = np.array([1, 0.4, 0.18, -0.2])
#print(lattice(c,v))
