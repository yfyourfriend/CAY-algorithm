import numpy as np
import matplotlib.pyplot as plt

from skimage.feature import match_template

# my imports for our version
from skimage.color import rgb2gray
from skimage import io

# new imports for ver 2
from skimage.feature import peak_local_max

image = rgb2gray(io.imread("BinaryMatoriginal.jpeg"))

# "coin" is really our -1
coin = image[2:5, 7:10]

result = match_template(image, coin,pad_input=True)
ij = np.unravel_index(np.argmax(result), result.shape)
x, y = ij[::-1]

peaks = peak_local_max(result,min_distance=2,threshold_rel=0.95) # find our peaks

fig = plt.figure(figsize=(8, 3))
ax1 = plt.subplot(1, 3, 1)
ax2 = plt.subplot(1, 3, 2)
ax3 = plt.subplot(1, 3, 3, sharex=ax2, sharey=ax2)

ax1.imshow(coin, cmap=plt.cm.gray)
ax1.set_axis_off()
ax1.set_title('template')

ax2.imshow(image, cmap=plt.cm.gray)
ax2.set_axis_off()
ax2.set_title('image')
# highlight matched region
hcoin, wcoin = coin.shape
rect = plt.Rectangle((x, y), wcoin, hcoin, edgecolor='r', facecolor='none')
ax2.add_patch(rect)

ax3.imshow(result)
ax3.set_axis_off()
ax3.set_title('`match_template`\nresult')
# highlight matched region
ax3.autoscale(False)
ax3.plot(peaks[:,1], peaks[:,0], 'o', markeredgecolor='r', markerfacecolor='none', markersize=10)

plt.show()
"""
# produce a plot equivalent to the one in the docs
plt.imshow(result)
# highlight matched regions (plural)
plt.plot(peaks[:,1], peaks[:,0], 'o', markeredgecolor='r', markerfacecolor='none', markersize=10)

plt.show()
"""


