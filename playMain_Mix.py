import game as board
import gameEngine as init
import random
import turtle
import ExpectiMax
import read as NN



def play(p1,p2):
    
    init.screenSetup()
    for i in range(7):
        init.setScore(init.blackStartCount,i+1)
        init.BlackPiece()
        #blackPieces.append(init.BlackPiece())
        init.setScore(init.whiteStartCount,i+1)
        init.WhitePiece()
        #whitePieces.append(init.WhitePiece())

    turn = random.randrange(0,2,1)

    NN.read('1')
    NN.read('2')

    turnCount = 0
    turnLimit = 2000
    #MAIN LOOP
    while board.checkWin() == 0:
        if (turnCount >= turnLimit):
            break
        #print init.boardState
        turnCount += 1
        print ("turn number: " + str(turnCount))
        moves = board.diceRoll()
        if turn == 0:
            #black turn
            print "BLACK TURN: " + str(moves)
            #print "Black rolls " + str(moves)
            if moves == 0:
                print "Unlucky! Black skips this turn."
                turn += 1
                turn %= 2
                continue
            if (p1 == 'e') :
                pieceToMove = ExpectiMax.moveByExpectimax(init.boardState,ExpectiMax.Color.BLACK,moves,1)
            if (p1 == 'nn') :
                pieceToMove = NN.networksBest[0].run(board.nnInputGen(moves))
            if (p1 == 'h') :
                pieceToMove = input("ENTER PIECE TO MOVE: ")
            extraTurn = board.move(0, pieceToMove, moves)
        else:
            #white turn
            print "WHITE TURN: "+ str(moves)
            #print "White rolls " + str(moves)
            if moves == 0:
                print "Unlucky! White skips this turn."
                turn += 1
                turn %= 2
                continue
            if (p1 == 'e') :
                pieceToMove = ExpectiMax.moveByExpectimax(init.boardState,ExpectiMax.Color.WHITE,moves,1)
            if (p1 == 'nn') :
                pieceToMove = NN.networksBest[1].run(board.nnInputGen(moves))
            if (p1 == 'h') :
                pieceToMove = input("ENTER PIECE TO MOVE: ")
            extraTurn = board.move(1, pieceToMove, moves)

        if extraTurn:
            print "Piece lands on a flowered tile, granting an EXTRA TURN!"
        else:
            turn += 1
            turn %= 2
    if (turnCount >= turnLimit):
        print("Tie")      

    if (board.checkWin() == -1) :
        print("Black Wins")
    else :
        print("White Wins")

playerTypes = ['e','h','nn']

p1 = ''
p2 = ''

while (p1 not in playerTypes or p2 not in playerTypes):
    print("The three player types are: (h)uman, (e)xpectiMax and (n)eural (n)etwork")
    p1 = raw_input("player 1 is: (h/e/nn)")
    p2 = raw_input("player 2 is: (h/e/nn)")
    if (p1 not in playerTypes or p2 not in playerTypes) :
        print("Your imputs are incorrect! Please try again!")
##(not p1 == "h" or not p1 == "e" or not p1 == "nn") and (not p2 == "h" or not p2 == "e" or not p2 == "nn")
play(p1,p2)
turtle.done()

