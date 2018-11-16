#! Python 3
# Program walks through the folder tree and searches for files with a certain file extension such as .pdf or .png and
# copy these files to a new folder

import os, re, zipfile
from shutil import copy2

# Regex for find file that end in .txt, .png, or .pdf
fileType = re.compile(r'((.txt)|(.png)|(.pdf))$')

# regexTest = ['test.png', 'test.txt', 'test.pdf']
#
# for values in regexTest:
#     check = fileType.search(values)
#     print(check)

directory = '/Users/irt/Desktop/selectivecopy'

def selectiveCopy(pathtoSearch):
    pathtoSearch = os.path.abspath(pathtoSearch)
    print(pathtoSearch)
    pathBase = os.path.basename(pathtoSearch)
    pathDir = os.path.dirname(pathtoSearch)

    #TODO: if there is not directory Create the folder where the copied files are saved
    if not os.path.exists(directory):
        os.makedirs(directory)
        print('Creating folder: ' + pathBase)

    #TODO: walk through the specified directory to copy
    for foldername, subfolders, filenames in os.walk(pathtoSearch):
        print('Looking through %s...for txt, png, and pdf files' % foldername)

        for subfolder in subfolders:
            print('Looking through %s...for txt, png, and pdf files' % subfolder)

        # TODO: If there is a fileType regex match then copy that file and paste it in given location
        for filename in filenames:
            mo = bool(fileType.search(filename))

            if mo is True:
                try:
                    print(os.path.join(pathtoSearch, filename) + ' is a match and will be copied to selective copy')
                    filename = os.path.join(pathtoSearch, filename)
                    copy2(filename, directory)
                except FileNotFoundError as e:
                    print(filename + ' Cannot be found')
                except Exception as e:
                    print(e)
            else:
                print(filename + '...is invalid')
                break


selectiveCopy('/Users/irt/Downloads')









