
import os

print(os.name)  # Prints "nt" in the case of windows


# This prints the list of functions that are available to us in the os module
# print(dir(os))
for function in dir(os):  # This presents the above line in a better way
    print(function)


# Working Directory
print(os.getcwd())  # This prints the Current Working Directory (CWD)

# TO CHANGE THE CURRENT WORKING DIRECTORY
os.chdir("C://")

# To List all the files in the Current Working Directory
print(os.listdir())  # You can specify the path in string in between the parenthesis

# This for loop checks whether the files end with py and prints accordingly
for file in os.listdir():

    # if file[len(file) - 2:] != "py":
    if file[-2:] != "py":  # This line does the same thing as the line above

        print(f'The folder {file} exists in the current working directory!')
    else:
        print(f'The file {file} exists in the current working directory!')


# To Make a Folder in the CWD
os.mkdir("OSTESTFOLDER")

# To Make Multiple Nested Directories
os.makedirs("This/That")

# To Rename a file in the CWD
# The first argument is the current name of the file and the second one is the new name of the file
os.rename("Name.py", "NewName.py")

# Reading/Getting Environment Variables
print(os.environ.get('PATH'))  # Gets all the environment variables paths
