#! Python 3
import PyPDF2

def extractText():
    pdf_file = open('meetingminutes.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdf_file)
    page_obj = pdfReader.getPage(0)
    print(page_obj.extractText())


def decryptPDF():
    pdf_file = open('encrypted.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdf_file)
    # You have to decrypt the PDF file before you can access the pages
    pdfReader.decrypt('rosebud')
    page_obj = pdfReader.getPage(0)
    print(page_obj.extractText())


# PyPDF2 does not have express functionality to write arbitrary text onto a PDF, instead you have to create a new PDF
# and copy data onto it from an existing document

#TODO: Open one or more PDF's(the source PDF) into PdfFileReader objects

#TODO: Create a new PdfFileReader object

#TODO: Copy pages from the PdfFileReader objects into the PdfFileWriter objects.

#TODO: Finally, use the PdfFileWriter object to output the PDF

def copyPDF():
    # Create file obj - You have to specify read binary, because...we're reading it, duh
    pdf1File = open('meetingminutes.pdf', 'rb')
    pdf2File = open('meetingminutes.pdf', 'rb')

    # Create the pdfFileReader object
    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
    pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

    # Create the pdfFileWriter object
    pdfWriter = PyPDF2.PdfFileWriter()

    for pageNum in range(pdf1Reader.numPages):
        page_obj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(page_obj)

    for pageNum in range(pdf2Reader.numPages):
        page_obj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(page_obj)

    # Create output - We have to specify write binary...because well...we're writing stuff, duh
    pdfOutputFile = open('combinedminutes.pdf', 'wb')
    pdfWriter.write(pdfOutputFile)
    # Remember that you have to close()  the files that are opened by open()
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()

def rotatePage():
    minutesFile = open('meetingminutes.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(minutesFile)
    page = pdfReader.getPage(0)
    page.rotateClockwise(90)

    # Create a pdfWriter object
    pdfWriter = PyPDF2.PdfFileWriter
    pdfWriter.addPage(page)

    # Create a new file to save the rotated PDF (remember you can't save over an existing file)
    rotateFile = open('rotatedminutes.pdf', 'wb')

    # Write to it using the PDFWriter object you just created
    pdfWriter.write(rotateFile)

    # Remember to close() out your open() files
    minutesFile.close()
    pdfWriter.close()

def overlayPage():
    minutesFile = open('meetingminutes.pdf')
