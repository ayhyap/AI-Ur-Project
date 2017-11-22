import Test2 as board
import Test as init
import random
import turtle
import finalExpectimax as ExpectiMax
import mainBoard as NN

init.screenSetup()
for i in range(7):
    init.setScore(init.blackStartCount,i+1)
    init.BlackPiece()
    #blackPieces.append(init.BlackPiece())
    init.setScore(init.whiteStartCount,i+1)
    init.WhitePiece()
    #whitePieces.append(init.WhitePiece())

turn = random.randrange(0,2,1)

turnCount = 0
#MAIN LOOP
while board.checkWin() == 0:
    #print init.boardState
    turnCount += 1
    print turnCount
    moves = board.diceRoll()
    if turn == 0:
        #black turn
##        pieceToMove = process()
        print "BLACK TURN: " + str(moves)
        #print "Black rolls " + str(moves)
        if moves == 0:
            print "Unlucky! Black skips this turn."
            turn += 1
            turn %= 2
            continue
        # pieceToMove = input("ENTER PIECE TO MOVE: ")
        extraTurn = board.move(0,ExpectiMax.moveByExpectimax(init.boardState,ExpectiMax.Color.BLACK,moves,1),moves)#expectimax implementation
    else:
        #white turn
##        pieceToMove = process()
        print "WHITE TURN: "+ str(moves)
        #print "White rolls " + str(moves)
        if moves == 0:
            print "Unlucky! White skips this turn."
            turn += 1
            turn %= 2
            continue
        pieceToMove = input("ENTER PIECE TO MOVE: ")
        extraTurn = board.move(1, pieceToMove, moves)
        #extraTurn = board.move(1, NN.networks[1].run(board.nnInputGen(moves)), moves)

    if extraTurn:
        print "Piece lands on a flowered tile, granting an EXTRA TURN!"
    else:
        turn += 1
        turn %= 2
        

print board.checkWin()
