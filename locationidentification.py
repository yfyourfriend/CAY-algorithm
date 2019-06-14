#!/usr/bin/python
from PIL import Image
import numpy as np
from binmaryMatrix_to_JPEG import *

def location_identification(binaryMatrix, robot_image_binary_matrix, k):
	"""
	This function takes in the 75 x 75 grid_map and the 20 x 20 image captured by the openmv and returns the matrix 
	that contains the position of the image
	"""
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
				return (row, row + 19, column, column + 19)
			column += 1
		row += 1
	return 0



def rotation():
	"""
	We will use a frame of reference (The Y as a reference frame) to compare the degree of rotation and return it. This is the
	simplest case we can try to solve. 
	In the 2nd stage, we check if the image captured is all black or all white - (In our current map, there are exactly only 1 all
	black case and 0 all white square. 
	In the 3 stage (the most complicated case: where there is no complete Y in the image captured, rather fragments of Y or no Y at all. Figure 
	out a way to find out the location here.
	"""
	
	#Stage 1
	frame_of_reference = #take the smallest possible unit (5 pixel to 5 pixel)
	filter = frame_of_reference
	i = 0
	for i in range(0,360):
		frame_of_reference_rotated = frame_of_reference.Image.rotate(i)
		if #use PIL Image filter to check for the existence of T, comparsion is rotated frame of reference and the image captured:
			degree_of_rotation = Image.dispacement.rotation(frame_of_reference_rotated, frame_of_reference)
			return degree_of_rotation 
	if [[0 for i in range(20)] for j in range(20)] == list(robot_image.getdata()) # reshape this as a
		

def main():
    im=Image.open(#The big binary image created path here)
    robot_image = Image.open("insert the path here")
    robot_image.show
    robot_image_pixels = list(robot_image_rgb.getdata()) #Here can we bracktact to a binary image and transform the image to a 4x4 matix?
    #Then we can run through the location_identification function with the big binary image and the frame captured by the window to get the location
    (x,y) = location_identification(binaryMatrix, robot_image_binary_matrix, k)



