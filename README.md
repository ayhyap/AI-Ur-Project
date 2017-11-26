# AI-Ur-Project

COMP3211 Project

USES PYTHON 2.7.3

Run networkTraining_multiProcessing.py in cmd to train the networks using the genetic algorithm approach.

Be sure to turn off the game graphic when training otherwise the program will attempt to open 100 instances of the graphic.

After 100 generations the file will output the top 3 networks numbered 1 to 3 respectively. 

For convenience, the three networks we have previously trained are included.

Run playMain_Mix.py to play the game with either human, expectiMax, or neural network players.
=====

Change turtleMode to False in turtleUI_bool.py to disable graphics (for faster processing).

turleMode is set to True by default.

All graphics-unrelated functions should still work. Rely on print init.boardState and other functions to check status.

=====

Program will reach the game 'while loop', and prompt user to input a piece to move.

The integer to input is defined as the n-th furthest piece on the board of that colour, INCLUDING PIECES IN THE END PILE.

=====

If you keyboard interrupt (ctrl+c) you can manually type in function to control pieces.

Use board.move(color = 0 (black) or 1 (white), pieceNo = 1 to 7, moves = 0 to 4) to move pieces.

PieceNo of board.move() is defined as the n-th furthest piece on the board of that color, INCLUDING PIECES IN THE END PILE.

Use board.getPiecePositions(color = 0 (black) or 1 (white)) to get a sorted array of piece positions of that color (largest first).

Use init.resetBoard() to reset everything to the start state.

Enter turtle.done() to be able to close the graphics window properly.
