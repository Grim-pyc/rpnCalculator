#inputSolver Module
#handles input solving for RPN Calculator v5.1
import math
from decimal import *

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
	registerList = shiftUp(registerList, arg)
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
	getcontext().prec = 39 #128-bit Quadruple Floating Point Support
	getcontext().clear_flags() #Clears flags from previous operation
	registerX = Decimal(registerList[0])
	registerY = Decimal(registerList[1])
	if arg == "**":
		xRegister = registerY ** registerX
		registerList = shiftDown(registerList, xRegister)
	elif arg == "%":
		xRegister = registerY % registerX
		registerList = shiftDown(registerList, xRegister)
	elif arg == "//":
		xRegister = registerY // registerX
		registerList = shiftDown(registerList, xRegister)
	elif arg == "*":
		xRegister = registerY * registerX
		registerList = shiftDown(registerList, xRegister)
	elif arg == "/":
		xRegister = registerY / registerX
		registerList = shiftDown(registerList, xRegister)
	elif arg == "+":
		xRegister = registerY + registerX
		registerList = shiftDown(registerList, xRegister)
	elif arg == "-":
		xRegister = registerY - registerX
		registerList = shiftDown(registerList, xRegister)
	else:
		print("This will never display")
	return registerList

def caseUnaryOperator(registerList, arg):
	getcontext().prec = 39 #256-bit Octuple Floating Point Support
	getcontext().clear_flags() #Clears flags from previous operation
	registerX = Decimal(registerList[0])
	if arg == "abs":
		xRegister = getcontext().abs(registerX)
		registerList = replace(registerList, xRegister)
	elif arg == "sqr":
		xRegister = getcontext().sqrt(registerX)
		registerList = replace(registerList, xRegister)
	elif arg == "cbr":
		xRegister = registerX ** (Decimal("1") / Decimal("3"))
		registerList = replace(registerList, xRegister)
	elif arg == "sq":
		xRegister = registerX ** Decimal("2")
		registerList = replace(registerList, xRegister)
	elif arg == "cb":
		xRegister = registerX ** Decimal("3")
		registerList = replace(registerList, xRegister)
	elif arg == "inv":
		xRegister = Decimal("1") / registerX
		registerList = replace(registerList, xRegister)
	elif arg == "log":
		xRegister = registerX.log10()
		registerList = replace(registerList, xRegister)
	elif arg == "ln":
		xRegister = registerX.ln()
		registerList = replace(registerList, xRegister)
	elif arg == "ex":
		xRegister = registerX.exp()
		registerList = replace(registerList, xRegister)
	else:
		print("This will never display")
	return registerList

def solver(registerList, arg, case):
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
