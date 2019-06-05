#!/usr/bin/python
from PIL import Image
from numpy import *
import numpy as *
from random import *
from bidict import *
from scipy import *
from binmaryMatrix_to_JPEG import *

def location_identification(binaryMatrix, robot_image_binary_matrix, k):
    #Actually this code is fine. WE just need an auxillary code in the middle to tansfrom an image into a kxk matrix
    """
    This function locates the k x k binary matrix inside the 2^k-1 x 2^k-1 binary matrix
    Input: 2^k-1 x 2^k-1 binary matrix, k x k robot_image_binary_matrix and the integer k
    Output: the tuple that indicates the row and column of the first entry of the location of the matrix
    """
	row4=0
	column4=0
	row15=0
	column15=0
	counter=0
	temp_counter=0
	while row15 < 2**k-1-k+1:
		while column15 < 2**k-1-k+1:
			temp_row15=row15
			while row4 < k:
				temp_column15=column15
				while column4 < k:
					if robot_image_binary_matrix[row4][column4]==binaryMatrix[temp_row15][temp_column15]:
						temp_counter=temp_counter+1
					column4=column4+1
					temp_column15=temp_column15+1	
				row4=row4 +1
				column4= 0
				temp_row15=temp_row15 +1
			if row15==0 and column15==0:
				counter=temp_counter
				row_position=0
				column_position=0
				temp_counter=0
			else:
				if temp_counter>=counter:
					counter=temp_counter
					row_position=row15
					column_position=column15
					temp_counter=0
				elif counter>temp_counter:
					counter=counter
					temp_counter=0
			column15=column15+1
			row4=0
			column4=0
			counter=0
		row15=row15+1
		column15=0
	print("Row=",row_position)
	print("Column=",column_position)
	return (row_position,column_position)

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



