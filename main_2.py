from PIL import Image
import numpy as np
import math
from numpy.core._multiarray_umath import ndarray

def image_cut(image):
    pass

def adaptive_threshold(greyscale_matrix, window, threshold):
    #need to edit this function to use list of list instead of numpy array
    i = 0
    j = 0

    out_put_matrix = np.zeros((20, 20))
    intImg = np.zeros((20,20))
    greyscale_matrix = np.divide(greyscale_matrix, 255)

    #find the computed Integral Image

    #Algorithm here is shady. Check later!!

    for column in range(0,20): #go column by column, in each column sum up the rows first
        for row in range(0,20): #first go down the row
            if row == 0 and column == 0:
               intImg[row][column] = greyscale_matrix[row][column]
            elif column == 0:
                intImg[row][column] =  intImg[row-1][column] + greyscale_matrix[row][column]
            elif row == 0:
                intImg[row][column] = intImg[row][column-1] + greyscale_matrix[row][column]
            else:
                intImg[row][column] = intImg[row-1][column] + intImg[row][column-1] - intImg[row-1][column-1] +greyscale_matrix[row][column]


    for i in width:
        for j in height:
            x1 = i - math.floor(s/2) #use floor divisors here instead of floor function
            x2 = i + math.floor(s/2)
            y1 = j - math.floor(s/2)
            y2 = j + math.floor(s/2)
            count = (x2 - x1) * (y2 - y1)
            sum = intImg[x2][y2] - intImg[x2][y2 - 1] - intImg[x1 - 1][ y2] +intImg[x1 - 1][ y1 - 1]
            if image[i][j] * count <= sum * threshold:
                out_put_matrix[i][j] = 0
            else:
                out_put_matrix[i][j] = 1

    return out_put_matrix

def image_converter(binary_matrix, adaptive_threshold_image):
    #Work with an image first
    #matrix becomes a list here
    binary_list = binary_matrix.tolist()
    for i in binary_matrix:
        if i == 0:
            adaptive_threshold_image.append((0,0,0))
        if i == 1:
            adaptive_threshold_image.append((255,255,255))
    return adaptive_threshold_image

def image_to_binary(image, Y_template, t_template, O_template):
    #introduce template-matching here
    #input:Editted Image
    #Output: A list of list
    binary_list = []

    #row 1
    list_1 = []

    for i in [0,4,9,14]:
        if i == 0:
            (x,y,w,z) = (0,0,4,4)
            if (x,y,w,z).find_template(Y_template):
                list_1.append(-1)
            elif (x,y,w,z).find_template(t__template):
                list_1.append(1)
            else:
                list_1.append(0)
        else:
            (x,y,w,z) =(0,i,4,i+4)
            if (x,y,w,z).find_template(Y_template):
                list_1.append(-1)
            elif (x,y,w,z).find_template(t__template):
                list_1.append(1)
            else:
                list_1.append(0)

    # row 2
    list_2 = []

    for i in [0, 4, 9, 14]:
        if i == 0:
            (x, y, w, z) = (4, 0, 9, 4)
            if (x, y, w, z).find_template(Y_template):
                list_2.append(-1)
            elif (x, y, w, z).find_template(t__template):
                list_2.append(1)
            else:
                list_2.append(0)
        else:
            (x, y, w, z) = (4, i, 9, i + 4)
            if (x, y, w, z).find_template(Y_template):
                list_2.append(-1)
            elif (x, y, w, z).find_template(t__template):
                list_2.append(1)
            else:
                list_2.append(0)

    # row 3
    list_3 = []

    for i in [0, 4, 9, 14]:
        if i == 0:
            (x, y, w, z) = (9, 0, 13, 4)
            if (x, y, w, z).find_template(Y_template):
                list_3.append(-1)
            elif (x, y, w, z).find_template(t__template):
                list_3.append(1)
            else:
                list_3.append(0)
        else:
            (x, y, w, z) = (9, i, 13, i + 4)
            if (x, y, w, z).find_template(Y_template):
                list_3.append(-1)
            elif (x, y, w, z).find_template(t__template):
                list_3.append(1)
            else:
                list_3.append(0)

    # row 4
    list_4 = []

    for i in [0, 4, 9, 14]:
        if i == 0:
            (x, y, w, z) = (14, 0, 19, 4)
            if (x, y, w, z).find_template(Y_template):
                list_4.append(-1)
            elif (x, y, w, z).find_template(t__template):
                list_4.append(1)
            else:
                list_4.append(0)
        else:
            (x, y, w, z) = (14, i, 19, i + 4)
            if (x, y, w, z).find_template(Y_template):
                list_4.append(-1)
            elif (x, y, w, z).find_template(t__template):
                list_4.append(1)
            else:
                list_4.append(0)

    final_binary_list = []

    final_binary_list.append(list_1)
    final_binary_list.append(list_2)
    final_binary_list.append(list_3)
    final_binary_list.append(list_4)

    return final_binary_list

