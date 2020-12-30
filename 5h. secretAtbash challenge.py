"""
The atBash encryption is where
a b c d e f g h i j k l m n o p q r s t u v w x y z
z y x w v u t s r q p o n m l k j i h g f e d c b a

a = z,  f = u, o = l etc.

To program this we can use the formula key = ord("z") + ord("a")
"""
# So this is an example of how this works before we do the challenge
# This creates the key
key = ord("z") + ord("a")

# this uses the key to convert a character into the code "s" becomes "h"
print(chr(key-ord("i")))

print(ord(" "))

"""
Using subroutines where appropriate:
1. Ask the user for a sentence
2. validate the input to make sure it does not contain a comma
	remove all spaces from the sentence.
3. Encrypt the sentence using the Atbash technique
4. output the final value of the encrypted data.
"""


def getSentence():
	text = input("Enter a sentence to encrypt: ")
	if "," in text:
		print("Please enter another sentence without a comma.\n")
		getSentence()
	return text


def atBash(my_text):
	result = ""
	key = ord("z") + ord("a")
	for letter in my_text:
		if letter != " ":
			result = result + chr(key-ord(letter))
	return result


my_text = getSentence()
cipher = atBash(my_text)
print(cipher)


