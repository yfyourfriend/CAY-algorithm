import numpy as np
from PIL import Image
import math

def deBruijnCodeLen(k):
  """
  INPUT: k
  OUTPUT: number of unique matrices we will have up to this choice of k
  """
  for i in range(1,k+1):
    print("For k=", i, ", we will obtain N=",(2**i-i)**2, " number of unique matrices")
  return

def k_needed_for_song(song_len):
  """
  Given a song of length l in seconds, output the number of k blocks we shall use
  to represent the song
  """
  # human reaction time in milliseconds
  human_reaction = 0.18
  # encoding per meaningful block
  # code_redun = 3
  code_redun = 1
  meaningful_blocks = song_len/human_reaction
  return math.ceil(code_redun * meaningful_blocks)

def deBruijn(k):

    # INPUT: k
    # OUTPUT: a string of length 2^k-1 where every substring of length k is distinct

    # list of primitive polynomials
    # https://en.wikipedia.org/wiki/Linear-feedback_shift_register#Some_polynomials_for_maximal_LFSRs

    primitive = {
        2: [0,1],
        3: [0,2],
        4: [0,3],
        5: [0,3],
        6: [0,5],
        7: [0,6],
        8: [0,4,5,6],
        9: [0,5],
        10: [0,7]
    }

    n = 2**k-1
    x = [0]*n

    for j in primitive[k]:
        x[j]=1

    for j in range(k,n):
        for i in primitive[k]:
            x[j] = (x[j]+x[j-k+i])%2

    return x


def deBruijnArray(k):

    # INPUT: k
    # OUTPUT: an array of dimension (2^k-1) by (2^k-1)
    # where every window of dimension k by k is distinct

    n = 2**k-1
    M = [[0 for j in range(n)] for i in range(n)]
    x =  deBruijn(k)

    for i in range(n):
        for j in range(n):
            M[i][j]=x[j]-x[i]
    return M

def showarray(M):

    # INPUT: M
    # OUTPUT: print M as a square, - = -1, 1=1, 0=0

    for row in M:
        strrow = ''
        for x in row:
            if x == -1:
                strrow += '-'
            else:
                strrow += str(x)
        print(strrow)




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
    shape_zero = [[1 for i in range(5)] for j in range(5)]
    shape_zero[2][2]=0
    shape_zero[2][3]=0
    shape_zero[2][4]=0
    shape_zero[3][2]=0
    shape_zero[3][4]=0
    shape_zero[4][2]=0
    shape_zero[4][3]=0
    shape_zero[4][4]=0

    # define shape for 1
    shape_one = [[1 for i in range(5)] for j in range(5)]
    shape_one[2][3] = 0
    shape_one[3][3] = 0
    shape_one[4][3] = 0
    shape_one[3][4] = 0
    shape_one[3][2] = 0

    # define shape for -1
    shape_min = [[1 for i in range(5)] for j in range(5)]
    shape_min[3][3] = 0
    shape_min[2][2] = 0
    shape_min[4][4] = 0
    shape_min[2][4] = 0

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

def scale_binmat(input_mat,ktimes):
    """
    Assume input from a list of list matrix
    Returns ktimes times bigger matrix.
    """
    lenmat = len(input_mat)
    # define ktimes times bigger matrix
    output_mat = [[0 for i in range(ktimes*lenmat)] for j in range(ktimes*lenmat)]

    for i in range(lenmat):
        for j in range(lenmat):
            # where i,j correspond to row, col of mat
            # Produce ktimes x ktimes for each entry
            for k in range(ktimes):
                for l in range(ktimes):
                    output_mat[ktimes*i+k][ktimes*j+l] = input_mat[i][j]
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

def save_image(binaryMatrix, filename):
    binaryMatrix = np.array(binaryMatrix)
    binaryMatrix = (binaryMatrix * 255).astype(np.uint8)
    im = Image.fromarray(binaryMatrix)
    im.save(filename + ".png", "PNG")
    A4len = 2480
    # 2480 divide by total Pixels per length of matrix note k=4 this is hardcoded
    # required_DPI = 2480 / (15*5)
    im = im.resize((A4len,A4len), Image.ANTIALIAS)
    im.save(filename + ".png", "PNG")
    return

def main():
    k = 7
    M = deBruijnArray(k)
    save_image(M,'DeBruijnPattern')
    output_mat = big_M(M)
    save_image(output_mat,'k7')
    """
    # Display image using PIL library
    show_image(output_mat)
    """

main()