def localize(window):
    # INPUT : A k by k window
    # OUTPUT: (x,y) the top-left corner
    # rows are indexed 0,1,2... from TOP to BOTTOM
    # columns are indexed 0,1,2,... from LEFT to RIGHT

    k = len(window)

    diffrow = []
    for j in range(k - 1):
        count = {0: 0, 1: 0}
        for i in range(k):
            diff = (window[i][j] + window[i][j + 1]) % 2
            count[diff] += 1
        if count[0] >= count[1]:
            diffrow += [0]
        else:
            diffrow += [1]
    # print("possible diff vectors:\t\t", diffrow)
    row1 = [0]
    row2 = [1]

    for i in range(k - 1):
        row1 += [(row1[i] + diffrow[i]) % 2]
        row2 += [(row2[i] + diffrow[i]) % 2]

    # print("possible row candidate 1:\t", row1)
    # print("possible row candidate 2:\t", row2)
    # print()

    diffcol = []
    for i in range(k - 1):
        count = {0: 0, 1: 0}
        for j in range(k):
            diff = (window[i][j] + window[i + 1][j]) % 2
            count[diff] += 1
        if count[0] >= count[1]:
            diffcol += [0]
        else:
            diffcol += [1]

    # print("possible diff vectors:\t\t", diffcol)
    col1 = [0]
    col2 = [1]

    for i in range(k - 1):
        col1 += [(col1[i] + diffcol[i]) % 2]
        col2 += [(col2[i] + diffcol[i]) % 2]

    # print("possible col candidate 1:\t", col1)
    # print("possible col candidate 2:\t", col2)

    W11 = [[row1[j] - col1[i] for j in range(k)] for i in range(k)]
    # print()
    # print("W11:")
    # showarray(W11)
    d11 = dist(W11, window)
    # print("dist:", d11)

    W12 = [[row1[j] - col2[i] for j in range(k)] for i in range(k)]
    # print()
    # print("W12:")
    # showarray(W12)
    d12 = dist(W12, window)
    # print("dist:", d12)

    W21 = [[row2[j] - col1[i] for j in range(k)] for i in range(k)]
    # print()
    # print("W21:")
    # showarray(W21)
    d21 = dist(W21, window)
    # print("dist:", d21)

    W22 = [[row2[j] - col2[i] for j in range(k)] for i in range(k)]
    # print()
    # print("W22:")
    # showarray(W22)
    d22 = dist(W22, window)
    # print("dist:", d22)

    if d11 == min([d11, d12, d21, d22]):
        row = row1
        col = col1
    elif d12 == min([d11, d12, d21, d22]):
        row = row1
        col = col2
    elif d21 == min([d11, d12, d21, d22]):
        row = row2
        col = col1
    else:
        row = row2
        col = col2
    # print()

    # print("Final choice!")
    # print("row :", row )
    # print("col :", col )

    dbseq = deBruijn(k)

    for x in range(n - k + 1):
        if dbseq[x:x + k] == row: break

    for y in range(n - k + 1):
        if dbseq[y:y + k] == col: break

    # print("window is at x = {}, y = {}".format(x,y))

    return (x, y)


def dist(X, Y):
    # INPUT: X, Y, k by k windows
    # OUTPUT: Hamming distance between X and Y

    k = len(X)
    d = 0

    for i in range(k):
        for j in range(k):
            if X[i][j] != Y[i][j]: d += 1
    return d



def main():
    image = Image.open('/Users/ravi/Downloads/test.jpeg') #Ensure that this code can run in openmv

    #cut the image to get a 4 x 4 window (20 pixels x 20 pixels)
    #this function will be defined as we capture images and calculate the distance from the top and bottom to cut
    image = image_cut(image)

    #convert the image cut into the greyscale
    greyscale_image = image.rgb_to_greyscale #this is a openmv method
    greyscale_pixels = list(image.getdata())

    print(greyscale_pixels)

    #convert greyscale_pixels to greyscale_matrix
    greyscale_matrix = np.reshape((20,20)) #can remove this and work with list of lists

    #decide window and threshold
    window = int(input('What would you like the window s x s be?\n'))
    threshold = int(input('What is the threshold to convert to black and white?\n'))
    threshold = (100 - threshold)/100

    #get a binary matrix based on image
    binary_matrix = adaptive_threshold(greyscale_matrix, window, threshold) #here list of lists will not be a matrix

    #Obtaining image formed from adaptive thresholding to be converted to binary matrix later
    adaptive_threshold_image = []
    image = image_converter(binary_matrix, adaptive_threshold_image)

    #obtaining binary matrix
    window_for_localisation = image_to_binary(image)

    coordinates = localize(window_for_localisation)

    print(coordinates)
    



main()
