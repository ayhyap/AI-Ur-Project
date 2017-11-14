import Test2 as board
import Test as init
import random
import turtle


init.screenSetup()
for i in range(7):
    init.setScore(init.blackStartCount,i+1)
    init.BlackPiece()
    #blackPieces.append(init.BlackPiece())
    init.setScore(init.whiteStartCount,i+1)
    init.WhitePiece()
    #whitePieces.append(init.WhitePiece())

turn = random.randrange(0,2,1)

#MAIN LOOP
while board.checkWin() == 0:
    print init.boardState
    moves = board.diceRoll()
    if turn == 0:
        #black turn
##        pieceToMove = process()
        print "BLACK TURN"
        print "Black rolls " + str(moves)
        if moves == 0:
            print "Unlucky! Black skips this turn."
            turn += 1
            turn %= 2
            continue
        pieceToMove = input("ENTER PIECE TO MOVE: ")
        extraTurn = board.move(0,pieceToMove,moves)
    else:
        #white turn
##        pieceToMove = process()
        print "WHITE TURN"
        print "White rolls " + str(moves)
        if moves == 0:
            print "Unlucky! White skips this turn."
            turn += 1
            turn %= 2
            continue
        pieceToMove = input("ENTER PIECE TO MOVE: ")
        extraTurn = board.move(1,pieceToMove,moves)

    if not extraTurn:
        turn += 1
        turn %= 2

print board.checkWin()
