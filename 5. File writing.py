"""
Important things to note when file reading and writing.
- You should open the file, carry out the process, close the file.
- files left open can cause problems.

The files created will be in the same directory as the python file
unless an absolute path is specified.

advanced:
You should use a try except block when writing or reading to files
you can use an else block after an except block.  This code will run if an exception isn't thrown.
"""
# variable filename stores the name of the file we are going to create
fileName = "output.txt"

# a try except else block is used to write the code.
try:
	# the file is opened using the open function.  This takes 2 parameters
	# the filename and either w,a or r. w = write, a = append, r = read.
	fout = open(fileName, "w")
except OSError:
	# This exception is thrown if the file cannot be created.
	print("Cannot open", fileName)
else:
	# if the code in the try block executes correctly this code will also run
	# putting it in this else block stops an exception being thrown for other code errors.
	# The \n at the end of the text is a newline character.
	# Each string will be written on a separate line
	fout.write("hello, world!\n")
	fout.write("hope you have a great day!\n")
	# this closes the file.
	fout.close()
	print("Success!")

"""
The above code used "w" in the open function.  Using this will erase anything that is already in the file.
To add to the file use "a" to append more text to the file.
"""

fileName1 = "passwords.txt"
name = "sarah"
password = "letmein"
name2 = "bob"
password2 = "helloareyouthere"

try:
	# "a" is used so this is adding to the file.
	fout = open(fileName1, "a")
except OSError:
	# This exception is thrown if the file cannot be created.
	print("Cannot open", fileName)
else:
	# writes the name and password to the first line of the file separated by a comma.
	# note that the + concatenation operator is used not the comma as the function write
	# only accepts one argument/parameter.
	fout.write(name + ",")
	fout.write(password + "\n")
	# this closes the file.
	fout.close()
	print("Success!")

# we can then add another line to the same file, this would normally be done in a more efficient
# way using a subroutine so that the code is not repeated, but this is just to show how append works

try:
	# "a" is used so this is adding to the file.
	fout = open(fileName1, "a")
except OSError:
	# This exception is thrown if the file cannot be created.
	print("Cannot open", fileName)
else:
	# writes the name and password to the first line of the file separated by a comma.
	# note that the + concatenation operator is used not the comma as the function write
	# only accepts one argument/parameter.
	fout.write(name2 + ",")
	fout.write(password2 + "\n")
	# this closes the file.
	fout.close()
	print("Success!")

# if you open the text file that has been created you will see it has 2 lines
# each line has a name then a comma then the password.



