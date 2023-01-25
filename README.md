# CCD-Image-Calibration
Scripts generated for an observational astronomy course project

# Background
This project involved taking photographs with filters on a CCD camera attached to a telescope to produce calibrated images. To produce the calibrated images in higher detail, many different image types were compiled together. Bias images have zero exposure time and are used to show the offset voltage of the CCD camera itself, Flat images of a uniformly lit surface demonstrate the differences in the efficiency of each pixel within the CCD, and Dark images are used to measure the thermal noise of the camera. These images together with the actual photograph of the galaxy in question combine to produce detailed images that can be measured with accuracy and precision.

To produce the calibrated science image, all of the Bias, Dark, and Flat exposures were combined to create a Master Bias, Master Dark, and Master Flat with which we could perform statistical operations. 
