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

def merge_decimal(list):
	x = 0
	for i in range(len(list)):
		x += list[i]*(10**i)

	return x

def botmove():

	options = np.sort(mainBoard.options())
	upper = merge_decimal(options)+mainBoard.History
	lower = merge_decimal(np.flip(options,0))+mainBoard.History

	uppermask = Tree[:,2]<upper
	lowermask = Tree[:,2]>lower

	completemask = np.logical_and(uppermask,lowermask)

	Possible = Tree[completemask]
	Wins = Possible[Possible[:,1] == 3]

	if len(Wins) == 0:
		mainBoard.move(options[0])
		return 0

	m = mainBoard.digit(Wins[0][2],8-mainBoard.NoTurn)
	mainBoard.move(m)

print("Lets play a gameof TicTacToe.")
print(" x starts and you should insert a number between 0 and 9 \n corresponding to the field you want to play.")



while mainBoard.finished != True:

	mainBoard.displayState()

	if mainBoard.NoTurn%2 == 0:
		usermove()
	else:
		botmove()

mainBoard.displayState()
print(mainBoard.symbol(mainBoard.Winner)+" has won the Game.")
