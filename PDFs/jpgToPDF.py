from PIL import Image
from PyPDF2 import PdfFileMerger
import os

image1 = Image.open('D:\\Privates Zeugs\\Persönliche_Daten\\Bürokratie\\Schulbesuchsbestaetigung_Lovetinsky.jpeg')
im1 = image1.convert('RGB')
im1.save('C:\\Users\\Dominik Lovetinsky\\Desktop\\SBB_Dominik_Lovetinsky.pdf')
path = 'D:\\HTL\\Werkstatt\\4AHET\\MANS\\Anlagenpruefung'

for file in os.listdir(path):
    if file.endswith('.jpg'):
        # print(path + file)
        img = Image.open(path + '\\' + file)
        img = img.convert('RGB')
        img.save(path + '\\' + file[:-4] + '.pdf')

merger = PdfFileMerger()

pdfs = [path + '\\' + str(n) + '.pdf' for n in range(1, 20)]

for pdf in pdfs:
    merger.append(pdf)

merger.write('D:\\HTL\\Werkstatt\\4AHET\\MANS\\Anlagenpruefung\\Anlagenpruefung_lovetinsky.pdf')
merger.close()
