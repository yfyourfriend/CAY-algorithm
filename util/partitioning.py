import matplotlib.pyplot as plt
from skimage.filters import threshold_triangle

from skimage.morphology import convex_hull_image, binary_opening, binary_erosion, binary_closing
from skimage.util import invert

from skimage.color import rgb2gray
from skimage import io

import numpy as np

from scipy import ndimage

# read input image
image = rgb2gray(io.imread("bachsuite1preludefullpage.png"))

# find an adaptive threshold using the triangle method
thresh = threshold_triangle(image)
# thresholded image
binary = image > thresh

# Perform binary closing; remove unwanted noise
# binary = binary_closing(binary)

# Perform binary dilation; connect regions
for j in range(3):
    binary = binary_erosion(binary)
    for i in range(2):
        binary = binary_closing(binary)
    binary = binary_erosion(binary)

# Collect all distinct regions
label_im, nb_labels = ndimage.label(binary)

print(label_im,nb_labels)

# Routine to remove regions not fitting width, height specs
def remove_unfit_matrices(label_im, nb_labels, minRow, minCol):
    """
    Input: label_im matrix.
    Output: matrices w removed entries not in width height specification
    """
    to_eliminate = []
    new_nb_labels = nb_labels
    output_mat = np.zeros_like(label_im)
    for i in range(0,nb_labels):
        slice_x, slice_y = ndimage.find_objects(label_im==i)[0]
        # set at least 40 pixels in width
        if abs(slice_x.start - slice_x.stop) <= minCol:
            to_eliminate.append(i)
        # set at least 300 pixels in length
        elif abs(slice_y.start - slice_y.stop) <= minRow:
            to_eliminate.append(i)
    for i in to_eliminate:
        output_mat[ndimage.find_objects(label_im==i)[0]]==0
        new_nb_labels -= 1
    return (output_mat,new_nb_labels)

binary, new_nb_labels = remove_unfit_matrices(binary, nb_labels,15,450)
print(binary, new_nb_labels)

plt.imshow(binary, cmap='gray')
plt.show()


