#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

# Functional argument that allows you to specify what file (using the name) to backup
def backuptoZip(folder):
    folder = os.path.abspath(folder) # Finds and saves the absolute path of specified folder in the 'folder' object

    # Figure out the filename this code should use based on what files already exists
    # Basename returns the tail end of a path, in this case it returns the actual folder name and the while loop
    # Adds a digit + .zip while the loop doesn't hit break.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # TODO: Create the ZIP File
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # TODO: Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        # Add all the files in this folder the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()
    print('Done.')

backuptoZip('.')
