#inputParser Module
#handles input parsing for RPN Calculator v5.1

def isRegisterCommand(arg):
	# Checks argument against a tuple to see if argument is a Register Command
    registerCommands = ("clx", "cls", "swap", "up", "down", "")
    if arg in registerCommands:
        return True
    else:
        return False

def isMathOperator(arg):
	# Checks argument against a tuple to see if argument is a math Operator
    mathOperators = ("**", "%", "//", "*", "/", "+", "-")
    if arg in mathOperators:
        return True
    else:
        return False
    
def isUnaryOperator(arg):
	# Checks argument against a tuple to see if argument is a unary operator
    unaryOperators = ("abs", "sqr", "cbr", "sq", "cb", "inv", "log", "ln", "ex")
    if arg in unaryOperators:
        return True
    else:
        return False
    
def isNumber(arg):
	# Determines if argument is a valid number
	# Instead of parsing the argument and checking for half a dozen exceptions, this code:
	# Attempts to convert argument into float using a try except statement.
	# If conversion fails, argument is not a valid number
	try:
		float(arg)
		boolean = True
	except:
		boolean = False
	finally:
		return boolean
    
def parser(arg):
	# Using the above functions to determine the case of argument
	if isNumber(arg):
		case = "number"
	elif isRegisterCommand(arg):
		case = "registerCommand"	
	elif isMathOperator(arg):
		case = "mathOperator"
	elif isUnaryOperator(arg):
		case = "unaryOperator"
	elif isMemoryCommand(arg):
            case = "memoryCommands" 
	else:
		case = "error"
	return case

def isMemoryCommand (arg):
    #Determines if argument is a Variable Command
    memoryCommands = ("sto", "STO", "rcl", "RCL")
    if arg in memoryCommands:
        return True
    else:
        return False 
