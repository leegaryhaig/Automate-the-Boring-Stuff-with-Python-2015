import openpyxl

# OpenPyXL supports creating bar, line, scatter, and pie charts using the data in a sheet’s cells. To make a chart
# 1. Create a Reference object from a rectangular selection of cells.
# 2. Create a Series object by passing in the Reference object.
# 3. Create a Chart object.
# 4. Append the Series object to the Chart object.
# 5. Add the Chart object to the Worksheet object, optionally specifying which cell the top left corner of the chart
#    should be positioned.

# Reference Objects require some explaining. Reference objects are created by calling the openpyxl.chart.Reference()
# function and passing three arguments:
# 1. The Worksheet object containing your chart data.
# 2. A tuple of two integers, representing the top-left cell of the rectangular selection of cells containing your chart
#    data: The first integer in the tuple is the row, and the second is the column. Note that 1 is the first row, not 0.
# 3. A tuple of two integers, representing the bottom-right cell of the rectangular selection of cells containing your
#    chart data: The first integer in the tuple is the row, and the second is the column.

## INTERACTIVE SHELL EXAMPLE ##

wb = openpyxl.Workbook()
sheet = wb.active

for i in range(1, 11):
    sheet['A' + str(i)] = i  # Creates some data in cells A1-A11, 1 to 11

ref_obj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)  # The cells where data lives
series_obj = openpyxl.chart.Series(ref_obj, title='First Series')  # Series_object will hold the reference object

chart_obj = openpyxl.chart.BarChart()  # assign chart type to the chart_obj
chart_obj.title = 'My Chart'
chart_obj.append(series_obj)  # Include the series object into chart object
sheet.add_chart(chart_obj, 'C5')  # Add chart to sheet and the top left of the chart will start on cell 'C5'

wb.save('sampleChart.xlsx')

