#!/usr/bin/python
from PIL import Image
import numpy as np
from Image_Generation import *

def find_image(big_image, small_image):
    # This function takes in 2 arguments and returns the position of the small image inside the big image, if there is
    # link: https://stackoverflow.com/questions/29663764/determine-if-an-image-exists-within-a-larger-image-and-if-so-find-it-using-py
    big_image = np.atleast_3d(big_image)
    small_image = np.atleast_3d(small_image)
    H, W, D = im.shape[:3]
    h, w = tpl.shape[:2]

    # Integral image and template sum per channel
    sat = im.cumsum(1).cumsum(0)
    tplsum = np.array([tpl[:, :, i].sum() for i in range(D)])

    # Calculate lookup table for all the possible windows
    iA, iB, iC, iD = sat[:-h, :-w], sat[:-h, w:], sat[h:, :-w], sat[h:, w:]
    lookup = iD - iB - iC + iA
    # Possible matches
    possible_match = np.where(np.logical_and.reduce([lookup[..., i] == tplsum[i] for i in range(D)]))

    # Find exact match
    for y, x in zip(*possible_match):
        if np.all(im[y+1:y+h+1, x+1:x+w+1] == tpl):
                return (y+1, y+h+1, x+1, x+w+1)

    return False

def rotation(frame_of_reference, openmv_image):
    """
    We will use a frame of reference (The Y as a reference frame) to compare the degree of rotation and return it. This is the
    highly inefficient. 
    """
    i = 0
    for i in range(0,360):
        frame_of_reference_rotated = frame_of_reference.Image.rotate(i)
        
        #find_image here will find the degree of rotation of the openmv_image
        if find_image(frame_of_reference_rotated, openmv_image) != False:
            degree_of_rotation = i
            #this acts as check to ensure that the degree of rotation we found is indeed accurate 
            (a,b,c,d) = find_image(openmv_image, frame_of_reference_rotated)
            if openmv_image.Image.crop(a,b,c,d) == frame_of_reference_rotated:
                return degree_of_rotation
        else:
            i += 1

def main():
    """
    The input below, from Image_generation must be in the correct format: a 75 x 75 array of RGB pixels. 
    So, ensure that the correct object is imported
    """
    large_map = Image_Generation.output_mat
    
    """
    This object will store the upright image of Y as a basis of comparison. Once again, ensure that the correct Object is
    imported
    """
    frame_of_reference = Image_Generation.xxx
    
    """
    Once again, ensure that the image is in the right format. This function will must include getdata() and setting it up into an
    matrix of size 20 x 20
    """
    openmv_image = #the image captured by the openmv will be obtained as an input here
    
    degree_of_rotation = rotation(frame_of_reference, openmv_image)
    
    #substract 360 degree here to as the degree_of_rotation mentioned directly above is based on the positive y axis
    upright_openmv_image = openmv_image.rotate(360 - degree_of_rotation)
    position_of_image = find_image(large_map, upright_openmv_image)
    print(position_of_image)
    

main()
