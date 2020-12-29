"""
instructions for basic challenge
1. create a 2D array of size 3 x 3.  Each element in each of the sublists should be an '_'
	This represents a blank board.
2. Display this blank board
3. Ask the user to input a name for player 1 and 2.
4. Indicate whose turn it is and allow the user to input a row and a column to enter their 'X' or 'O'
5. Add this to the board and display it. Do not allow the user to choose a position that has already been taken.
6. Program a check check for ONE winning combination and prove it works
7. Tell the user someone has won.

instructions for master challenge
1. Allow the user to play another game, tracking how many games each competitor has won.
2. Check the board for any winning combinations after each move.
3. Alternate which player starts first.
4. Extension - make the game a single player vs CPU (the level of intelligence is up to you).

This code is for the full 2 player game.
I have not coded the player vs CPU version.
"""
board = []
scoreBoard = []
BOARD_SIZE = 3
turn = 0
game = 1

def buildBoard():
	global board
	board = []
	for i in range(BOARD_SIZE):
		board.append([])
		for j in range(BOARD_SIZE):
			board[i].append('_')



def printBoard():
	for i in board:
		print(i)


def userNames():
	player1 = input("Player one please enter your name: ")
	player2 = input("Player two please enter your name: ")

	scoreBoard.append([player1, 0])
	scoreBoard.append([player2, 0])
	return [player1,player2]

def check(row, column, symbol):
	if row == 0 and column == 0:
		if board[1][1] == symbol and board[2][2] == symbol:
			return True
		elif board[0][1] == symbol and board[0][2] == symbol:
			return True
		elif board[1][0] == symbol and board[2][0] == symbol:
			return True

	elif row == 0 and column == 1:
		if board[0][0] == symbol and board[0][2] == symbol:
			return True
		elif board[1][1] == symbol and board[2][1] == symbol:
			return True

	elif row == 0 and column == 2:
		if board[1][1] == symbol and board[2][0] == symbol:
			return True
		elif board[0][0] == symbol and board[0][1] == symbol:
			return True
		elif board[1][2] == symbol and board[2][2] == symbol:
			return True

	elif row == 1 and column == 0:
		if board[1][1] == symbol and board[1][2] == symbol:
			return True
		elif board[0][0] ==symbol and board[2][0] == symbol:
			return True

	elif row == 1 and column == 1:
		if board[0][2] == symbol and board[2][0] == symbol:
			return True
		elif board[0][0] == symbol and board[2][2] == symbol:
			return True
		elif board[1][0] == symbol and board[1][2] == symbol:
			return True

	elif row == 1 and column == 2:
		if board[1][0] == symbol and board[1][1] == symbol:
			return True
		elif board[0][2] == symbol and board[2][2] == symbol:
			return True

	elif row == 2 and column == 0:
		if board[2][1] == symbol and board[2][2] == symbol:
			return True
		elif board[1][0] == symbol and board[0][0] == symbol:
			return True
		elif board[1][1] == symbol and board[0][2] == symbol:
			return True

	elif row == 2 and column == 1:
		if board[2][0] == symbol and board[2][2] == symbol:
			return True
		elif board[0][1] == symbol and board[1][1] == symbol:
			return True

	elif row == 2 and column == 2:
		if board[2][0] == symbol and board[2][1] == symbol:
			return True
		elif board[1][2] == symbol and board[0][2] == symbol:
			return True

	return False


def checkDuplicates(row, column):
	if board[row][column] == '_':
		return True
	else:
		return False

def getPosition(player):
	row = int(input(player + " enter a row number 0 - 2"))
	column = int(input(player + " enter a column number 0 - 2"))
	return [row, column]

def crossTurn(row, column):
	if checkDuplicates(row, column):
		board[row][column] = 'X'
		return True
	else:
		print("position already taken!")
		return False


def noughtTurn(row, column):
	if checkDuplicates(row, column):
		board[row][column] = 'O'
		return True
	else:
		print("position already taken!")
		return False

def playGame(players):
	global game
	won = False
	#players = userNames()
	buildBoard()
	printBoard()

	if game % 2 == 0:
		for i in range(4):
			player_one = getPosition(players[0])
			crossTurn(player_one[0], player_one[1])
			printBoard()
			won = check(player_one[0], player_one[1], 'X')
			if won:
				print(players[0] + " You have won!")
				scoreBoard[0][1] += 1
				break
			player_two = getPosition(players[1])
			noughtTurn(player_two[0], player_two[1])
			printBoard()
			won = check(player_two[0], player_two[1], 'O')
			if won:
				print(players[1] + " You have won!")
				scoreBoard[1][1] += 1
				break
			if i == 4:
				print("It's a draw!")

	else:
		for i in range(5):
			player_two = getPosition(players[1])
			noughtTurn(player_two[0], player_two[1])
			printBoard()
			won = check(player_two[0], player_two[1], 'O')
			if won:
				print(players[1] + " You have won!")
				scoreBoard[1][1] += 1
				break
			player_one = getPosition(players[0])
			crossTurn(player_one[0], player_one[1])
			printBoard()
			won = check(player_one[0], player_one[1], 'X')
			if won:
				print(players[0] + " You have won!")
				scoreBoard[0][1] += 1
				break
			if i == 4:
				print("It's a draw!")


def menu(players):
	global game
	play = True
	while play:
		playGame(players)
		print(scoreBoard)
		answer = input("Another game? Type 'n' to exit ").lower()
		if answer == 'n':
			play = False
		game += 1


players = userNames()
menu(players)






