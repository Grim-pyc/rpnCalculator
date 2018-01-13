import math

tupleOfSupportedOperators = ("**", "*", "/", "//", "%", "+", "-")
tupleOfSupportedCommands = ("clx", "cls", "up", "down", "swap")
tupleOfSupportedDigits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".")

errorMessage1 = "ERROR: INVALID INPUT \n\nPlease only use supported operators and commands"
errorMessage2 = "ERROR: DIVIDE BY ZERO"
errorMessage3 = "ERROR: SYNTAX ERROR"
errorMessage4 = "ERROR: OVERFLOW ERROR"

def caseWhiteSpace():
	print("White Space")

def caseOperators(userInput, xx, yy, zz, tt):
	global x
	global y
	global z
	global t
	if (userInput == "**"):
		x,y,z,t = yy**xx, zz, tt, tt
	elif (userInput == "*"):
		x,y,z,t = yy*xx, zz, tt, tt
	elif (userInput == "/"):
		if (xx == 0.0):
			errorDisplayer(errorMessage2)
		else:
			x,y,z,t = yy/xx, zz, tt, tt
	elif (userInput == "//"):
		x,y,z,t = yy//xx, zz, tt, tt
	elif (userInput == "%"):
		x,y,z,t = yy%xx, zz, tt, tt
	elif (userInput == "+"):
		x,y,z,t = yy+xx, zz, tt, tt
	elif (userInput == "-"):
		x,y,z,t = yy-xx, zz, tt, tt
	
def caseCommands():
	print("Commands")
	
def caseNumber(userInput, xx, yy, zz, tt):
	global x
	global y
	global z
	global t
	x,y,z,t = float(userInput), xx, yy, zz
	
def errorDisplayer(errorMessage):
	print('\n'*50)
	print(errorMessage, end='\n\n')
	input("Enter any value to continue ")
	
def RPNCalculator():
	global x 
	global y
	global z
	global t
	x,y,z,t = 0.0,0.0,0.0,0.0
	
	while True:
		print('\n'*50)
		print("Shrapnitek Business RPN Calculator v2", end='\n\n')
		print('',t,z,y,x, sep='\n ', end='\n\n')
		userInput = str(input("$ "))
		if (userInput.strip() == ""):
			caseWhiteSpace()
			continue
		elif (userInput.strip() in tupleOfSupportedOperators):
			caseOperators(userInput, x, y, z, t)
			continue
		elif (userInput.strip().lower() in tupleOfSupportedCommands):
			caseCommands()
			continue
		else:
			for i in range(0, len(userInput.strip()), 1):
				if (userInput.strip()[i] not in tupleOfSupportedDigits):
					isError = True #If the conditional fails, isError is set to false and the loop is broken
					errorDisplayer(errorMessage1)
					break
				else:
					isError = False #By default isError is set to false. Cannot be set to true once loop breaks
			if (userInput.count(".") not in (0, 1)): #Checks if number has two or more decimal points
				isError = True
				errorDisplayer(errorMessage3)
			if (not isError):
				caseNumber(userInput, x, y, z, t)
RPNCalculator()