import numpy as np
from TicTacToe2 import StateOfBoard

Tree = np.genfromtxt("SearchedTree.csv")
mainBoard = StateOfBoard()

def usermove():

        userin = raw_input("")
        inputOK = False
        while inputOK != True:
                if userin.isdigit():
                        if 0<=int(userin)<9:
                                inputOK = True
                if inputOK == False:
                        print("Please enter a number between 1 and 9.")
                        userin = raw_input("")


        mainBoard.move(int(userin)+1)

def algorithmMove():
	Possible = Tree[:,2]
	print(Possible[10000])
	Possible -=  10**10
	print(Possible[10000])
	Possible -= (mainBoard.History-10**10)
	print(str(Possible[10000])+"\t"+str(mainBoard.History-10**10))
	Possible = Possible[Possible>0]
	Possible = Possible[Possible<(10**mainBoard.NoTurn-1)]
	options = mainBoard.options()
	mainBoard.move(options[0])
	print(Possible[0])



print("Lets play a gameof TicTacToe.")
print(" x starts and you should insert a number between 0 and 9 \n corresponding to the field you want to play.")



while mainBoard.finished != True:

	mainBoard.displayState()
	usermove()
	algorithmMove()

print(mainBoard.symbol(mainBoard.Winner)+" has won the Game.")
