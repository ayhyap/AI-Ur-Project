# AI-Ur-Project

COMP3211 Project

Run test2.py in python shell, test1.py does nothing on its own.

Use move(color = 0 (black) or 1 (white), pieceNo = 1 to 7, moves = 0 to 4) to move pieces.
PieceNo of move() is defined as the n-th furthest piece on the board of that color which is not at the end.

Use getPiecePositions(color = 0 (black) or 1 (white)) to get a sorted array of piece positions of that color (largest first).

Enter turtle.done() to be able to close the graphics window properly.

==

Change turtleMode to False in globalVars.py to disable graphics (for faster processing).
All graphics-unrelated functions should still work. Rely on print init.boardState and other functions to check status.