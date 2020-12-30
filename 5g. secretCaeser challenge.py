"""
Same instructions as original except:
- instead of methods write subroutines.
- Instead of create a new variable with no value, write create a new variable that references an empty string.
"""
plainText = "Hello World"

for letter in plainText:
	print(ord(letter), end=', ')

encrypted = ""

for letter in plainText:
	encrypted = encrypted + chr(ord(letter) + 10)

print("\nThe final value is:", encrypted)

