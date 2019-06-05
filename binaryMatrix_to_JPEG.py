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


def error_check(binaryMatrix, k):
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


def main():
    k = int(input("What is the integer K? (K < 100)\n"))
    f = []
    random_variable = 0
    while random_variable == 0:
        for i in range(0,k):
            f.append(random.randint(0,1))
        if rabin(f):
            random_variable = 1
        else:
            random_variable = 0
    binaryMatrix = binary_matrix(f)
    if error_check(binaryMatrix, k) != 0:
        #insert code to replace identical parts
        pass
    #from here we will create an binary imgae
    #We can attach maybe 1 = RGB(255,255,255) - white
    #we can attach 0 = RGB(0,0,0) - black
    #Then generate a black & white image whereby every k x k frame is unique from the binary matrix

















