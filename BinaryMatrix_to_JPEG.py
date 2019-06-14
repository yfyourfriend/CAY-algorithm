import numpy as np
from PIL import Image

def big_M(input_mat):
    """
    Assume 3 alphabets; -1,0,1 as input from a list of list matrix
    Each alphabet is defined to have a k x k shape, where k=5 in this case
    Returns 5 times bigger matrix.
    """
    lenmat = len(input_mat)
    # define 5 times bigger matrix
    output_mat = [[0 for i in range(5*lenmat)] for j in range(5*lenmat)]
    # define shape for 0
    shape_zero = [[0 for i in range(5)] for j in range(5)]
    # define shape for 1
    shape_one = [[1 for i in range(5)] for j in range(5)]
    # define shape for -1
    shape_min = [[0 for i in range(5)] for j in range(5)]
    shape_min[3][3] = 1
    shape_min[2][2] = 1
    shape_min[4][4] = 1
    shape_min[2][4] = 1

    for i in range(lenmat):
        for j in range(lenmat):
            # where i,j correspond to row, col of mat
            # Produce 5 x 5 for each entry

            # Case 1 : entry is 0
            if input_mat[i][j] == 0:
                for k in range(5):
                    for l in range(5):
                        output_mat[5*i+k][5*j+l] = shape_zero[k][l]
            # Case 2 : entry is 1
            if input_mat[i][j] == 1:
                for k in range(5):
                    for l in range(5):
                        output_mat[5*i+k][5*j+l] = shape_one[k][l]
            # Case 3 : entry is -1
            if input_mat[i][j] == -1:
                for k in range(5):
                    for l in range(5):
                        output_mat[5*i+k][5*j+l] = shape_min[k][l]
    return output_mat

def show_image(binaryMatrix):
    """
    Imput: Matrix containing only 1 and 0 in its entries
    PIL assumes np.array (dependency)
    Calls PIL for image generated from binary image
    Return None but PIL sends to std.out (standard output)
    """
    binaryMatrix = np.array(binaryMatrix)
    binaryMatrix = (binaryMatrix * 255).astype(np.uint8)
    im = Image.fromarray(binaryMatrix)
    im.show()

def main():
    # generate first row
    x = [0] * 15

    # assume polynomial x**4 + x**3 + 1 = 0
    x[0] = 1
    x[3] = 1

    # set first row according to rule
    for i in range(4,15):
        x[i] = (x[i-1] + x[i-4]) %2

    # generate matrix 2**k -1 by 2**k -1
    M = [[0 for i in range(15)] for j in range(15)]

    # fill up the matrix according to rule
    for i in  range(15):
        for j in range(15):
            # M[i][j] = (x[i] + x[j]) % 2
            M[i][j] = (x[j] - x[i])

    output_mat = big_M(M)

    # Display image using PIL library
    show_image(output_mat)

main()

