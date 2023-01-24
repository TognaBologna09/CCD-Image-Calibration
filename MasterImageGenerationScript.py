 # -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:07:57 2020

@author: awgiu
"""


# The goal of this script is to create arrays of filenames that I 
# can copy and paste into Matlab.

# Using these filenames, the file data can be accessed and used to create
# master image files. The end result of this script are 8 saved .csv files.
# They are a master dark, master bias, and 6 flat filtered images.

import astropy.io.fits as astr
import numpy as np

import matplotlib.pyplot as plt

from pathlib import Path

# File Naming Configuration
# 
# There will be 7 arrays of filenames. bias file names, dark file names,
# flat_i_night1 file names, flat_i_night23 file names, flat_Ha file names
# science image names for each filter

bias_file_names = []    #30 different file names bias format

dark_file_names = []    #30 different file names dark format

flat_i_n1_format_names = []     #10 file names in the night 1 anomalous i format
flat_i_n2n3_format_names = []   #10 file names in the night2,night3 i format

flat_Ha_names = []  #10 file names in the Ha flat format

science_i_file_names = []   #18 different file names science i format
science_Ha_file_names = []  #18 different file names science Ha format

for i in np.arange(1,11,1):
    
    bias_name_n1 = 'Calib-0'+str('{0:02d}'.format(i))+'-bi.fit'
    bias_name_n2 = 'n2calib-0'+str('{0:02d}'.format(i))+'-bi.fit'
    bias_name_n3 = 'n3calib-0'+str('{0:02d}'.format(i))+'-bi.fit'
    bias_file_names.append(bias_name_n1)
    bias_file_names.append(bias_name_n2)
    bias_file_names.append(bias_name_n3)
    
# The bias names for night1 night2 night3 
    
    dark_name_n1 = 'Calib-0'+str('{0:02d}'.format(i))+'-d.fit'
    dark_name_n2 = 'n2calib-0'+str('{0:02d}'.format(i))+'-d.fit'
    dark_name_n3 = 'n3calib-0'+str('{0:02d}'.format(i))+'-d.fit'
    dark_file_names.append(dark_name_n1)
    dark_file_names.append(dark_name_n2)
    dark_file_names.append(dark_name_n3) 

# The dark names for night1 night2 night3
for i in np.arange(1,18,1):  
    
    flat_in1 = 'flats-0'+str('{0:02d}'.format(i))+'i.fit'
    flat_in2n3 = 'flats-0'+str('{0:02d}'.format(i))+'-i.fit'
    flat_i_n1_format_names.append(flat_in1)
    flat_i_n2n3_format_names.append(flat_in2n3)

# The flat i names for night1, night2 night3

    flat_ha = 'flats-0'+str('{0:02d}'.format(i))+'-ha.fit'
    flat_Ha_names.append(flat_ha)

for i in np.arange(1,19,1):

    sci_i = '7469-0'+'{0:02d}'.format(i)+'-i.fit'
    sci_ha = '7469-0'+'{0:02d}'.format(i)+'-ha.fit'
    science_i_file_names.append(sci_i)
    science_Ha_file_names.append(sci_ha)
    
# The science i names for night1 night2 night3
# The science Ha names for night1 night2 night3

# Creating variable lists for the CCD data

bias_files = []
dark_files = []

n1flat_i_files = []
n1flat_ha_files = []

n2_flat_i_files = []
n2_flat_ha_files = []

n3_flat_i_files = []
n3_flat_ha_files = []

#bias_folder_path = fits_image_filename = fits.util.get_testdata_filepath('Master_bias+dark')
Path_to_data_folder_db = 'C:\\Users\\awgiu\\Documents\\.School\\Fall 2020 (COVID ONLINE)\\ASTR 310 (observ. astro)\\Project1\\Master_bias+dark'
for i in range(1,31):
    elemdark = astr.open(Path_to_data_folder_db +'\\'+ (dark_file_names[i-1]))
    dark_files.append(elemdark[0].data)
    
    elembias = astr.open(Path_to_data_folder_db+'\\'+(bias_file_names[i-1]))
    bias_files.append(elembias[0].data)

Path_to_flats_folder = 'C:\\Users\\awgiu\Documents\\.School\\Fall 2020 (COVID ONLINE)\\ASTR 310 (observ. astro)\\Project1\\flats_files'
night1_i_folder = 'night1_flat_i'
night1_ha_folder = 'night1_flat_Ha'

night2_i_folder = 'night2_flat_i'
night2_ha_folder = 'night2_flat_Ha'

night3_i_folder = 'night3_flat_i'
night3_ha_folder = 'night3_flat_Ha'

for i in range(1,18):
    elem_n1_i = astr.open(Path_to_flats_folder+'\\'+night1_i_folder+'\\'+flat_i_n1_format_names[i-1])
    elem_n1_ha = astr.open(Path_to_flats_folder+'\\'+night1_ha_folder+'\\'+flat_Ha_names[i-1])
    
    n1flat_i_files.append(elem_n1_i[0].data)
    n1flat_ha_files.append(elem_n1_ha[0].data)
    
    elem_n2_i = astr.open(Path_to_flats_folder+'\\'+night2_i_folder+'\\'+flat_i_n2n3_format_names[i-1])
    elem_n2_ha = astr.open(Path_to_flats_folder+'\\'+night2_ha_folder+'\\'+flat_Ha_names[i-1])
    
    n2_flat_i_files.append(elem_n2_i[0].data)
    n2_flat_ha_files.append(elem_n2_ha[0].data)
    
    elem_n3_i = astr.open(Path_to_flats_folder+'\\'+night3_i_folder+'\\'+flat_i_n2n3_format_names[i-1])
    elem_n3_ha = astr.open(Path_to_flats_folder+'\\'+night3_ha_folder+'\\'+flat_Ha_names[i-1])
    
    n3_flat_i_files.append(elem_n3_i[0].data)
    n3_flat_ha_files.append(elem_n3_ha[0].data)

darkn1 = dark_files[0]
darkn2 = dark_files[1]
darkn3 = dark_files[2]

Master_Dark_list = []
Master_Bias_list = []

# A for loop to create a master dark image
print('start the timer...')
for row in range(1472): # rows in pixel data
    print(1472-row) # timer
    for col in range(2184): # cols in pixel data
        
        bias_list_to_take_median = []   # bias image list of pixel vals
        
        for img in range(30):   
            
            bias_image_data_set = bias_files[img]   # var for img file
            bpix_val = bias_image_data_set[row,col] # pixel value for img file
            bias_list_to_take_median.append(bpix_val)   # appending pix val
            
        bmedian_pix_val = np.median(bias_list_to_take_median) # computing median
        Master_Bias_list.append(bmedian_pix_val)    # appending val to list

# Using the large for loop above to create an array of the master bias image file

Master_Bias_array = np.asarray(Master_Bias_list)    # list to array
Master_Bias_image = np.reshape(Master_Bias_array,(1472,2184))   # reshaping array
np.savetxt("MasterBiasImageData.csv",Master_Bias_image,delimiter=',') #saving as csv

for row in range(1472): # rows in pixel data
    print(1472-row) # timer
    for col in range(2184): # cols in pixel data
        
        list_to_take_median = []
        
        for img in range(30):
            
            b_file = bias_files[img] # a pix value for the master bias
            b_pixval = b_file[row,col]
            
            image_data_set = dark_files[img]    # variable for the image file
            pix_val = image_data_set[row,col]-b_pixval # pixel value for image file
            list_to_take_median.append(pix_val) # appending pixel value
        
        median_pix_val = np.median(list_to_take_median) # computing median of pix values over images
        Master_Dark_list.append(median_pix_val) # appending the list for master img

# using the data stored from the for loop to create Master Dark 

Master_Dark_array = np.asarray(Master_Dark_list)    # converting list to array
Master_Dark_image = np.reshape(Master_Dark_array,(1472,2184))   # reshaping array
np.savetxt("MasterDarkImageData.csv",Master_Dark_image,delimiter=',') # saving as csv



# creating variable lists for the master flat images of each night
        
Master_i_n1_list = []
Master_i_n2_list = []
Master_i_n3_list = []

Master_ha_n1_list = []
Master_ha_n2_list = []
Master_ha_n3_list = []

# a for loop to calculate the median pixel value of all 17 flats taken each night
print('start the second timer...')
for row in range(1472):
    print(1472-row)
    for col in range(2184):
        
        in1_pix_list = []
        in2_pix_list = []
        in3_pix_list = []
        
        han1_pix_list = []
        han2_pix_list = []
        han3_pix_list = []
        
        for img in range(17):
            
            in1_img_data_set = n1flat_i_files[img]
            in1_pix_val = in1_img_data_set[row,col]
            in1_pix_list.append(in1_pix_val)
            
            in2_img_data_set = n2_flat_i_files[img]
            in2_pix_val = in2_img_data_set[row,col]
            in2_pix_list.append(in2_pix_val)
            
            in3_img_data_set = n3_flat_i_files[img]
            in3_pix_val = in3_img_data_set[row,col]
            in3_pix_list.append(in3_pix_val)
            
            han1_img_data_set = n1flat_ha_files[img]
            han1_pix_val = han1_img_data_set[row,col]
            han1_pix_list.append(han1_pix_val)
            
            han2_img_data_set = n2_flat_ha_files[img]
            han2_pix_val = han2_img_data_set[row,col]
            han2_pix_list.append(han2_pix_val)
            
            han3_img_data_set = n3_flat_ha_files[img]
            han3_pix_val = han3_img_data_set[row,col]
            han3_pix_list.append(han3_pix_val)
        
        in1_med_func = np.median(in1_pix_list)
        Master_i_n1_list.append(in1_med_func)
        
        in2_med_func = np.median(in2_pix_list)
        Master_i_n2_list.append(in2_med_func)
        
        in3_med_func = np.median(in3_pix_list)
        Master_i_n3_list.append(in3_med_func)
        
        han1_med_func = np.median(han1_pix_list)
        Master_ha_n1_list.append(han1_med_func)
        
        han2_med_func = np.median(han2_pix_list)
        Master_ha_n2_list.append(han2_med_func)
        
        han3_med_func = np.median(han3_pix_list)
        Master_ha_n3_list.append(han3_med_func)
            
Master_i_n1_array = np.asarray(Master_i_n1_list)    # converting list to array
Master_i_flat_image_n1 = np.reshape(Master_i_n1_array,(1472,2184)) # reshaping to array

Master_i_n2_array = np.asarray(Master_i_n2_list)     # converting list to array
Master_i_flat_image_n2 = np.reshape(Master_i_n2_array,(1472,2184)) # reshaping to array


Master_i_n3_array = np.asarray(Master_i_n3_list) # converting list to array
Master_i_flat_image_n3 = np.reshape(Master_i_n3_array,(1472,2184)) # reshaping to array


Master_ha_n1_array = np.asarray(Master_ha_n1_list) # converting list to array
Master_ha_flat_image_n1 = np.reshape(Master_ha_n1_array,(1472,2184)) # reshaping to array


Master_ha_n2_array = np.asarray(Master_ha_n2_list) # converting list to array
Master_ha_flat_image_n2 = np.reshape(Master_ha_n2_array,(1472,2184))


Master_ha_n3_array = np.asarray(Master_ha_n3_list) # converting list to array
Master_ha_flat_image_n3 = np.reshape(Master_ha_n3_array,(1472,2184))


# Saving the arrays

#np.savetxt('Master_i_FlatImage_n1.csv',Master_i_flat_image_n1,delimiter=',')  # saved to csv
#np.savetxt('Master_i_FlatImage_n2.csv',Master_i_flat_image_n2,delimiter=',')
#np.savetxt('Master_i_FlatImage_n3.csv',Master_i_flat_image_n3,delimiter=',')

#np.savetxt('Master_ha_FlatImage_n1.csv',Master_ha_flat_image_n1,delimiter=',')
#np.savetxt('Master_ha_FlatImage_n2.csv',Master_ha_flat_image_n2,delimiter=',')
#np.savetxt('Master_ha_FlatImage_n3.csv',Master_ha_flat_image_n3,delimiter=',')

# plotting 

fig = plt.figure(1)
plt.imshow(Master_Dark_image)

fig = plt.figure(2)
plt.imshow(Master_ha_flat_image_n2)

fig = plt.figure(3)
plt.imshow(Master_i_flat_image_n3)

# Printing the file names into the console
print('Bias flenames: \n\n')
print(bias_file_names)

print('\n\nDark filenames: \n\n')
print(dark_file_names)

print('\n\nFlat i night 1 filenames: \n\n')
print(flat_i_n1_format_names)
print('\n\nFlat i night 2 and 3 filenames: \n\n')
print(flat_i_n2n3_format_names)

print('\n\nFlat Ha filenames: \n\n')
print(flat_Ha_names)

print('\n\nScience i filter filenames: \n\n')
print(science_i_file_names)

print('\n\nScience Ha filter filenames: \n\n')
print(science_Ha_file_names)

    