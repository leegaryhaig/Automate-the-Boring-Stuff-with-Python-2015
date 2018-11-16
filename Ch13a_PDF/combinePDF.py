#! Python
import os, PyPDF2
cwdList = os.listdir()
matchList = []

pdfWriter = PyPDF2.PdfFileWriter()

# Looks for pdf files in the cwd and places them in match list
for i in range(len(cwdList)):
    if cwdList[i].endswith('.pdf'):
        matchList.append(cwdList[i])

# TODO: Loop through all of the PDF files
for i in range(len(matchList)):
    pdfFile = open(matchList[i], 'rb')

    pdfReader = PyPDF2.PdfFileReader(pdfFile)

    # TODO: Copy all of the pages after the 1rst and save it pdfWriter
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# TODO: Save all of the pages into a master
outputFile = open('master.pdf', 'wb')

pdfWriter.write(outputFile)
pdfFile.close()
outputFile.close()
