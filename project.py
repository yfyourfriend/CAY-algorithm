#!/usr/bin/python
from PIL import Image
from numpy import *
import numpy as *
from random import *
from bidict import *
from scipy import *


def rabin(f):
    #input f, which is a string of coefficients a0,a1,...,aN
    #Output: Reducibility of polynomials via rabin irreducibility test
    degree = len(f)
    k = prime_factors(degree)
    A = []
    f = reverse_list(f)
    f = poly1d(f)
    for j in range(0,k):
        A.append(n/k[j])
    for i in the range(1,k+1):
        tuple1 = (x**(2**A[i]) - x) / f
        g = gcd(f, tuple1[1])
        if g != 1:
            return False #f is reducible
    tuple2 = (x**(2**degree)-x) / f
    if tuple2[1] == 0:
        return True     #f is irreducible
    else:
        return False
    return 0

def prime_factors(n):
    #input int n
    #output: list of prime divisors via sieve of erathosthene
    i = 2
    factors = []
    while i*i <= n:
        if n % 1:
            i += 1
        else:
            n //= i
            factors.append(i)
    return factors

def reverse_list(f):
    return f.reverse()

def gcd(f,h):
    while remainderIsLeft(np.polydiv(f,g)):
        temporary = f
        f = g
        g = np.polydiv(temporary, g)[1][:]
        if entriesAreIdentical(g):
            return g

def entriesAreIdentical(f):
    return all(np.abs(x) == np.abs(f[0]) for x in f)

def binary_matrix(f):
    k = len(f)
    zero_array = np.zeros((2**k)-1,(2**k)-1)
    for i in range(0, k):
        zero_array[0][i] = f[i]
    for i in range(0,(2**k)-1-k):
        zero_array[0][i+k]= zero_array[0][i] + zero_array[0][i+1]
    for i in range((2**k)-1):
        zero_array[i][0]=zero_array[0][i]
    for i in range(1,(2**k)-1):
        if zero_array[i][0] == 0:
            for j in range(2**k-1):
                zero_array[i][j] = zero_array[0][j]
        else:
            for j in range((2**k)-1):
                zero_array[i][j] = zero_array[0][(2**k)-2-j]
    return zero_array

def mapping(list_of_pixels,binary_list): #must make sure its forward mapping, ie ( key: value is pixel tuple: binary number )
    keys = list_of_pixels
    values = binary_list
    for key, val in zip(keys, values):
        new_dictionary[key] = value

def error_check(A, k):
    #input a matrix
    #Output if A is unique, other the positions of k x k matrix which is not unique
    row = 0
    column = 0
    j = 0
    while j < (((2**k)-1)-k+1):
        while row < (((2**k)-1)-k+1)):
            while column < (((2**k)-1)-k+1):
                counter = 0
                for l in range(0,k):
                    for m in range(0,k):
                        if A[row + l][column + m] == A[j +l][j + m]:
                            counter += 1
                if counter == 16:
                    return (row, column)
    return True

def location_identification(binaryMatrix, robot_image_binary_matrix, k):
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



def main():
    im=Image.open("/home/ krish/Desktop/random-image-3.jpg")
    im.show()
    imrgb = im.convert("RGB")
    list_of_pixels = list(imrgb.getdata())
    size_of_row = (len(list_of_pixels)**(1/2))
    image_matrix = np.reshape(list_of_pixels,(size_of_row,3*size_of_row))
    k = (size_of_row + 1)/2
    f = []
    random_variable = 0
    while random_variable == 0:
        for i in range(0,k):
            f.append(random.randint(0,1))
        if rabin(f):
            random_variable = 1
        else:
            random_variable = 0
    binaryMatrix = binary_matrix(A)
    error_check(binaryMatrix)
    binary_list = binaryMatrix.tolist()
    mapping(list_of_pixels, binary_list)
    robot_image = Image.open("insert the path here")
    robot_image.show
    robot_image_rgb = robot_image.convert("RGB")
    robot_image_pixels = list(robot_image_rgb.getdata())
    robot_image_binary_list = []
    for i in robot_image_pixels:
        robot_image_binary_list.append(new_dictionary[i])
    robot_image_binary_matrix = np.reshape(robot_image_binary_list, (k,k))
    (x,y) = location_identification(binaryMatrix, robot_image_binary_matrix, k)



