import openpyxl

# Puts example.xlsx into wb object
wb = openpyxl.load_workbook('example.xlsx')


def openxl():
    print(wb.sheetnames)
    print(type(wb))


def getsheets():
    sheet = wb['Sheet3']
    print(sheet)
    print(sheet.title)

getsheets()