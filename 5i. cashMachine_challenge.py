"""
This is one solution to the cash machine challenge.
It will be good to re run this when they start to do OOP and see how subtly different the code
is.
I have got around the local scope of the subroutines by declaring thst I will be using the global
variables at the start of the subroutines.  This is not the only way you can get around this.
You can also use parameters and return values.
The code loads the account number, pin and balance from the file each time it runs the menu and
saves them back to the file each time the balance is changed.
"""

accNo = ""
pin = ""
balance = 1000
loggedIn = False


def saveData():
	fileName = "user.txt"

	try:
		fout = open(fileName, "w")
	except OSError:
		print("Cannot open", fileName)
	else:
		user = accNo + "," + pin + "," + str(balance)
		userCode = ""
		for letter in user:
			userCode = userCode + chr(ord(letter)+10)
		fout.write(userCode + "\n")
		fout.close()
		print("Success!")


def getData():
	global accNo, pin, balance, loggedIn
	fileName = "user.txt"

	try:
		my_file = open(fileName, "r")
	except OSError:
		print("Cannot open", fileName)
	else:
		fileRead = my_file.readlines()
		userDecode = ""
		for line in fileRead:
			for letter in line:
				userDecode = userDecode + chr(ord(letter)-10)
		userDetails = userDecode.split(",")
		accNo = userDetails[0]
		pin = userDetails[1]
		balance = userDetails[2]
		# when the balance is read from the file it has the \n new line
		# character included.  This must be removed before you can cast it
		# to a float.
		balance = balance[:-1]
		print(balance)
		try:
			balance = float(balance)
		except ValueError:
			print("There has been an error loading the balance.")
		print(userDecode, userDetails)


# menu is an array of option that are printed out
# the return value is the option number as a string.
def menu():
	menuList = ["1. Login",
	            "2. Logout",
	            "3. Display Account Balance",
	            "4. Withdraw Funds",
	            "5. Deposit Funds",
	            "6. Exit"]

	for i in menuList:
		print(i)
	choice = input("\nEnter the number of your option: ")
	return choice


def optionOne():
	aNumber = input("Enter your account Number: ")
	apin = input("Enter your pin number: ")
	if aNumber == accNo:
		if apin == pin:
			return True
		else:
			print("Pin is incorrect.")
			optionOne()
	else:
		print("Account Number is incorrect.")
		optionOne()

def optionTwo():
	print("You have logged out")
	return False


def optionthree():
	print("Your balance is:", balance)


def optionfour():
	global balance
	print("Please enter the withdrawal amount:")
	try:
		amount = float(input())
	except ValueError:
		print("Please enter a valid number.")
		optionfour()
	else:
		if balance >= amount:
			balance = round(balance - amount, 2)
			saveData()
		else:
			print("Sorry you don't have enough money!")

def optionfive():
	global balance
	print("Please enter the deposit amount:")
	try:
		amount = float(input())
	except ValueError:
		print("Please enter a valid number.")
		optionfive()
	else:
		balance = round(balance + amount, 2)
		saveData()



def main():
	global loggedIn
	exitApp = False
	while not exitApp:
		getData()
		option = menu()
		if option == "1":
			loggedIn = optionOne()
		elif option == "2":
			loggedIn = optionTwo()
		elif option == "3":
			if loggedIn:
				optionthree()
			else:
				print("You must be logged in to view your balance.")
		elif option == "4":
			if loggedIn:
				optionfour()
			else:
				print("You must be logged in to withdraw funds.")
		elif option == "5":
			if loggedIn:
				optionfive()
			else:
				print("You must be logged in to deposit funds.")
		elif option == "6":
			exitApp = True



main()

