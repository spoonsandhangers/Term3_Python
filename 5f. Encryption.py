"""
A character has an ascii value which is an integer.
To code a simple Ceasar cipher we can change these values by adding/subtracting from this value.
We can use a loop to iterate through a string and add or subtract a value from each characters ascii value.

"""
# This prints out the ascii value of the character a - ord()
print(ord("a"))
# This prints out the character represented by the ascii value 97 which is "a"
print(chr(97))

# this subroutine takes a string and an integer value as parameters
# it takes the string and adds the integer value to each of the characters ascii code
# it then saves each character in a new string and returns the result.

def encryptString(mystring, value):
	result = ""
	for letter in mystring:
		result = result + chr(ord(letter)+value)
	return result


# calls the subroutine and stores the return value in the variable cipher.
cipher = encryptString("abcdefg", 1)
print(cipher)






