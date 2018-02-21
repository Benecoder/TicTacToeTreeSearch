#!/usr/bin/env python2

import numpy as np

"""
Encoding the state of the Board:

	Nine Digit integer Number with:

	x	~ 2
	empty 	~ 1
	o	~ 3

"""

class StateOfBoard():

	def __init__(self,initState = None,NoTurn = None,History = None):

		if initState == None:
			self.State = 111111111
		else:
			if initState > 10**9:
				print("Faulty inital State Encoding")
				print(initState)
				raise

			self.State = initState

		if NoTurn == None:
			self.NoTurn = 0
		else:
			self.NoTurn = NoTurn

		if History == None:
			self.History = 0
		else:
			self.History = History

		self.finished = False
		self.Winner = 1



	def symbol(self,a):
		if a == 2:
			return "x"
		elif a == 1:
			return " "
		elif a == 3:
			return "o"
		else:
			print("Faulty Board encoding detected")
			print("StateOfBoard.symbol() was asked to process: "+str(a))
			raise

	def digit(self,number, n):
	    return number // 10**n % 10

	def displayState(self):

		print("------")
		for i in range(3):
			dumpstr = ""
			for j in range(3):
				dumpstr += self.symbol(self.digit(self.State,i*3+j)) + "|"
			print(dumpstr)

		print("------")

	def check(self):

		Board = [self.digit(self.State,i) for i in range(9)]

		if self.NoTurn >= 9:
			self.finished = True
			self.Winner = 1
			return True

		for i in range(3):
			if Board[i*3] == Board[i*3+1] == Board[i*3+2] and Board[i*3] != 1:
				self.finished = True
				self.Winner = Board[i*3]
				return True
		for i in range(3):
			if Board[i] == Board[i+3] == Board[i+6] and Board[i] != 1:
				self.finished = True
				self.Winner = Board[i]
				return True

		if Board[0] == Board[4] == Board[8] and Board[0] != 1:
			self.finished = True
			self.Winner = Board[0]
			return True

		if Board[2] == Board[4] == Board[6] and Board[2] != 1:
			self.finished = True
			self.Winner = Board[2]
			return True

		return False

	def move(self,x):
		if self.digit(self.State,x) != 1:
			print("Trying to capture a captured spot. This incident will be reported.")
			print("Index: "+str(x))
			raise

		self.State += ((self.NoTurn%2)+1)*(10**x)

		self.History += x*(10**self.NoTurn)
		self.NoTurn +=1

		self.check()

	def options(self):

		State = [self.digit(self.State,i) for i in range(9)]
		State = np.array(State)
		return np.where(State == 1)[0]




root = StateOfBoard()
BoardTree = []

def recursiveSearch(Node):

	open = Node.options()
	for index in open[:-1]:
		BoardTree.append(StateOfBoard(initState = Node.State,
						NoTurn = Node.NoTurn,
						History = Node.History))
		BoardTree[-1].move(index)

		if BoardTree[-1].finished != True:
			recursiveSearch(BoardTree[-1])
#		else:
#			BoardTree[-1].displayState()

	if len(open>0):
		Node.move(open[-1])

		if Node.finished != True:
			recursiveSearch(Node)
#		else:
#			Node.displayState()



recursiveSearch(root)

Trees = [[a.NoTurn,a.Winner,a.History] for a in BoardTree]
Trees = np.array(Trees)
np.savetxt("SearchedTree.csv",Trees)
