# CCD-Image-Calibration
Scripts generated for an observational astronomy course project

# Background
This project involved taking photographs with filters on a CCD camera attached to a telescope to produce calibrated images. To produce the calibrated images in higher detail, many different image types were compiled together. Bias images have zero exposure time and are used to show the offset voltage of the CCD camera itself, Flat images of a uniformly lit surface demonstrate the differences in the efficiency of each pixel within the CCD, and Dark images are used to measure the thermal noise of the camera. These images together with the actual photograph of the galaxy in question combine to produce detailed images that can be measured with accuracy and precision.

To produce the calibrated science image, all of the Bias, Dark, and Flat exposures were combined to create a Master Bias, Master Dark, and Master Flat with which we could perform statistical operations. 

# Master Image Generation Example

_A for loop to create a master dark image_
```
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
         Master_Bias_list.append(bmedian_pix_val)    # appending val to list*
```
# Science Image Calibration Function

```
def calibrationFunc(rawdata,biasdata,darkdata,flatdata,true_exptime,dark_exptime):
    numerator = np.subtract(flatdata, np.add(biasdata, (true_exptime//dark_exptime)*darkdata))
    denominator = np.average(numerator)

    flat = np.divide(numerator, denominator)

    data = np.divide(np.subtract(rawdata,np.add(biasdata,(true_exptime // dark_exptime)*darkdata)),flat)

    return data
```

# Final Images Generated
![Alt text](C:\Users\awgiu\Documents\.School\Fall 2020 (COVID ONLINE)\ASTR 310 (observ. astro)\Project1\Figure_1_Coadded_i_NGC7469raw?=true "NGC7469")
