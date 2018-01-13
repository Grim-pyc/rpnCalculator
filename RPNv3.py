import math

registers = [0.0, 0.0, 0.0, 0.0]
commands = ("", "cls", "clx", "up", "down", "swap")
operators = ("**", "*", "/", "//", "%", "+", "-")
digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "e")

errorMessage1 = "ERROR: INVALID INPUT \n\nPlease only use supported operators and commands"
errorMessage2 = "ERROR: DIVIDE BY ZERO"
errorMessage3 = "ERROR: SYNTAX ERROR"
errorMessage4 = "ERROR: OVERFLOW ERROR"

def errorDisplayer(errorMessage):
	print('\n'*50)
	print(errorMessage, end='\n\n')
	input("Enter any value to continue ")
	
def printer(input_reg):
	print('\n'*50)
	print("Shrapnitek Business RPN Calculator v3", '\n')
	for i in range(0, len(input_reg), 1):
		print('', input_reg[i])
	print()

def parser(Input):
	formattedInput = Input.strip().lower()
	if formattedInput in commands:
		case = "command"
	elif formattedInput in operators:
		case = "operator"
	else:
		for i in formattedInput:
			if i not in digits:
				error = True
				break
			else:
				error = False
				
		if formattedInput.count(".") not in (0, 1):
			Error = True
		elif formattedInput[-1] == "e":
			Error = True
			
		if error == False:
			case = "number"
		else:
			case = "error"
			errorDisplayer(errorMessage1)
	return case

def caseCommand(Input, registers):
	formattedInput = Input.strip().lower()
	if formattedInput == "":
		registers.insert(1, registers[0])
		registers.pop()

def caseNumber(Input, registers):
	formattedInput = Input.strip().lower()
	registers.insert(0, Input)
	registers.pop()
	
while True:
	printer(registers)
	userInput = str(input("$ "))
	case = parser(userInput)
	
	if case == "command":
		registers = caseCommand(userInput, registers)
	elif case == "operator":
		registers = caseOperator()
	elif case == "number":
		registers = caseNumber(userInput, registers)
	elif case == "error":
		pass 