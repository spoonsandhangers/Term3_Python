"""
New wording for challenge
Using subroutines where appropriate:
1. Create a global variable to hold the file name shopping_list.txt
2. Use try/except/else blocks to
	- open the file in writing mode.
	- write 3 items to your shopping_list file each on separate lines.
	- close the file and print a message to tell the user that it was a success.

"""

fileName = "shopping_list.txt"

try:
	fout = open(fileName, "w")
except OSError:
	print("Cannot open", fileName)
else:
	fout.write("Bread\n")
	fout.write("Milk\n")
	fout.write("Sugar\n")
	fout.close()
	print("Success!")

