import numpy as np
from TicTacToe2 import StateOfBoard

Tree = np.genfromtxt("SearchedTree.csv")
mainBoard = StateOfBoard()

def usermove():

        userin = raw_input("")
        inputOK = False
        options = mainBoard.options()

        while inputOK != True:
                if userin.isdigit():
                        if 0<=int(userin)<9:
                        	if int(userin) in options:
                        		inputOK = True
                if inputOK == False:
                        print("Please enter a number between 1 and 9 corresponding to a free spot.")
                        userin = raw_input("")


        mainBoard.move(int(userin))

def algorithmMove():

	Possible = Tree*1 - 10**10
	Possible[:,2] -= (mainBoard.History-10**10)
	Possible[:,2] = Possible[:,2][Possible[:,2]>0]
	print(len(Possible[:,2]<(10**(10-mainBoard.NoTurn))))
	print(len(Possible[:,2]))
	Possible[:,2] = Possible[:,2][Possible[:,2]<(10**(10-mainBoard.NoTurn))]
	
	desirable = Possible[:,1][Possible[:,1] == 3]
	
	choice = desirable[random.randint(0,len(desirable))][2]
	
	mainBoard.move(mainBoard.digit(choice,(8-mainBoard.NoTurn)))



print("Lets play a gameof TicTacToe.")
print(" x starts and you should insert a number between 0 and 9 \n corresponding to the field you want to play.")



while mainBoard.finished != True:

	mainBoard.displayState()
	usermove()
	mainBoard.displayState()
	algorithmMove()

print(mainBoard.symbol(mainBoard.Winner)+" has won the Game.")
