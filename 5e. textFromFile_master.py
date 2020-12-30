"""
Continuing from following challenge and using subroutines where appropriate:
1. Create a text file with the following data:
James,Jones,01/01/99
Sarah,Smith,12/12/99
Bobby,Ball,04/04/99
Harry.Hall,06/06/99
2. Create a subroutine to ask the user for the name of the file that they wish to read from
3. Use a loop to read and output each line.
"""


def getFileName():
	my_file = input("What is the name of the file you would like to read from?: ")
	return my_file + ".txt"


the_file = getFileName()

try:
	# opens the file
	fileName = open(the_file, "r")
except IOError as e:
	# the exception is stored in the variable e
	print("The exception", e, "was raised.")
else:
	fileRead = fileName.readlines()
	for line in fileRead:
		print(line, end="")
	fileName.close()
