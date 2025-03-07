#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 13:27:05 2025

@author: hugoo
"""

#Use numpy.load() to load the arrays. For both arrays [:,0] correspond to 
#the scattering vector and [:,1] corresponds to the scattering strength. 
#A few useful SciPy functions might be scipy.optimize.minimize_scalar() and 
#scipy.interpolate.interp1d(). Matplotlib might be helpful to visualize the 
#result, e.g. with plot() or scatter().

import numpy as np
import matplotlib.pyplot as plt
import scipy

exp = np.load('I_q_IPA_exp.npy')
mod = np.load('I_q_IPA_model.npy')
exp_trimmed = exp[10:254,:]

f = scipy.interpolate.interp1d(mod[:,0], mod[:,1])
new_mod = f(exp_trimmed[:,0])


def min_err(x):
    difference = sum((x * new_mod - exp_trimmed[:,1])**2)
    return difference

res = scipy.optimize.minimize_scalar(min_err)


fig = plt.figure()
ax  = fig.add_subplot(111)
ax.plot(exp_trimmed[:,0], exp_trimmed[:,1], label='fit', color='r')
ax.plot(exp_trimmed[:,0], res.x*new_mod, label='fit', color='g')
plt.show()
print(res.x)
