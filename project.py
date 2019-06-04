#!/usr/bin/python
from PIL import Image
from numpy import *
import numpy as *
from random import *
from bidict import *
from scipy import *
"""
this is redundant now
def poly_to_str(coefficients):
    #input binary string of size k
    #output polynomial f that can be used in rabin test. if rabin test passes, then we can use this string of size k to form the 2^k -1 x 2^k -1 matrix
    return ''.join(['{:+d}x**{:d}'.format(a,n) for n, a in enumerate(coefficients)][::-1]) #figure out how to differentiate string vs comment in python
"""

def rabin(f): #Input becomes a string of coefficients
    #input f, which is a string of coefficients a0,a1,...,aN
    #Output: Reducibility of polynomials via rabin irreducibility test
    degree = len(f)
    k = prime_factors(degree)
    A = []
    f = poly1d(f)
    for j in range(0,k):
        A.append(n/k[j])
    for i in the range(1,k+1):
        tuple1 = (x**(2**A[i]) - x) / f #2nd entry in the tuple provides the remainder. need to make sure that the 2nd entry is selected
        g = gcd(f, tuple1[1]) #Need to define gcd for the polynomials
        if g != 1:
            return False #"f is reducible"
    tuple2 = (x**(2**degree)-x) / f
    if tuple2[1] == 0:
        return True     # "f is irreducible"
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

def gcd(f,h): #Figure out a way to calculate the greatest common divisor of 2 polynomials
    #Input: 2 polynomials f and h
    #output: the greatest common divisor of both polynomials
    pass

def binary_matrix(f): #f is the list consisting of the coefficients of the polynomial #len(f) == k from jpg_processor
    k = len(f) #k is the degree of polynomial f
    zero_array = np.zeros((2**k)-1,(2**k)-1)
    for i in range(0, k):
        zero_array[0][i] = f[i] #each coefficient from the constant coefficient to leading coefficient is mapped to the first k columns in the first row of the matrix
    for i in range(0,11): #Change 11 here
        zero_array[0][i+4]= zero_array[0][i] + zero_array[0][i+1] #Change i+something here
    for i in range(15): #change 15 here
        zero_array[i][0]=zero_array[0][i]
    for i in range(1,15): #Change range here
        if zero_array[i][0] == 0:
            for j in range(15): #change 15 here
                zero_array[i][j] = zero_array[0][j]
        else:
            for j in range(15): #change 15 here
                zero_array[i][j] = zero_array[0][14-j] #change 14 here
    return zero_array

def mapping(x,list_of_pixels): #Check if the mapping corresponds, help bijective mapping for 2 matrices
    keys = x
    values = list_of_pixels
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
                    return (row, colum) #returns the index of the first entry (1,1) of kxk matrix that are identical. Thus, the number at this index can be changed
    return True

def location_identification(A, window, k): #input is robot window, A and k (need to work with error correction)
    row = 0
    column = 0
    while row < (((2**k)-1)-k+1):
        while column < (((2**k)-1)-k+1):
            counter = 0
            for l in range(0,k):
                for m in range(0,k):
                    if A[row + l][column + m] == window[0+l][0+m]:
                        counter+=1
            if counter == 16:
                return (row,column)



def main():
    im=Image.open("/home/ krish/Desktop/random-image-3.jpg")
    im.show()
    imrgb = im.convert("RGB")
    list_of_pixels = list(imrgb.getdata())
    size_of_row = (len(list_of_pixels)**(1/2)) #no of rows in the pixel_matrix
    image_matrix = np.reshape(list_of_pixels,(size_of_row,3*size_of_row)) #from here we can figure out k
    k = (size_of_row + 1)/2
    f = []
    while True:
        for i in range(0,k):
            A.append(random.randint(0,1))
        #f = poly_to_str(A), this becomes redundant
        if rabin(f):
            #find a way to end look and use A from here
            pass
    x = binary_matrix(A)
    error_check(x, k)
    mapping(x, image_matrix)
    #from here on we need an input of the camera image by the robot the small window
    #then the function location_identification can be called upon to provide the exact location



