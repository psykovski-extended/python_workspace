from PyPDF2 import PdfFileMerger
import os

dirs = os.scandir("C:\\Users\\Dominik Lovetinsky\\Downloads\\")

pdfs = ["C:\\Users\\Dominik Lovetinsky\\Downloads\\" + str(n) + '.pdf' for n in range(1, 340)]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
