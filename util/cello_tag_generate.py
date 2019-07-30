from PyPDF2 import PdfFileWriter, PdfFileReader

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Image,Table


########################################################################
class LetterMaker(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, pdf_file, org, seconds):
        self.c = canvas.Canvas(pdf_file, pagesize=A4)
        self.styles = getSampleStyleSheet()
        self.width, self.height = A4
        self.organization = org
        self.seconds  = seconds


    #----------------------------------------------------------------------
    def createDocument(self):
        """"""
        # voffset = 65

        # settings for later
        init_pos = (85, 120)
        num_music_lines = 11
        bar_per_bulk_line = 4
        music_len_bulk = 143
        music_height_bulk = 102

        # How to insert later
        init_pos_first = (85,self.height-(190))
        bar_per_init = 3
        music_len_first = 177

        start_tag = 3

        # Create list of Distinct Tags
        Y = [i for i in range(start_tag)]
        for i in range(start_tag):
            digit_len = len(str(i))
            dir_str = 'tag36h11/tag36_11_'
            # Compensate for number of digits
            for j in range(5-digit_len):
                dir_str += str(0)
            Y[i-start_tag] = Image(dir_str + str(i) + '.png')
            Y[i-start_tag].drawHeight = 2.5*mm
            Y[i-start_tag].drawWidth = 2.5*mm

        # Create list of Distinct Tags to input
        # tag_num = 1
        tag_num = bar_per_init + bar_per_bulk_line * num_music_lines
        I = [i for i in range(tag_num)]
        for i in range(start_tag,tag_num):
            digit_len = len(str(i))
            dir_str = 'tag36h11/tag36_11_'
            # Compensate for number of digits
            for j in range(5-digit_len):
                dir_str += str(0)
            I[i-start_tag] = Image(dir_str + str(i) + '.png')
            I[i-start_tag].drawHeight = 2.5*mm
            I[i-start_tag].drawWidth = 2.5*mm

        # Also programmatically create the data object with correct labels / placement

        # container for the 'Flowable' objects
        elements = []

        data = [ [i for i in range(bar_per_bulk_line)] for j in range(num_music_lines)]
        for j in range(num_music_lines):
            for i in range(bar_per_bulk_line):
                # print(i,j, i + j*bar_per_bulk_line)
                data[j][i] = I[i + j*bar_per_bulk_line]
                # print(data)
        # print(data)

        table = Table(data, colWidths=music_len_bulk, rowHeights = music_height_bulk)
        # table.setStyle([("VALIGN", (0,0), (0,0), "TOP")])
        table.wrapOn(self.c, self.width, self.height)
        # table.drawOn(self.c, *self.coord(init_pos[0],init_pos[1]))
        table.drawOn(self.c, init_pos[0],init_pos[1])


        data = [ [i for i in range(bar_per_init)] ]
        for j in range(bar_per_init):
            # print(i,j, i + j*bar_per_bulk_line)
            data[0][j] = I[j]
            # print(data)
        # print(data)

        table2 = Table(data, colWidths=music_len_first, rowHeights = music_height_bulk)
        # table2.setStyle([("VALIGN", (0,0), (0,0), "TOP")])
        table2.wrapOn(self.c, self.width, self.height)
        # table2.drawOn(self.c, *self.coord(init_pos[0],init_pos[1]))
        table2.drawOn(self.c, init_pos_first[0],init_pos_first[1])
        # insert body of letter

        # p.wrapOn(self.c, self.width-70, self.height)
        # p.drawOn(self.c, *self.coord(20, voffset+48, mm))

    #----------------------------------------------------------------------
    def coord(self, x, y, unit=1):
        """
        # http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
        Helper class to help position flowables in Canvas objects
        """
        x, y = x * unit, self.height -  y * unit
        return x, y

    #----------------------------------------------------------------------
    def savePDF(self):
        """"""
        self.c.save()

#----------------------------------------------------------------------
if __name__ == "__main__":
    doc = LetterMaker("simple_table.pdf", "The MVP", 10)
    doc.createDocument()
    doc.savePDF()

    table_filename = "simple_table.pdf"

    # Now, after the output of table, merge with music pdf.
    input_file = PdfFileReader(open("1pagebach.pdf", "rb"))
    table_file = PdfFileReader(open(table_filename, "rb"))

    # Will configure if we need more tables
    input_page = input_file.getPage(0)

    # merge!
    table_page = table_file.getPage(0)
    input_page.mergePage(table_page)

    # output binary initialise
    output_file = PdfFileWriter()

    # output_file.addPage(PdfFileReader(BytesIO(imgTemp.getvalue())).getPage(0))
    output_file.addPage(input_page)

    # finally write "output" to document
    output_file.write(open("document-output.pdf","wb"))


