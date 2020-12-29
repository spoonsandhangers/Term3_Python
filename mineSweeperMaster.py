"""
new instructions for the master challenge
Using subroutines where appropriate.
1. allow the user 5 guesses, update the display after each guess.
2. After each guess tell the user if they are:
	Boiling hot - the row or column is correct
	Hot - The row or column is 1 away from the mine
	Warm - The row or column is 2 away from the mine
	Cold - The row or column is 3 or more away form the mine
3. Update the guessed location with a '1' and refresh the displayed grid after each wrong guess.
4. If the user guesses correctly, put an 'X' on the dispaly where the mine was located
	and congratulate them.
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
guess_number = 0

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


# checks if user guess is correct and gives hints
def checkUserGuess():
	global user_row, user_column, mine_row, mine_column
	if user_row == mine_row and user_column == mine_column:
		mineSweeperBoard[mine_row][mine_column] = 'X'
		return True
	elif user_row == mine_row or user_column == mine_column:
		print("You are Boiling hot!")
	elif user_row == mine_row + 1 or user_row == mine_row -1 or user_column == mine_column +1 or user_column == mine_column -1:
		print("You are Hot!")
	elif user_row == mine_row + 2 or user_row == mine_row -2 or user_column == mine_column +2 or user_column == mine_column -2:
		print("You are warm!")
	else:
		print("You are cold!")
	return False


def updateBoard(row,column):
	mineSweeperBoard[row][column] = '1'

# sets up the board
setUpBoard()
# prints out the board
printBoard()
# randommly places the mine
placeMine()
print(mine_row, mine_column)

# This while loop will run while guess is not true and guess number is less than 5
while not guess and guess_number < 5:
	userGuess()
	guess = checkUserGuess()
	if guess:
		print("Well done you have found it!")
	else:
		print("Please guess again")
		updateBoard(user_row,user_column)
		printBoard()
	guess_number += 1

# if guess is false after all the user guesses have gone this prints out a message.
if not guess:
	print("Unlucky this time!")
	print("Mine position", mine_row, mine_column)


#print(mine_row, mine_column)
#print(user_row,user_column)

