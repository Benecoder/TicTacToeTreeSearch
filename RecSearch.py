from TicTacToe2 import *


root = StateOfBoard()
BoardTree = [root]

def recursiveSearch(Node):

	open = Node.options()

	for index in open[1:]:
		BoardTree.append(StateOfBoard(initState = Node.State,
						NoTurn = Node.NoTurn,
						History = Node.History))
		BoardTree[-1].move(index)

		if BoardTree[-1].finished != True:
			recursiveSearch(BoardTree[-1])
#		else:
#			BoardTree[-1].displayState()

	if len(open) > 0:
		Node.move(open[0])

		if Node.finished != True:
			recursiveSearch(Node)

recursiveSearch(root)

print("Finished recursive Search")

Tree = [[a.NoTurn,a.Winner,a.History] for a in BoardTree]

Tree = np.array(Tree)
np.savetxt("SearchedTree.csv",Tree)

