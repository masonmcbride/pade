from math import factorial
from itertools import product
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import pade

"""Establish constants: dt, X = [0,..,2], e^X = [exp(0),...,exp(2)]"""
dt = 0.001
X = np.arange(0,2,dt)
e_X = np.exp(X)

"""Pade approximants"""

# c_n = f(a)/n! for expansion centered at a. a=0, so e^a = 1
Ω = product(range(5),range(5))
taylor_coeffs = [1./factorial(n) for n in range(10)]
pade = {(m,n):pade(taylor_coeffs,m,n) for (m,n) in Ω}

"""Plot that shit"""
fig = plt.figure()
fig.suptitle("Padé Approximants of e^x for (m, n) in Ω=[0,4]x[0,4]")
plt.plot(X, e_X, label='y = exp(x)')
for (m,n),(P,Q) in list(pade.items())[20:25]:
    print(f"{(m,n)} {P,Q=}")
    p_mnX = [P(x)/Q(x) for x in X]
    plt.plot(X, p_mnX, label=fr'$Pade({m},{n})_*X$')
plt.xlabel('x',fontsize=20)
plt.ylabel('f(x)',fontsize=20)
plt.legend()
plt.show()