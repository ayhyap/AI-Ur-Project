import Test2 as board
import Test as init
import random
import turtle
import finalExpectimax as ExpectiMax
import MultiNNTrain as NN

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


##LOAD
NN.read("1")
NN.read("2")
NN.read("3")

nnWins = 0
for i in range(0,100,1):
    #print "ROUND " + str(i)
    #MAIN LOOP
    turnCount = 0
    init.resetBoard()
    while board.checkWin() == 0:
        #print init.boardState
        turnCount += 1
        #print turnCount
        moves = board.diceRoll()
        if turn == 0:
            #black turn
    ##        pieceToMove = process()
            print "BLACK TURN: " + str(turnCount)
            print "Black rolls " + str(moves)
            if moves == 0:
                print "Unlucky! Black skips this turn."
                turn += 1
                turn %= 2
                continue
            pieceToMove = input("ENTER PIECE TO MOVE: ")
            extraTurn = board.move(0, pieceToMove, moves)
            #extraTurn = board.move(0,ExpectiMax.moveByExpectimax(init.boardState,ExpectiMax.Color.BLACK,moves,1),moves)#expectimax implementation
            # extraTurn = board.move(0, NN.networksBest[1].run(board.nnInputGen(moves)), moves)
        else:
            #white turn
    ##        pieceToMove = process()
            print "WHITE TURN: " + str(turnCount)
            print "White rolls " + str(moves)
            if moves == 0:
                print "Unlucky! White skips this turn."
                turn += 1
                turn %= 2
                continue
            #pieceToMove = input("ENTER PIECE TO MOVE: ")
            #extraTurn = board.move(1, pieceToMove, moves)
            #extraTurn = board.move(1, NN.networksBest[1].run(board.nnInputGen(moves)), moves)
            extraTurn = board.move(1,ExpectiMax.moveByExpectimax(init.boardState,ExpectiMax.Color.WHITE,moves,1),moves)#expectimax implementation

        if extraTurn:
            print "Piece lands on a flowered tile, granting an EXTRA TURN!"
            pass
        else:
            turn += 1
            turn %= 2

        if turnCount == 200:
            break
            
    print init.boardState
    if (board.checkWin() == 1):
        print "WHITE WIN"
        #print "WHITE WIN (expectimax)"
    elif (board.checkWin() == -1):
        print "BLACK WIN"
        #print "BLACK WIN (neural network 1)"
        #nnWins += 1
    else:
        print "TIE"
    
#print "Expect " + str(100-str(nnWins)) + " : NN " + str(nnWins)
