"""
Master challenge new instructions:
1. Create a subroutine that asks the user for the name of a the file they wish to write to.
	Concatenate ".html" to this filename and return this string as the filename.
2. Find some basic html online (3 or 4 lines is enough)
3. Write the html code to the file.
4. test the created webpage by opening it in chrome.
"""

def getFileName():
	myfile = input("Enter the name of the file to write to: ")
	return myfile + ".html"


# calls the filename subroutine.
fileName = getFileName()

try:
	fout = open(fileName, "w")
except OSError:
	print("Cannot open", fileName)
else:
	fout.write("<!DOCTYPE html>\n")
	fout.write("<html>\n<head>\n<title>File Writing</title></head>")
	fout.write("<body>\n<h1>File Writing Web Page</h1>\n")
	fout.write("<p>This is a webpage I have written to a file.</p>\n")
	fout.write("<p>I hope you like it!</p>\n")
	fout.write("</body>\n</html>\n")
	fout.close()
	print("Success!")
