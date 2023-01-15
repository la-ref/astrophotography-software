
# Astrophotography Stacking &amp; Edition Software


## 1. The goal of the project
During a tutored project for our computer science GOAL, we have to realize a professional image editing software to edit, stack and filter astrophotographic images (based on a .fits, .fit)

## 2. Requirements
### 2.1 The programming language
We have chosen the programming language Python (**Version 3.10.4 recommended**), being simplified of use and rich in library, it is easier for us to develop thanks to this one. The disadvantage is that it is heavy to use, some functions can take several tens of minutes to execute.
### 2.2 The libraries
#### 2.2.1 Astropy
Use the ``pip install astropy[all]`` to download the latest version of the library. It is used to simplify our functions, especially on FITS images 
#### 2.2.1 Matplotlib
Use the ``pip install matplotlib`` to download the latest version of the library. It is used to display our images and graphics on the application
#### 2.2.1 Numpy
Use the ``pip install numpy`` to download the latest version of the library. It is used to calculate easily thanks to the different functions
#### 2.2.1 scipy
Use the ``pip install scipy`` to download the latest version of the library. It is used to rotate a matrix
#### 2.2.1 Pyinstaller
Use the ``pip install Pyinstaller`` to download the latest version of the library. It is used to generate an .exe file
## 3. Installation
### 3.1 With the .exe
> a. Create a folder
>> b. Place the .exe in it
>>> c. Create an img folder in this folder
>>>> d. Place your "M13_blue" folder holding the images with the name "M13_blue_000X".
>>>>> e. Run the .exe file

### 3.1 Without the .exe
> a. Create a folder
>> b. Place the files main.py, Calculation.py, Filters.py, Interface_front.py, Normalization.py, Stacking.py, Stacking_front.py in the folder
>>> c. Create a folder img in this folder
>>>> d. Place your "M13_blue" folder holding the images with name "M13_blue_000X"
>>>>> e. Open the file main.py and run the command "``python main.py``"

## 4. The features
### 4.1 Stacking
#### 4.1.1 Sum
Assembling several images by adding the pixels of each image represented by a 2d array
#### 4.1.1 Average
Assembly of several images by averaging each pixel of the different images represented by a 2d array
#### 4.1.1 Median
Assembly of several images by determining the median of each pixel of the different images of represented by a 2d table.
#### 4.1.1 Sigma
Assemble multiple images by adding each image with their outliers filter by the deviation and dispersion of the median for the different images of represented by a 2d table
### 4.2 Filters
#### 4.2.1 Outliers
##### 4.2.1.1 Median
Removes the outliers from each image in a list with multiple images and replaces the outliers with the median based on the range/dispersion around the median of Q1 and Q3 with the interquartile range
##### 4.2.1.2 Average
Removes outliers from each image in a list with multiple images and replaces the outliers with the mean based on the range/dispersion around the median of Q1 and Q3 with the interquartile range
##### 4.2.1.3 Sigma
Removes the outliers from each image in a list with multiple images and replaces the outliers with the range and dispersion of the median as a function of the range/dispersion around the median of Q1 and Q3 with the interquartile range

#### 4.2.2 Butterworth
##### 4.2.2.1 High pass
Allows you to apply a high-pass butterworth filter to an image represented via a 2d array by converting our image into frequency via the Fourier transform and applying the high-pass butterworth filter and converting it back into pixel
##### 4.2.2.2 Low Pass
Allows to apply an image representing via a 2d array a butterworth low pass filter by converting our image in frequency via the fourier transform and applying the butterworth low pass filter and reconverting it in pixel
#### 4.2.3 Gaussian
##### 4.2.3.1 High pass
Allows you to apply a Gaussian high-pass filter that applies a Gaussian convolution matrix to each pixel of an image represented via a 2d array and subtracts it from the base image making a high = data-low(gauss)
##### 4.2.3.2 Simple
to apply a Gaussian convolution matrix giving a blur effect on each pixel of an image represented via a 2d array

#### 4.2.4 Median
Allows to give a filtered image of each pixel by replacing them by the median of each neighboring pixel at a chosen diameter 
#### 4.2.5 Average
Allows to give a filtered image of each pixel by replacing them by the average of each neighboring pixel at a chosen diameter 
#### 4.2.6 Convolution
Allows to apply a convolution matrix on each pixel of an image represented via a 2d array The matrix is applied according to the neighbors located according to the size/diameter of the matrix directly on the pixels of the image
#### 4.2.7 Sobel
Allows to apply a convolution matrix of sobel in vertical and horizontal giving an effect of accentuation of the edges of the objects of the image and being applied on a each pixel of an image represented via a 2d table
#### 4.2.8 Bilateral
Allows to apply a bilateral filter on an image giving a blur/softness effect on each pixel of an image represented via a 2d array via the value of the Gaussian distribution and the distance between the points in the chosen neighbor diameter allowing to have a more equitable distribution than a classic Gaussian filter

## 5. Credit
- [Gauthier Corion] For the graphical interface via PyQt
- [Matthieu CZARKOWSKI] For the algorithmic software features (stacking, filter, streching)
