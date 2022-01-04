# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 20:45:36 2021

@author: Ethan
"""

#The majority of equations and basic code outline was leveraged from the lecture
#notes provided by the professor

import math
import numpy as np
import scipy.integrate as integ
import matplotlib.pyplot as plt
from gekko import GEKKO


# 1 - Numerical Integration - HIC

# Code primarily leveraged from:
#   https://www.intmath.com/applications-integration/hic-part2.php

def H(t):
    d = 50
    h_1 = lambda t: ((22000/(((t-74)**2)+500)))
    h_2, err = integ.quad(h_1, t, t+d)
    HIC = (d*((1/d)*h_2)**2.5)/1000
    return HIC

xv = [t for t  in range(160)]
yv = [H(t) for t  in xv]
plt.figure()
plt.title("Mercedes Benz Airbag")
plt.xlabel("time (ms)")
plt.ylabel("HIC")
plt.plot(xv,yv)

print('\n#1: Numerical Integration - HIC')
print('\nPlot showing HIC value under plots in Python!')


# 2 - Numerical Integration - Work

# Code primarily leveraged from:
#   https://www.intmath.com/applications-integration/8-electric-charges.php

a = 1*10**(-12)
b = 4*10**(-12)
k = 9*10**(9)
q1 = 1.6*10**(-19)
q2 = q1

print('\n\n#2: Numerical Integration - Work')
print("\nThe Expected result is 1.728E-16 J\n")

x_1 = lambda x:((k*q1*q2)/(x**2))
x_2, err = integ.quad(x_1, a, b)
print('Python result is')
print(x_2)


# 3 - Differential Equation - RLC

# Code primarily leveraged from:
#   https://dwightreid.com/blog/education-2/differential-equations-python/second-order-differential-equations-python/

def RLC(A,t):
    Vc,x=A
    V = 1
    R = 10
    L = 78e-9
    C = 3e-9
    res = np.array([x,(V-Vc-(x*R*C))/(L*C)])
    return res

time = np.linspace(0,0.6e-6,1000)
vc,x = integ.odeint(RLC,[0,0],time).T
i=1e-9*x
plt.figure()
plt.title('Voltage Source')
plt.plot(time,vc)
plt.xlabel('t')
plt.ylabel('Vc')
plt.show()

print('\n\n#3: Differential Equation - RLC')
print('\nPlot showing voltage source result in plots in Python!')


# 4 - Differential Equation - Hospital ER

# Code primarily leveraged from:
#   http://apmonitor.com/che263/index.php/Main/PythonDynamicSim

print("\n\n4#: Differential Equation - Hospital ER\n")

m = GEKKO()

# time we will be integrating over
m.time = np.linspace(0,48)

# defining constant terms
c1 = 50
c2 = 50
Area = 600  # m^2

# defining the inflow
qin1 = 10   # m^3/hr inflow

# variables
ERUout = m.Var(value=0,lb=0,ub=1)
ICUout = m.Var(value=0,lb=0,ub=1)
overflow1 = m.Var(value=0,lb=0)
overflow2 = m.Var(value=0,lb=0)

# outflow equations
qin2 = m.Intermediate(c1 * ERUout**1)
qout1 = m.Intermediate(qin2 + overflow1)
qout2 = m.Intermediate(c2 * ICUout**1 + overflow2)

# mass balance equations
m.Equation(Area*ERUout.dt()==qin1-qout1)
m.Equation(Area*ICUout.dt()==qin2-qout2)

# minimize overflow
m.Obj(overflow1 + overflow2)

# set options
m.options.IMODE = 6 # dynamic optimization

# simulate differential equations
m.solve()

# plot results
plt.title("Hospital ER: ERU vs ICU")
plt.figure(1)
plt.plot(m.time,ERUout,'b-')
plt.plot(m.time,ICUout,'r--')
plt.xlabel('Time (hrs)')
plt.ylabel('Patients in thousands')
plt.legend(['ERU Cap','ICU Cap'])
plt.show()

print('\nPlot showing ERU vs ICU in plots in Python!')


