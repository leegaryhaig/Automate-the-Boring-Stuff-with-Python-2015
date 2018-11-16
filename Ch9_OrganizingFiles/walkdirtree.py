import os, sys

# the os.walk() function is passed a single string value: the path of a folder and can be used in a for loop to walk
# down a directory tree, similar to how the range function walks over a range of numbers. However, the os.walk() function
# will return 3 values on each iteration, a string of the current folders name, a list of strings of the folders in current
# folder and a list of strings of the files in the current folder.

# os.path.join('usr','bin', 'spam') to work on all operating systems

for folderName, subfolders, filenames in os.walk(str(sys.argv[1])):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE clear ' + folderName + ': ' + filename)


    print(' ')