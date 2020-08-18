# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 16:46:41 2020
Quantum Mechanics in Python
Source: https://github.com/mholtrop/QMPython/blob/master/Solving_the_Schrodinger_Equation_Numerically.ipynb
@author: Rakesh
"""

import numpy as np
import matplotlib.pyplot as plt

def rd(dim, off, s=1.):
    return s*np.diag(np.ones(dim), off)


N = 128
p = 2*np.pi

x = np.linspace(0,p, N)

h = x[1]-x[0]

y = np.sin(x)

z = np.zeros_like(x)

plt.figure(figsize=(10,7))

dn = rd(N, 0, -1.)
dnm = rd(N-1, 1)

Md = 1./h*(dn + dnm)
yp = Md.dot(y)
plt.plot(x[:-1],yp[:-1])
plt.plot(x,z)
plt.show()

Mdd = (1./(h*h))*(rd(N-1, -1) + rd(N, 0, -2.) + rd(N-1, 1))
ypp = Mdd.dot(y)
plt.plot(x[1:-1],ypp[1:-1])
plt.show()