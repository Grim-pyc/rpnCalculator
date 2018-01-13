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
    elif (len(arg) != 0) and (arg[-1] == "e"):
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
    if isRegisterCommand(arg):
        case = "registerCommand"
    elif isMathOperator(arg):
        case = "mathOperator"
    elif isBitwiseOperator(arg):
        case = "bitwiseOperator"
    elif isTrigOperator(arg):
        case = "trigOperator"
    elif isUnaryOperator(arg):
        case = "unaryOperator"
    elif isNumber(arg):
        case = "Number"
    elif isFraction(arg):
        case = "Fraction"
    else:
        case = "Error"
    return case

tester = ("12.2", "12/2", "12.2e.2", "12/4e3", "12.2e3.12", "")
for i in tester:
    print(i, parser(i))