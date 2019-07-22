"""
Crucial references
similar stackoverflow for watermark on pdf slides
https://stackoverflow.com/questions/2925484/place-image-over-pdf/33405986
documentation
https://www.reportlab.com/docs/reportlab-userguide.pdf
"""
from io import BytesIO
from PyPDF2 import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

"""
import numpy as np
from PIL import Image

# Img processing
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

def scale_binmat(input_mat,ktimes):
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

im = Image.open('tag36_11_00000_multiplyby0.png')
np_im = np.array(im)
for i in range(1,100):
    new_im = np.array(scale_binmat(np_im,i))
    new_im =  Image.fromarray(new_im)
    new_im.save("tag36_11_00000_multiplyby" + str(i) + ".png")
"""

# Get our files ready
output_file = PdfFileWriter()
coded_out = PdfFileWriter()

# Remember to rename input file; this is the musical score
blank_paper = PdfFileReader(open("blankA4.pdf", "rb"))
input_file = PdfFileReader(open("1pagebach.pdf", "rb"))
path = 'codes/apriltag-imgs/tag36h11/tag36_11_00000.png'

# Store number of pages in input document, since score could have multiple pages
# We only test with 1 page pdf for now
page_count = input_file.getNumPages()

# Go through all the input file pages to overlay De Bruijn code
# for page_number in range(page_count):
page_number = 0
print ("Creating code for page {} of {}".format(page_number, page_count))

# Set input page on current page number
input_page = input_file.getPage(page_number)
blank_paper = blank_paper.getPage(0)

# Create object for each linear slice of our De Bruijn window up till end of music line
imgTemp = BytesIO()
imgDoc = canvas.Canvas(imgTemp, pagesize=A4)

# Draw image on Canvas and save PDF in buffer

# In which this line is embeddedd many times for different subsections of the matrix canvas.
# drawImage(self, image, x,y, width=None,height=None,mask=None); note image is path to common image file eg .jpeg
# imgDoc.drawImage(path.format(page_number), 0, 0)
code_width, code_height = imgDoc.drawImage(path.format(page_number), 0, 0)
# x, y - start position

# Scale imgDoc for the code
ratio_to_scale = A4[0]/code_width
print(code_width, code_height)
desired_width = 6
ratio_to_scale = 6/code_width
# Instead, we scale using the PIL function
# 6 mm
print(ratio_to_scale)

# imgDoc.scale(ratio_to_scale, ratio_to_scale)

imgDoc.save()

# Use PyPDF to merge the image-PDF into the template
# mixed_page = PdfFileReader(BytesIO(imgTemp.getvalue())).getPage(0)
# mixed_page.mergePage(input_page)
coded_page = PdfFileReader(BytesIO(imgTemp.getvalue())).getPage(0)
coded_page.scale(ratio_to_scale,ratio_to_scale)

blank_paper.mergePage(coded_page)
input_page.mergePage(coded_page)
# output_file.addPage(PdfFileReader(BytesIO(imgTemp.getvalue())).getPage(0))
output_file.addPage(input_page)
coded_out.addPage(blank_paper)

# finally write "output" to document
output_file.write(open("document-output.pdf","wb"))
coded_out.write(open("document-code-output.pdf","wb"))

