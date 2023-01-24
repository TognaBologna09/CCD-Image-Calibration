# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 03:01:31 2020

@author: awgiu
"""


import matplotlib.pyplot as plt
import numpy as np
#from mat4py import loadmat
from matplotlib.colors import LogNorm

import scipy.io

icoadded = scipy.io.loadmat('iCoadded.mat')
data = icoadded.get('iCoadded')

fig = plt.figure(1)
plt.imshow(data,cmap='inferno',norm=LogNorm(vmin=3000,vmax=17000))
plt.title('Co-added i filter NGC7469')
plt.xlim(1050,1200)
plt.ylim(900,1060)
plt.xlabel('Pixel')
plt.ylabel('Pixel')
cbar = plt.colorbar()
cbar.set_label('Intensity Scale')

fig = plt.figure(2)
plt.title('Histogram of Intensity values from co-added i filter NGC7569')
plt.hist(data,[0,1000,2000,3000,4000,6000,8000,10000,14000,18000,22000])