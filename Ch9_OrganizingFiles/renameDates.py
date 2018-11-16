#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.
#Create a regex that matches files with the American date format.

import shutil, os, re

# shutil or shell utilities - allows you to copy, move rename and delete files in your python programs
# os or operating system - allows you to use operating system dependent functionality such as path,
# re or regular expressions - allows you to specify patterns of text that you may want to find or modify

datePattern = re.compile(r'''^(.*?) # Before date: Optionally(?) All characters (.*) before (^) the date
    ((0|1)?\d)-                     # Month: Optionally(?) First digit for month is either (0|1) with any digit (\d) following
    ((0|1|2|3)?\d)-                 # Day: Optionally(?) The first digit for day is either (0|1|2|3) 
    ((19|20)\d\d)                  # Year: The first two digits for year is either (19|20) with any two digits following
    (.*?)$                          # Afterdate: Optionally(?) all characters (.*) after ($) the date
    ''', re.VERBOSE)                #re.Verbose allows whitespace and comments in the regex string

# To keep the group numbers straight, try reading the regex from the beginning and count up each time you encounter an
# open parenthesis. Without thinking about the code, just write an outline of a regular expression

# datePattern = re.compile(r'''^(1) # Before date:
#    (2 (3) )-                      # Month:
#    (4 (5) )-                      # Day:
#    (6 (7) )-                      # Year:
#    (8)$                           # After date:

# Because mo.group(3) sits INSIDE mo.group(2), mo.group(2) includes the regex mo.group(3) regex.


# TODO: Loop over the files in the working directory
for amerFilename in os.listdir('./datesdata'):
    mo = datePattern.search(amerFilename)

# TODO: Skip files without dates
    if mo == None:
        continue

# TODO: Get the different parts of the filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)


    # TODO: Form the Euro style filename
    euroFilename = beforePart + '-' + dayPart + '-' + monthPart + '-' + yearPart + '-' + afterPart

    # TODO: get the Full Absolute File paths
    absWorkingDir = os.path.abspath('.') #store the current working directory in absWorkingDir
    amerFilename = os.path.join(absWorkingDir, 'datesdata', amerFilename) # stores path with new American date filename in amerFilename
    euroFilename = os.path.join(absWorkingDir, 'datesdata', euroFilename) # stores path with current Euro date filename in euroFilename

    # TODO: Rename the files
    print(amerFilename)
    print(euroFilename)
    shutil.move(amerFilename, euroFilename) #uncomment after testing, renaming files like this is very dangerous.