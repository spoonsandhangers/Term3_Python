"""
A list is the closest thing to an Array that Python has
A 2D list is a list of lists.
This looks like:
my_list = [["this","is","list","one"],["this","is","list","two"]]

the list called my_list is made up of 2 sub lists:
["this","is","list","one"]
["this","is","list","two"]
These 2 lists are contained in square brackets and separated by a comma just
as if they were single elements.

A 2D list can contain as many sub lists as required.

remember all lists begin at index 0.
"""

# a regular list of strings
list_1D = ["This", "a", "1D", "list"]

# a 2D list
my_list = [["this", "is", "list", "one"], ["this", "is", "list", "two"]]

# you can separate the lists onto different lines so it is easier to read.

list_2D = [[1, 3, 5, 7, 9],
           [2, 4, 6, 8, 10],
           [100, 200, 300, 400, 500]]

# the list above list_2D contains 3 sub lists

"""
In Python you cannot declare the size of a list as you could in Java.
You can declare an empty list and then fill it with the amount of elements that
you require.
"""
# declare an empty list.
my_2D_list = []

# create a  few 1D lists
list_one = ['a', 'e', 'i', 'o', 'u']
list_two = ['b', 'c', 'd', 'f', 'g', 'h', 'j']
list_three = ['k', 'l', 'm', 'n']

# add the 1D lists to the empty list using the same
# append instruction you would use if they were single elements.

my_2D_list.append(list_one)
my_2D_list.append(list_two)
my_2D_list.append(list_three)

# my_2D_list now contains three sub lists
# this will print them out showing their list structure.
print(my_2D_list)

# the next thing to think about is how you address each element in this
# 2D list structure.
# each sublist is addressed as an element of the outer list.
# so the first sublist is my_2D_list[0]
# the 2nd sublist is my_2D_list[1] etc.
# This addresses the whole of the sublist not individual elements inside it
# look at the result of these print statements

print("This is the first element in the 2D list", my_2D_list[0])
print("This is the second element in the 2D list", my_2D_list[1])
print("This is the third element in the 2D list", my_2D_list[2])
print("")
# this printed out the sub lists

# To print out the individual elements in each sublist we use the same
# syntax, just adding another set of square brackets.
# The number in the second set represents the element in the sublist.

print("This is the first element in the first sublist", my_2D_list[0][0])
print("This is the first element in the second sublist", my_2D_list[1][0])
print("This is the second element in the third sublist", my_2D_list[2][1])
print("")

# as well as printing them out we can change them

# This changes the third element in the first list to the string "new element"
# Note you can only do this if there is already an element in that position.
# It cannot be used to add an element.
my_2D_list[0][2] = "new element"

print(my_2D_list)

# To find the length of the 2D list.  This will be the amount of sub lists
# that are contained in the list.

print("The length of the 2D list is:", len(my_2D_list))

# To find the length of each of the sub lists in the 2D list.

print("The length of the first sub list is:", len(my_2D_list[0]))
print("The length of the second sub list is:", len(my_2D_list[1]))
print("The length of the third sub list is:", len(my_2D_list[2]))

"""
The example in the code book shows a chess board.
To do this in Python:
"""
# declare an empty list called chessBoard
chessBoard = []
# declares a constant for the board size
BOARD_SIZE = 8

# nested for loops that create the board
# the outer loop creates the sub lists that represent the rows.
# the inner loop creates the elements in the sublists that represent the columns

for row in range(BOARD_SIZE):
	# adds a sub list to the main list
	chessBoard.append([])
	for column in range(BOARD_SIZE):
		# adds 2 underscores as each element in each sublist.
		# this represents an empty square on the board.
		chessBoard[row].append('__')

# this for loop prints out each of the sublists in the
# main list chessBoard.
print("")
for i in chessBoard:
	print(i)

# As we did before we can change the values in the list
# To represent the pieces on the board.
# set up some white pieces
chessBoard[0][0] = "WC" # row 0 column 0 white castle
chessBoard[0][1] = "WK" # row 0 column 1 white knight
chessBoard[1][0] = "WP" # row 1 column 0 white pawn
chessBoard[1][1] = "WP" # row 1 column 1 white pawn

# set up some black pieces
chessBoard[7][0] = "BC" # row 0 column 0 black castle
chessBoard[7][1] = "BK" # row 0 column 1 black knight
chessBoard[6][0] = "BP" # row 1 column 0 black pawn
chessBoard[6][1] = "BP" # row 1 column 1 black pawn

# print the status of the board now
print("")
for i in chessBoard:
	print(i)






