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

def find_image(big_image, small_image):
    # This function takes in 2 arguments and returns the position of the small image inside the big image, if there is
    # take note that this function was written for opencv, need to change certain parts
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
    frame_of_reference = 5#take the smallest possible unit (5 pixel to 5 pixel)
    i = 0
    for i in range(0,360):
        frame_of_reference_rotated = frame_of_reference.Image.rotate(i)
        if find_image(frame_of_reference_rotated, #image_captured_by_robot) != False:
                degree_of_rotation = i
                (a,b,c,d) = find_image(frame_of_reference_rotated, image_captured_by_robot)
                if image_from_opnemv.Image.crop(a,b,c,d) == frame_of_reference_rotated: #Indentation error here. Fix later
                        return degree_of_rotation


    if [[0 for i in range(20)] for j in range(20)] == list(robot_image.getdata()) # reshape this as a


def main():
    im=Image.open("test1.jpeg")
    robot_image = Image.open("insert the path here")
    robot_image.show
    robot_image_pixels = list(robot_image_rgb.getdata()) #Here can we bracktact to a binary image and transform the image to a 4x4 matix?
    # Then we can run through the location_identification function with the big binary image and the frame captured by the window to get the location
    (x,y) = location_identification(binaryMatrix, robot_image_binary_matrix, k)


main()
