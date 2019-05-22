import numpy as np
from TicTacToe2 import StateOfBoard

Tree = np.genfromtxt("SearchedTree.csv")
mainBoard = StateOfBoard()

def usermove():

        userin = input("")
        inputOK = False
        options = mainBoard.options()

        while inputOK != True:
                if userin.isdigit():
                        if 1<=int(userin)<=9:
                        	if int(userin) in options+1:
                        		inputOK = True
                if inputOK == False:
                        print("Please enter a number between 1 and 9 corresponding to a free spot.")
                        userin = input("")


        mainBoard.move(int(userin)-1)

def merge_decimal(list):
	x = 0
	for i in range(len(list)):
		x += list[i]*(10**i)

	return x

def Probabilities(options,History,NoTurn,recursion = True):
    
    WinProbs = []
    
    for i in range(len(options)):
        remain_options = np.concatenate((options[:i],options[i+1:]))
        proposedHistory = History+options[i]*(10**(8-NoTurn))
    
        
        if proposedHistory in Tree[:,2]:
            Winner = Tree[Tree[:,2]==proposedHistory][0][1]
            if Winner == 3:
                WinProbs.append(1.0)
            else:
                WinProbs.append(0.0)
        else:


            upper = merge_decimal(np.concatenate((remain_options,[options[i]])))+History
            lower = merge_decimal(np.concatenate((np.flip(remain_options,0),[options[i]])))+History

            uppermask = Tree[:,2]<=upper
            lowermask = Tree[:,2]>=lower


            completemask = np.logical_and(uppermask,lowermask)


            Possible = Tree[completemask]
            Wins = Possible[Possible[:,1]==3]
            WinProb = float(len(Wins))/len(Possible)

            if recursion:
                DisasterPrevention = np.min(Probabilities(remain_options,proposedHistory,NoTurn+1,recursion = False))
                WinProb *= DisasterPrevention

            WinProbs.append(WinProb)

    WinProbs = np.array(WinProbs)
    return WinProbs

def botmove():
    options = np.sort(mainBoard.options())
    WP = Probabilities(options,mainBoard.History,mainBoard.NoTurn)
    for j in range(len(WP)):
        print(str(j)+': '+str(round(WP[j],5)))
    mainBoard.move(options[np.argmax(WP)])

print("Lets play a game of TicTacToe.")
print(" x starts and you should insert a number between 0 and 9 \n corresponding to the field you want to play.")



while mainBoard.finished != True:

    mainBoard.displayState()

    if mainBoard.NoTurn%2 == 0:
        usermove()
    else:
        botmove()

mainBoard.displayState()
print(mainBoard.symbol(mainBoard.Winner)+" has won the Game.")
