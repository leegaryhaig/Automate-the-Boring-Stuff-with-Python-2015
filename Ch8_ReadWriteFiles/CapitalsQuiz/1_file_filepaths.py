import os

'''If you want your programs to work on all operating
systems, you will have to write your Python scripts to handle both cases.If you
pass it the string values of individual file and folder names in your path,
os.path.join() will return a string with a file path using the correct path
separators'''

# In interactive shell
# import os
# os.path.join('usr', 'bin', 'spam')

# The os.path.join() function is helpful if you need to create strings for filenames.
# For example, the following example joins names from a list of filenames to the end of a folder’s name
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('~', 'Users', 'glee', filename))


# Current working directory or cwd. You can get the current
# working directory as a string value with the os.getcwd() function and change it with os.chdir().

# Absolute Paths(begins with the root folder) vs. Relative Paths(Current working directory)
# There are also the dot (.) and dot-dot (..) folders. These are not real
# folders but special names that can be used in a path. A single period (“dot”)
# for a folder name is shorthand for “this directory.” Two periods (“dot-dot”)
# means “the parent folder.”

# Creating New Folders with os.makedirs()

# Handling Absolute and Relative Paths

# Calling os.path.abspath(path) will return a string of the absolute path of the arg, this is easy way
# to convert a relative path into absolute

# Calling os.path.isabs(path) will return True if the arg is absolute and False if its a relative path

# Calling os.path.relpath(path, start) will return a string of a relative path from the start path to path.
# if start is not provided the cwd is used as the start path

