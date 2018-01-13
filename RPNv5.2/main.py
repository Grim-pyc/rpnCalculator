import inputParser
import inputSolver


def printer(registerList):
	print('\n'*50)
	print("Shrapnitek Business RPN Calculator v5.1", '\n')
	for i in range(len(registerList)-1, -1, -1):
		print('', registerList[i])
	print()
	
registerList = ["0.0", "0.0", "0.0", "0.0"]

while True:
	printer(registerList)
	userInput = str(input("$ "))
        case = inputParser.parser(userInput)
        registerList = inputSolver.solver(registerList, userInput, case)
	
