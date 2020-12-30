"""
File reading
Same process as writing:
open, read the contents of the file, close the file.

This should also be done in try/except/else blocks
"""
try:
	# opens the file
	myFile = open("passwords.txt", "r")
except IOError as e:
	# the exception is stored in the variable e
	print("The exception", e, "was raised.")
else:
	# The file is read into the variable fileRead
	fileRead = myFile.readlines()
	# A for loop can be used to read each line in turn
	for line in fileRead:
		print(line, end="")

	# you can also use a for loop to split each line into a list by a separator
	# in this case the comma, and append it to another list
	# this creates a 2D list. The line breaks will be included in the final string.
	data = []
	for line in fileRead:
		data.append(line.split(","))

	# closes the file.
	myFile.close()

# prints the 2D list that was created.
print(data)

