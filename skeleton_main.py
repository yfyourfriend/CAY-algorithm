# Hello World Example
#
# Welcome to the OpenMV IDE! Click on the green run arrow button below to run the script!

import sensor, image, time

sensor.reset()                      # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)   # Set frame size to QVGA (320x240)
sensor.skip_frames(time = 2000)     # Wait for settings take effect.
clock = time.clock()                # Create a clock object to track the FPS.
template1 = image.Image()                    #insert gray scale image path of 'Y' template here
template2 = image.Image()                    #insert gray scale image path of '+' template here
template3 = image.Image()                    #insert gray scale image path of 'O' template here

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
    
def get_list_of_list(window):
    list_1 = [0,0,0,0]
    list_2 = [0,0,0,0]
    list_3 = [0,0,0,0]
    list_4 = [0,0,0,0]
    counter = 0
    while counter != 16:
        tup1 = window.find_template(template1)
        tup2 = window.find_template(template2)
        tup3 = window.find_template(template3)
        if tup1[0] < tup2[0]:
            if tup1[0] <= tup3[0]:
                row = tup1[0]
                column = tup1[1]
                if column == 4:
                    column = 1
                if column == 9:
                    column = 2
                if column == 13
                    column = 3
                if row == 0:
                    list_1[column] = -1
                    counter += 1
                if row == 4:
                    list_2[column] = -1
                    counter += 1
                if row == 9:
                    list_3[column] = -1
                    counter += 1
                if row == 14:
                    list_4[column] = -1
                    counter += 1
                window.mask_rectange(tup1)
            if tup1[0] >= tup3[0]:
                row = tup3[0]
                column = tup3[1]
                if column == 4:
                    column = 1
                if column == 9:
                    column = 2
                if column == 13
                    column = 3
                if row == 0:
                    list_1[column] = 0
                    counter += 1
                if row == 4:
                    list_2[column] = 0
                    counter += 1
                if row == 9:
                    list_3[column] = 0
                    counter += 1
                if row == 14:
                    list_4[column] = 0
                    counter += 1
                window.mask_rectange(tup3)
        elif tup2[0] < tup1[0]:
            if tup2[0] <= tup3[0]:
                row = tup2[0]
                column = tup2[1]
                if column == 4:
                    column = 1
                if column == 9:
                    column = 2
                if column == 13
                    column = 3
                if row == 0:
                    list_1[column] = 1
                    counter += 1
                if row == 4:
                    list_2[column] = 1
                    counter += 1
                if row == 9:
                    list_3[column] = 1
                    counter += 1
                if row == 14:
                    list_4[column] = 1
                    counter += 1
                window.mask_rectange(tup2)
            if tup2[0] >= tup3[0]:
                row = tup3[0]
                column = tup3[1]
                if column == 4:
                    column = 1
                if column == 9:
                    column = 2
                if column == 13
                    column = 3
                if row == 0:
                    list_1[column] = 0
                    counter += 1
                if row == 4:
                    list_2[column] = 0
                    counter += 1
                if row == 9:
                    list_3[column] = 0
                    counter += 1
                if row == 14:
                    list_4[column] = 0
                    counter += 1
                window.mask_rectange(tup3)
        else:
            if tup1[1] < tup2[1]:
                row = tup1[0]
                column = tup1[1]
                if column == 4:
                    column = 1
                if column == 9:
                    column = 2
                if column == 13
                    column = 3
                if row == 0:
                    list_1[column] = -1
                    counter += 1
                if row == 4:
                    list_2[column] = -1
                    counter += 1
                if row == 9:
                    list_3[column] = -1
                    counter += 1
                if row == 14:
                    list_4[column] = -1
                    counter += 1
                window.mask_rectangle(tup1)
            else:
                row = tup2[0]
                column = tup2[1]
                if column == 4:
                    column = 1
                if column == 9:
                    column = 2
                if column == 13
                    column = 3
                if row == 0:
                    list_1[column] = 1
                    counter += 1
                if row == 4:
                    list_2[column] = 1
                    counter += 1
                if row == 9:
                    list_3[column] = 1
                    counter += 1
                if row == 14:
                    list_4[column] = 1
                    counter += 1
                window.mask_rectange(tup2)
        if counter == 17:
            print("Counter has hit 17. There is a problem with the algorithm.End loop here.")
            return "Error"
    
    list_of_list = [list_1, list_2, list_3, list_4]
    return list_of_list
    

while(True):
    clock.tick()                    # Update the FPS clock.
    window = sensor.snapshot()      # Take a picture and return the image.
    window = window.rgb_to_grayscale()
    window = window.midpoint(1,0.5,True,1,False, None)
    list_of_list = get_list_of_list(window)
    location_tuple = localise(list_of_list)

    print(clock.fps())              # Note: OpenMV Cam runs about half as fast when connected
                                    # to the IDE. The FPS should increase once disconnected.
