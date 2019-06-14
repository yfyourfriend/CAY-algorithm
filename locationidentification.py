#!/usr/bin/python
from PIL import Image
from numpy import *
import numpy as *
from random import *
from bidict import *
from scipy import *
from binmaryMatrix_to_JPEG import *

def location_identification(binaryMatrix, robot_image_binary_matrix, k):
	# This function takes in 
	row = 0
	column = 0
	while row < 56:
		while column < 56:
			counter = 0
			for l in range(0,20):
				for m in range(0,20):
					if binaryMatrix[row + l][column + m] == robot_image_binary_matrix[0 + l][0 + m]:
						counter += 1
			if counter == 20 * 20:
				return (row, column) 
	return 0

def rotate_image():
    """
    This function takes in the robot_image and transforms it with various degree of freedom and then outputs a k x k image 
    """
    pass

def main():
    im=Image.open(#The big binary image created path here)
    robot_image = Image.open("insert the path here")
    robot_image.show
    robot_image_pixels = list(robot_image_rgb.getdata()) #Here can we bracktact to a binary image and transform the image to a 4x4 matix?
    #Then we can run through the location_identification function with the big binary image and the frame captured by the window to get the location
    (x,y) = location_identification(binaryMatrix, robot_image_binary_matrix, k)



