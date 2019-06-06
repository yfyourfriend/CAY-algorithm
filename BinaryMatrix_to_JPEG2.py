from PIL import Image
import numpy as np

def binary_Matrix(A):
    #input: A is a list corresponding to the cofficients of a ireducible polynomial over galois field 2 
    #Output: 1023 x 1023 binary matix
    x = np.zeros((1023,1023))
    for i in range(11):
        x[0][i] = A[i]
        for i in range(0,(2**10)-1-10):
        x[0][i+4] =( x[0][i] + x[0][i+1] ) % 2
    for i in range((2**10)-1):
        x[i][0]=x[0][i]
    for i in range(1,(2**10)-1):
        if x[i][0] == 0:
            for j in range(2**10-1):
                x[i][j] = x[0][j]
        else:
            for j in range((2**10)-1):
                x[i][j] = x[0][(2**10)-2-j]
    return x

def show_image(binaryMatrix):
    binaryMatrix = (binaryMatrix * 255).astype(np.uint8)
    im = Image.fromarray(x)
    im.show()
    print(im)
   
def main():
    A = [1, 1, 1, 0, 1, 0, 1, 0, 1, 0,1]
    binaryMatrix = binary_Matrix(A)
    show_image(binaryMatrix) 
    
