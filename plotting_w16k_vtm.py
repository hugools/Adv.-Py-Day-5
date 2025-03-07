#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 12:56:34 2025

@author: hugoo
"""
import matplotlib.pyplot as plt

f = open("W16K_VTM.txt", "r")
temp = []
cd = []

for x in f:
    temp.append(float(x[0:7]))
    cd.append(float(x[8:16]))
    
fig = plt.figure()
ax  = fig.add_subplot(111)
ax.set_title('VTM of W16K')
ax.plot(temp, cd, label='fit', color='r')
ax.set_xlabel(r'Celsius')
ax.set_ylabel(r'CD')
plt.show()

    