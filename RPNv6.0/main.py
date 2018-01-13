import inputParser
import inputSolver
import gui
import Tkinter

#for i in range(len(registerList)-1, -1, -1):
                printerGrid = Tkinter.Label(text=registerList[i]).grid(row=i, column=0)



def printer(registerList):
	print('\n'*50)
	print("Shrapnitek Business RPN Calculator v5.1", '\n')
	for i in range(len(registerList)-1, -1, -1):
		print('', registerList[i])
	print()
	
registerList = ["0.0", "0.0", "0.0", "0.0"]
def runCalc(regsiterList, userInput):
        case = inputParser.parser(userInput)
        registerList = inputSolver.solver(registerList, userInput, case)
