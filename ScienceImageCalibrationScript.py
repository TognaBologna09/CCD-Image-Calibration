# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 03:07:51 2020

@author: awgiu
"""
import astropy.io.fits as astr # fits reader
import numpy as np # numpy

import matplotlib.pyplot as plt

from matplotlib.colors import LogNorm

plt.style.use('default')   

# list of the file names to iterate
science_ha_file_names = ['7469-001-ha.fit', '7469-002-ha.fit', '7469-003-ha.fit', 
                         '7469-004-ha.fit', '7469-005-ha.fit', 
                         '7469-006-ha.fit', '7469-007-ha.fit', '7469-008-ha.fit', 
                         '7469-009-ha.fit', '7469-010-ha.fit', 
                         '7469-011-ha.fit', '7469-012-ha.fit', '7469-013-ha.fit', 
                         '7469-014-ha.fit', '7469-015-ha.fit', 
                         '7469-016-ha.fit', '7469-017-ha.fit', '7469-018-ha.fit']



# list of the file names to iterate
science_i_file_names = ['7469-001-i.fit', '7469-002-i.fit', '7469-003-i.fit', 
                        '7469-004-i.fit', '7469-005-i.fit', '7469-006-i.fit', 
                        '7469-007-i.fit', '7469-008-i.fit', '7469-009-i.fit', 
                        '7469-010-i.fit', '7469-011-i.fit', '7469-012-i.fit', 
                        '7469-013-i.fit', '7469-014-i.fit', '7469-015-i.fit', 
                        '7469-016-i.fit', '7469-017-i.fit', '7469-018-i.fit']

# pathing to the folders
Path_to_science_folders = 'C:\\Users\\awgiu\Documents\\.School\\Fall 2020 (COVID ONLINE)\\ASTR 310 (observ. astro)\\Project1\\science_files'

night1_science_folder = 'night1_science'
night2_science_folder = 'night2_science'
night3_science_folder = 'night3_science'

# creating lists to place the array data with lengths equal to the number of images

science_i_n1_list = []
science_ha_n1_list = []

science_i_n2_list = []
science_i_n3_list = []
science_ha_n2_list = []
science_ha_n3_list = []

# for i in range(18): # for loop over the science images taken night 1
#     elem_i_n1 = astr.open(Path_to_science_folders+'\\'+night1_science_folder+'\\'+science_i_file_names[i])
#     elem_ha_n1 = astr.open(Path_to_science_folders+'\\'+night1_science_folder+'\\'+science_ha_file_names[i])
#     # using fits reader to access the data 
#     # appending the array data to the list
#     science_i_n1_list.append(elem_i_n1[0].data)
#     science_ha_n1_list.append(elem_ha_n1[0].data)

for i in range(10):
    elem_i_n2 = astr.open(Path_to_science_folders+'\\'+night2_science_folder+'\\'+'n2_'+science_i_file_names[i])
    elem_i_n3 = astr.open(Path_to_science_folders+'\\'+night3_science_folder+'\\'+'n3_'+science_i_file_names[i])
    # using fits reader to access the data 
    # appending the array data to the list
    science_i_n2_list.append(elem_i_n2[0].data)
    science_i_n3_list.append(elem_i_n3[0].data)
    #   #   #   #   #   #   #   #   #   #   #   #
    elem_ha_n2 = astr.open(Path_to_science_folders+'\\'+night2_science_folder+'\\'+'n2_'+science_ha_file_names[i])
    elem_ha_n3 = astr.open(Path_to_science_folders+'\\'+night3_science_folder+'\\'+'n3_'+science_ha_file_names[i])    
    # using fits reader to access the data 
    # appending the array data to the list
    science_ha_n2_list.append(elem_ha_n2[0].data)
    science_ha_n3_list.append(elem_ha_n3[0].data)

# loading in the master image data
# 
# these will fill 8 variables: dark, bias,
# ((n1,n2,n3(_i_flat)), (n1,n2,n3(_ha_flat)))

Master_Bias_image = np.loadtxt('MasterBiasImageData.csv',delimiter=',')
Master_Dark_image = np.loadtxt('MasterDarkImageData.csv',delimiter=',')

Master_i_FlatImage_n1 = np.loadtxt('Master_i_FlatImage_n1.csv',delimiter=',')
Master_i_FlatImage_n2 = np.loadtxt('Master_i_FlatImage_n2.csv',delimiter=',')
Master_i_FlatImage_n3 = np.loadtxt('Master_i_FlatImage_n3.csv',delimiter=',')

Master_ha_FlatImage_n1 = np.loadtxt('Master_ha_FlatImage_n1.csv',delimiter=',')
Master_ha_FlatImage_n2 = np.loadtxt('Master_ha_FlatImage_n2.csv',delimiter=',')
Master_ha_FlatImage_n3 = np.loadtxt('Master_ha_FlatImage_n3.csv',delimiter=',')

# writing a pixel by pixel calibration function

def calibrationFunc(rawdata,biasdata,darkdata,flatdata,true_exptime,dark_exptime):
    numerator = np.subtract(flatdata, np.add(biasdata, (true_exptime//dark_exptime)*darkdata))
    denominator = np.average(numerator)
    
    flat =np.divide(numerator, denominator)
    
    data = np.divide(np.subtract(rawdata,np.add(biasdata,(true_exptime // dark_exptime)*darkdata)),flat)
    
    return data

# Creating lists to store the function outputs

Calibrated_science_i = [ ]
Calibrated_science_ha = [ ]

# for i in range(len(Calibrated_science_i)):
#     np.savetxt('calibrated_science_i_img'+str(i)+'.csv', Calibrated_science_i[i-1], delimiter = ',')
#     np.savetxt('calibrated_science_ha_img'+str(i)+'.csv', Calibrated_science_ha[i-1], delimiter = ',')

# Calibrating n1 images

# for img in range(18):
#     calibrated_i = calibrationFunc(science_i_n1_list[img],Master_Bias_image,Master_Dark_image,Master_i_FlatImage_n1,1,1)
#     calibrated_ha = calibrationFunc(science_ha_n1_list[img],Master_Bias_image,Master_Dark_image,Master_ha_FlatImage_n1,1,1)

#     Calibrated_science_i.append(calibrated_i)
#     Calibrated_science_ha.append(calibrated_ha)

for img in range(10):
    i_n2 = calibrationFunc(science_i_n2_list[img],Master_Bias_image,Master_Dark_image,Master_i_FlatImage_n2,1,1)
    i_n3 = calibrationFunc(science_i_n3_list[img],Master_Bias_image,Master_Dark_image,Master_i_FlatImage_n3,1,1)
    
    ha_n2 = calibrationFunc(science_ha_n2_list[img],Master_Bias_image,Master_Dark_image,Master_ha_FlatImage_n2,1,1)
    ha_n3 = calibrationFunc(science_ha_n3_list[img],Master_Bias_image,Master_Dark_image,Master_ha_FlatImage_n3,1,1)
    
    Calibrated_science_i.append(i_n2)
    Calibrated_science_i.append(i_n3)
    
    Calibrated_science_ha.append(ha_n2)
    Calibrated_science_ha.append(ha_n3)

# for img in range(20):
#     fig = plt.figure(img)
#     plt.title("Calibrated I image #"+str(img))
#     plt.imshow(Calibrated_science_i[img], cmap = 'inferno', norm = LogNorm(vmin=200,vmax=6400))
#     cbar = plt.colorbar()
#     cbar.set_label('Intensity Scale')
    
# for img in range(20):
#     fig = plt.figure(img+20)
#     plt.title('Calibrated Ha image #'+str(img))
#     plt.imshow(Calibrated_science_ha[img], cmap = 'inferno', norm = LogNorm(vmin=150,vmax=6400))
#     cbar = plt.colorbar()
#     cbar.set_label('Intensity Scale')

fig = plt.figure(41)
plt.imshow(Master_Bias_image, cmap = 'magma', norm = LogNorm(vmin=1019,vmax=1030))
plt.title('Master_Bias')
plt.xlabel('Pixel')
plt.ylabel('Pixel')
cbar = plt.colorbar()
cbar.set_label('Intensity Scale')

fig = plt.figure(42)
plt.imshow(Master_Dark_image, cmap = 'magma', norm = LogNorm(vmin=150,vmax=1000))
plt.title('Master_Dark')
plt.xlabel('Pixel')
plt.ylabel('Pixel')
cbar = plt.colorbar()
cbar.set_label('Intensity Scale')

fig = plt.figure(43)
plt.imshow(Master_i_FlatImage_n2,cmap='magma', norm = LogNorm(vmin=40000,vmax=44000))
plt.title('Master Flat i n2')
plt.xlabel('Pixel')
plt.ylabel('Pixel')
cbar = plt.colorbar()
cbar.set_label('Intensity Scale')

fig = plt.figure(44)
plt.imshow(Master_ha_FlatImage_n3,cmap='magma',norm=LogNorm(vmin=15000,vmax=18000))
plt.title('Master Flat Ha n3')
plt.xlabel('Pixel')
plt.ylabel('Pixel')
cbar = plt.colorbar()
cbar.set_label('Intensity Scale')

fig = plt.figure(45)
plt.imshow(Calibrated_science_i[15], cmap='magma',norm=LogNorm(vmin=150,vmax=1230))
plt.title('Calibrated i filter Exposure 16/20')
plt.xlabel('Pixel')
plt.ylabel('Pixel')
cbar = plt.colorbar()
cbar.set_label('Intensity Scale')

fig = plt.figure(46)
plt.imshow(Calibrated_science_ha[15], cmap='magma',norm=LogNorm(vmin=150,vmax=1250))
plt.title('Calibrated Ha filter Exposure 16/20')
plt.xlabel('Pixel')
plt.ylabel('Pixel')
cbar = plt.colorbar()
cbar.set_label('Intensity Scale')

# fig = plt.figure(1)
# plt.title('Calibrated_science_image_i') 
# plt.imshow(Calibrated_science_i[0], cmap='viridis', norm=LogNorm(vmin=200,vmax=6400))
# cbar = plt.colorbar()
# cbar.set_label('Intensity Scale')

# fig = plt.figure(2)
# plt.title('Calibrated_science_image_ha')
# plt.imshow(Calibrated_science_ha[0],cmap='viridis', norm = LogNorm(vmin=200,vmax=6400))
# cbar = plt.colorbar()
# cbar.set_label('Intensity Scale')

# fig = plt.figure(3)
# plt.title('Masterflat i n2')
# plt.imshow(Master_i_FlatImage_n2,cmap='viridis', norm = LogNorm(vmin=1200,vmax=6400))
# cbar = plt.colorbar()
# cbar.set_label('Intensity Scale')

#for img in range(18):   # range equivalent to the number of imgs n1
    