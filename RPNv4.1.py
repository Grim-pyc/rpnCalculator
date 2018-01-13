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

def isBitwiseOperator(arg):
    bitwiseOperators = ("<<", ">>", "&", "|", "~", "^")
    if arg in bitwiseOperators:
        return True
    else:
        return False

def isTrigOperator(arg):
    trigRatios = ("sin", "cos", "tan", "csc", "sec", "cot")
    arcTrigRatios = ("asin", "acos", "atan", "acsc", "asec", "acot")
    if arg in trigRatios + arcTrigRatios:
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

def isImproperFraction(arg):
    boolean = True
    for i in arg.split("/"):
        if not isNumber(i):
            boolean = False
    if arg.count("/") != 1:
        boolean = False
    return boolean

def isMixedFraction(arg):
    boolean = True
    for i in arg.split("."):
        if not isNumber(i):
            boolean = False
    if arg.count(".") != 2:
        boolean = False
    return boolean
        
def isFraction(arg):
    if isImproperFraction(arg):
        return True
    elif isMixedFraction(arg):
        return True
    else:
        return False
    
def parser(arg):
	if isNumber(arg):
		case = "number"
	elif isFraction(arg):
		case = "fraction"
	elif isRegisterCommand(arg):
		case = "registerCommand"	
	elif isMathOperator(arg):
		case = "mathOperator"
	elif isUnaryOperator(arg):
		case = "unaryOperator"
	elif isTrigOperator(arg):
		case = "trigOperator"
	elif isBitwiseOperator(arg):
		case = "bitwiseOperator"
	else:
		case = "error"
	return case
'''
tester = ("12.2", "12/2", "12.2e.2", "12/4e3", "12.2e3.12")
for i in tester:
    print(i, parser(i))
'''

def shiftDown(registerList, xRegister):
	registerList[:2] = [xRegister]
	registerList[3:] = [registerList[2]]
	return registerList

def shiftUp(registerList, xRegister):
	registerList[:0] = [xRegister]
	registerList[4:] = []
	return registerList

def caseNumber(registerListOld, arg):
	registerListNew = shiftUp(registerListOld, arg)
	return registerListNew

def caseFraction(registerListOld, arg):
	pass

def caseRegisterCommand(registerListOld, arg):
	if arg == "":
		xRegister = registerListOld[0]
		registerListNew = shiftUp(registerListOld, xRegister)
	elif arg == "clx":
		registerListOld[:1] = []
		registerListOld[3:] = [registerListOld[2]]
		registerListNew = registerListOld
	elif arg == "cls":
		pass
	elif arg == "swap":
		pass
	elif arg == "up":
		pass
	elif arg == "down":
		pass
	else:
		print("This will never display")
	return registerListNew
	
def solver(registerListOld, arg):
	case = parser(arg)
	if case == 'number':
		registerListNew = caseNumber(registerListOld, arg)
	elif case == 'fraction':
		registerListNew = caseFraction(registerListOld, arg)
	elif case == 'registerCommand':
		registerListNew = caseRegisterCommand(registerListOld, arg)
	elif case == 'mathOperator':
		registerListNew = caseMathOperator(registerListOld, arg)
	elif case == 'unaryOperator':
		registerListNew = caseUnaryOperator(registerListOld, arg)
	elif case == 'trigOperator':
		registerListNew = caseTrigOperator(registerListOld, arg)
	elif case == 'bitwiseOperator':
		registerListNew = caseBitwiseOperator(registerListOld, arg)
	else:
		print("error")
	return registerListNew




registerList = ["12", "13", "14", "15"]
print(solver(registerList, "clx"))
























