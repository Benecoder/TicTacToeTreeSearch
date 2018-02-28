# TicTacToeTreeSearch

TicTacToe2.py is a simple Generator that plays every possible game of TicTacToe and stores the result in a csv file.

<b>The Board (StateOfBoard class)</b>

The StateofBoard class handles the Gameplay, keeps track of whos's turn it is and stores the moves made. The Present State of the Board is stored in a nine digit string; each digit encoding one space on the board. In this encoding x is equivalent to 2, o is eqivalent to 3 and 1 is empty. x always starts the game. 



<b>(all optional) Arguments are</b>:

initState(Nine digit integer):  The State at wich the Board will be initialized to. Defaults to 111111111 ie. all empty.

NoTurn:   The Number of Turns that have already be performed. Should in the Fute be handled by the init function itself.

History:  The Order in wich the moves have been made. A list of integers where 0 encodes the top left spot and 8 encodes the bottom right one.



<b>Methods are:</b>

symbol: returns the x	~ 2,o	~ 3 and empty	~ 0 . encoding as a string.

digit: returns the nth digit of a decimal number.

displayState: Display the present state of the board.

check: Checks wether the game has finished.

move: makes the move on the xth field on the board. Who's turn it is is automaticcly alternated and check is beeing called on.

options: returns a list of empty fields.

<b>The Search Algorithm (recursive search):</b>
Given a root board, this function recursivly searches all possible outcomes and stores the instences of every possible game in BoardTree.
The list is ordered in the sense, that in the first move always the first opening has been taken and in the last element always the last element has been taken.


<b> SearchedTree.csv</b>

The CSV file that is return from running every possible combination of moves. Technicly only every second game of TicTacToe because you could always exchange the o's and the x's and get the same but opposite result. Every row encodes one game with first column being the Number of turns the second being the winner and the remaining Spots being the History of gameplay. Every Row is filled up with tens so as to not have a jagged List.

<b> TTTMCTS - TicTacToe monte Carlo Tree Search </b>

This file uses the TicTacToe class from TicTacToe2.py and the searched tree to classify the moves into moves that could lead to a win and moves that could not. It then takes the first available option. I.e. it's a really shitty bot.

