# AI-Ur-Project

COMP3211 Project

USES PYTHON 2.7.3

Run playMain.py from python shell

BUG: Attempting to move a black piece in the end pile will move another piece not in the end pile.

=====

Change turtleMode to False in globalVars.py to disable graphics (for faster processing).

All graphics-unrelated functions should still work. Rely on print init.boardState and other functions to check status.

=====

Program will reach the game 'while loop', and prompt user to input a piece to move.

The integer to input is defined as the n-th furthest piece on the board of that colour, INCLUDING PIECES IN THE END PILE.

=====

If you keyboard interrupt (ctrl+c) you can manually type in function to control pieces.

Use move(color = 0 (black) or 1 (white), pieceNo = 1 to 7, moves = 0 to 4) to move pieces.

PieceNo of move() is defined as the n-th furthest piece on the board of that color, INCLUDING PIECES IN THE END PILE.

Use getPiecePositions(color = 0 (black) or 1 (white)) to get a sorted array of piece positions of that color (largest first).

Use init.resetBoard() to reset everything to the start state.

Enter turtle.done() to be able to close the graphics window properly.