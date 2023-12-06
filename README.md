# Digital-Image-Processing-Assignments
This repository contains three assignments. The details of these assignments are as follows:

Assignment 1:
This Python script provides a graphical user interface (GUI) for performing various image processing operations using OpenCV, NumPy, and Tkinter. The script covers the following functionalities:

Digital Negative:
Computes the digital negative of the input image and displays both the original and negative images using Matplotlib.

1.Mapping Linear Equations:
Takes user-defined input ranges (x1, y1, x2, y2) to perform linear mapping on the image.
Displays the original and mapped images using Matplotlib.

2.Histogram Stretching:
Enhances the contrast of the input image using histogram stretching.
Prompts the user to specify the desired output range (MIN, MAX) for stretching.
Displays the original and stretched images using Matplotlib.

3.Histogram Shrinking:
Adjusts the dynamic range of the input image using histogram shrinking.
Prompts the user to specify the desired output range (MIN, MAX) for shrinking.
Displays the original and shrunken images using Matplotlib.

4.Gamma Correction:
Applies gamma correction to the input image based on the user-defined gamma value.
Prompts the user to enter the gamma value for correction.
Displays the original and gamma-corrected images using Matplotlib.

Assignment 2:
This Python script provides a graphical user interface (GUI) for implementing two image processing algorithms:

1.ACE-1 Filter:
Parameters:
k1: User-defined parameter for the ACE-1 filter.
k2: User-defined parameter for the ACE-1 filter.
N: User-defined window size (NxN) for the ACE-1 filter.
Execution:
The ACE-1 filter is applied to the chosen image with the specified parameters.
The result is displayed alongside the original image using Matplotlib.

2.Color Enhancement:
Parameters:
Color Space: User chooses between HSL or HSV for color enhancement.
Execution:
The color enhancement algorithm is applied to the chosen image in the specified color space.
The result is displayed alongside the original color image using Matplotlib.

Assignment 3:
This Python script provides a graphical user interface (GUI) for implementing an Adaptive Median Filter on an image. The script allows users to add salt and pepper noise to an image with increasing probability and then applies the Adaptive Median Filter accordingly.

Adaptive Median Filter:
Parameters:
Window Size (N x N): User-defined window size for the Adaptive Median Filter.
Execution:
The user clicks the "Adaptive Median Filter" button.
A file dialog appears to select an image file for processing.
The script adds salt and pepper noise to the image with increasing probabilities.
The Adaptive Median Filter is applied to the noisy image.
The script displays the original image with added noise and the image after noise removal using the Adaptive Median Filter.
