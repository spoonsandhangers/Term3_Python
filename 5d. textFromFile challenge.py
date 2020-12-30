"""
Using subroutines where appropriate:
1. create a text file with the following data:
James,Jones,01/01/99
2. Create a subroutine to read a single line from a text file and output it to the user.
"""

try:
	# opens the file
	myFile = open("reading.txt", "r")
except IOError as e:
	# the exception is stored in the variable e
	print("The exception", e, "was raised.")
else:
	fileRead = myFile.readlines()
	for line in fileRead:
		print(line, end="")
	myFile.close()
