# import numpy as np

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from skimage.filters import threshold_triangle
from skimage.measure import label, regionprops
from skimage.morphology import binary_closing, binary_erosion
# from skimage.util import invert
from skimage.color import rgb2gray, label2rgb
from skimage import io


# read input image
image = rgb2gray(io.imread("1pagebach.png"))

# find an adaptive threshold using the triangle method
thresh = threshold_triangle(image)
# thresholded image
binary = image > thresh

# Perform binary closing; remove unwanted noise
binary = binary_closing(binary)

for i in range(5):
    binary = binary_erosion(binary, [[1,1,1,1],[1,1,1,1],[1,1,1,1]])

# Collect all distinct regions
label_image = label(binary,background=1, connectivity=1)

plt.imshow(label_image,cmap=plt.cm.hot)
plt.show()


image_label_overlay = label2rgb(label_image, image=image)

fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(image_label_overlay)
print(image_label_overlay)

for region in regionprops(label_image):

    minr, minc, maxr, maxc = region.bbox
    print(minr,maxr,minc, maxc)
    print(region.area)
    # take regions with large enough areas
    if maxr-minr > 20 and maxc - minc > 20:
        # draw rectangle around segmented coins
        rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                  fill=False, edgecolor='red', linewidth=2)
        ax.add_patch(rect)

ax.set_axis_off()
plt.tight_layout()
plt.show()

