# CAY-algorithm
In this project, we are trying to make a robot to scan dots in order for it to know its position. 
The sequence of the dots are unique from each other, and therefore each location has a unique sets of dots, 
which the robot will scan and read.

In the image processing section, the code converts an image saved in desktop into an RGB image.
So, when our robot uses the camera attached to it, it will snap a photo of the sequence of dots at the paper underneath it.
Then, that snapshot will be converted (from, say, CMYK) into RGB format.
The algorithm will then convert the RGB image into a sequence of numbers, arranged in the form of a matrix.
Each element of the matrix has 3 components. Each corresponds to how red, blue, or green-ish the pixel is.
So, for example, an image with 15 by 15 pixel size will have 225 pixels. The algorithm will convert each pixels into a sequence of 3 numbers
which are the R,G,B components of the pixel. And since there are 225 pixels to be scanned and converted, we will have an array (matrix)
with the size of 15 by 45, because each element of the matrix has 3 components.

Next the sequence of numbers (the matrix) above will be compared to a "map" that the robot already have inside its "brain". That is,
the robot already knows the picture of all the dots in the paper located underneath it. Since the robot is only scanning a small part
of the paper, the robot only has a small part of all the sequences of dots. Since the sequences are unique, the robot can then compare the
image which it has captured underneath it with a full map that it already has inside its brain. Therefore the robot will know its location
in the big paper.
