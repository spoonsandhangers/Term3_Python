"""
new instructions for the challenge
Using subroutines where appropriate.
1. declare an empty list to represent the minesweeper board
2. declare a constant for the row size of value 5
3. declare a constant for the column size of value 5
4. Use nested loops to fill the empty list full of 5 sub lists with 5 '0's in each.
5. Generate a random row for the mine between 0 and 4
6. Generate a random column for the mine between 0 and 4.
7. Display the minesweeper board full of '0's
8. Ask the user to guess where the mine is by entering a row and a column.
9. Check if the user guessed correctly and output an appropriate message.
10. Update the guessed location with a '1' and refresh the displayed grid.
"""
import random

# these are global variables
mineSweeperBoard = []
ROW = 5
COLUMN = 5
mine_row = 0
mine_column = 0
user_row = 0
user_column = 0
guess = False

# creates a board 5x5 using 2 nested for loops
# uses the global list mineSweeperBoard
# no return value is needed.

def setUpBoard():
	for row in range(ROW):
		# adds a sub list to the main list
		mineSweeperBoard.append([])
		for column in range(COLUMN):
			# adds 2 underscores as each element in each sublist.
			# this represents an empty square on the board.
			mineSweeperBoard[row].append('0')


# prints the board status.
def printBoard():
	for i in mineSweeperBoard:
		print(i)


# places a mine on the board
def placeMine():
	# so that we can use the global variables inside the subroutine
	# we use the global keyword.
	global mine_row
	global mine_column
	mine_row = random.randint(0, 4)
	mine_column = random.randint(0, 4)


# asks the user for a guess and updates the user_row and column variables
def userGuess():
	# so that we can use the global variables inside the subroutine
	# we use the global keyword.
	global user_row
	global user_column
	print("Please guess a row and column from 0 to 4:")
	user_row = int(input("Enter a row: "))
	user_column = int(input("Enter a column: "))


# checks if user guess is correct
def checkUserGuess():
	# use the global keyword so that the subroutine updates the global variables.
	global user_row, user_column, mine_row, mine_column
	# checks if the row and column of the user guess are the same as the
	# row and column of the mine.
	if user_row == mine_row and user_column == mine_column:
		return True
	print("Unlucky this time!")
	return False


def updateBoard(row,column):
	mineSweeperBoard[row][column] = '1'

# runs all the subroutines to play through the game once.
setUpBoard()
printBoard()
placeMine()
print(mine_row, mine_column)
userGuess()
guess = checkUserGuess()
updateBoard(user_row,user_column)
printBoard()






#print(mine_row, mine_column)
#print(user_row,user_column)

