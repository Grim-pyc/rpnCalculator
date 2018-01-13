
def isRegisterCommand(arg):
    registerCommands = ("clx", "cls", "swap", "up", "down", "")
    if arg in registerCommands:
        return True
    else:
        return False

def isMathOperator(arg):
    mathOperators = ("**", "%", "//", "*", "/", "+", "-")
    if arg in mathOperators:
        return True
    else:
        return False
    
def isUnaryOperator(arg):
    unaryOperators = ("abs", "sqr", "cbr", "sq", "cb", "inv", "log", "ln", "ex")
    if arg in unaryOperators:
        return True
    else:
        return False
    
def isNumber(arg):
    Digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "e")
    boolean = True
    for i in range(0, len(arg)):
        if arg[i] not in Digits:
            boolean = False
    if ("e" in arg) and ("." in arg.split("e")[-1]):
        boolean = False
    elif arg == "":
        boolean = False
    elif arg[-1] == "e":
        boolean = False
    elif arg.count(".") > 1:
        boolean = False
    elif arg.count("e") > 1:
        boolean = False
    return boolean
    
def parser(arg):
	if isNumber(arg):
		case = "number"
	elif isRegisterCommand(arg):
		case = "registerCommand"	
	elif isMathOperator(arg):
		case = "mathOperator"
	elif isUnaryOperator(arg):
		case = "unaryOperator"
	else:
		case = "error"
	return case

def shiftDown(registerList, xRegister):
	registerList[:2] = [xRegister]
	registerList[3:] = [registerList[2]]
	return registerList

def shiftUp(registerList, xRegister):
	registerList[:0] = [xRegister]
	registerList[4:] = []
	return registerList

def replace(registerList, xRegister):
	registerList[0:1] = [xRegister]
	return registerList
	
def caseNumber(registerList, arg):
	registerList = shiftUp(registerList, float(arg))
	return registerList

def caseRegisterCommand(registerList, arg):
	if arg == "":
		xRegister = registerList[0]
		registerList = shiftUp(registerList, xRegister)
	elif arg == "clx":
		registerList[:1] = []
		registerList[3:] = [registerList[2]]
	elif arg == "cls":
		registerList[:] = list(["0.0"] * 4)
	elif arg == "swap":
		tempRegister = registerList[1]
		registerList[1:2] = []
		registerList[:0] = [tempRegister]
		del tempRegister
	elif arg == "up":
		registerList[:0] = [registerList[3]]
		registerList[4:] = []
	elif arg == "down":
		registerList[4:] = [registerList[0]]
		registerList[:1] = []
	else:
		print("This will never display")
	return registerList

def caseMathOperator(registerList, arg):
	if arg == "**":
		xRegister = float(registerList[1]) ** float(registerList[0])
		registerList = shiftDown(registerList, xRegister)
	elif arg == "%":
		xRegister = float(registerList[1]) % float(registerList[0])
		registerList = shiftDown(registerList, xRegister)
	elif arg == "//":
		xRegister = float(registerList[1]) // float(registerList[0])
		registerList = shiftDown(registerList, xRegister)
	elif arg == "*":
		xRegister = float(registerList[1]) * float(registerList[0])
		registerList = shiftDown(registerList, xRegister)
	elif arg == "/":
		xRegister = float(registerList[1]) / float(registerList[0])
		registerList = shiftDown(registerList, xRegister)
	elif arg == "+":
		xRegister = float(registerList[1]) + float(registerList[0])
		registerList = shiftDown(registerList, xRegister)
	elif arg == "-":
		xRegister = float(registerList[1]) - float(registerList[0])
		registerList = shiftDown(registerList, xRegister)
	else:
		print("This will never display")
	return registerList

def caseUnaryOperator(registerList, arg):
	if arg == "abs":
		xRegister = math.fabs(float(registerList[0]))
		registerList = replace(registerList, xRegister)
	elif arg == "sqr":
		xRegister = math.sqrt(float(registerList[0]))
		registerList = replace(registerList, xRegister)
	elif arg == "cbr":
		xRegister = float(registerList[0]) ** (1/3)
		registerList = replace(registerList, xRegister)
	elif arg == "sq":
		xRegister = float(registerList[0]) ** 2
		registerList = replace(registerList, xRegister)
	elif arg == "cb":
		xRegister = float(registerList[0]) ** 3
		registerList = replace(registerList, xRegister)
	elif arg == "inv":
		xRegister = 1 / float(registerList[0])
		registerList = replace(registerList, xRegister)
	elif arg == "log":
		xRegister = math.log10(float(registerList[0]))
		registerList = replace(registerList, xRegister)
	elif arg == "ln":
		xRegister = math.log(float(registerList[0]))
		registerList = replace(registerList, xRegister)
	elif arg == "ex":
		xRegister = math.exp(float(registerList[0]))
		registerList = replace(registerList, xRegister)
	else:
		print("This will never display")
	return registerList

def solver(registerList, arg):
	case = parser(arg)
	if case == 'number':
		registerList = caseNumber(registerList, arg)
	elif case == 'fraction':
		registerList = caseFraction(registerList, arg)
	elif case == 'registerCommand':
		registerList = caseRegisterCommand(registerList, arg)
	elif case == 'mathOperator':
		registerList = caseMathOperator(registerList, arg)
	elif case == 'unaryOperator':
		registerList = caseUnaryOperator(registerList, arg)
	elif case == 'trigOperator':
		registerList = caseTrigOperator(registerList, arg)
	else:
		print("error")
	return registerList

def printer(registerList):
	print('\n'*50)
	print("Shrapnitek Business RPN Calculator v5", '\n')
	for i in range(len(registerList)-1, -1, -1):
		print('', registerList[i])
	print()
	
registerList = ["0.0", "0.0", "0.0", "0.0"]

while True:
	printer(registerList)
	userInput = str(input("$ "))
	registerList = solver(registerList, userInput)























