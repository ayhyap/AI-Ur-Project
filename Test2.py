import Test as init
import random
import globalVars
import turtle

##init.screenSetup()

#initialize piece turtles
#boardState = [[7,7],[0,0],[0,0],[0,0],[0,0],0,0,0,0,0,0,0,0,[0,0],[0,0],[0,0]]    #0 is none, negative integers is black, positive integers is white
#             start   1     2     3     4*  1 2 3 4*5 6 7 8   1     2*   end      #for combined zones, [black, white]
#               [0]   1     2     3     4   5 6 7 8 9 101112  13   14    15

##blackPieces = []
##whitePieces = []

##for i in range(7):
##    init.setScore(init.blackStartCount,i+1)
##    blackPieces.append(init.BlackPiece())
##    init.setScore(init.whiteStartCount,i+1)
##    whitePieces.append(init.WhitePiece())

#LET the furthest piece (not at end) be piece number 1.
#piece number 2 is the next one behind, and so on.
#pieces in start pile are arbitrarily ordered
#print init.boardState
def move(color, piece, moves):
    temp = getPiecePositions(color)
    offset = 0
##    for i in range(0,7,1):
##        if temp[i] != 15:
##            break
##        else:
##            offset += 1
##    if offset+piece-1 > 6:
##        #invalid move
##        print "invalid move"
##        return False
    
    position = temp[offset + piece - 1]
    
    #position = getPiecePositions(color)[piece-1]
    if color == 0:
        #black
        if position > 4 and position < 13:
            return init.BlackPiece.pieces[init.boardState[position]*-1-1].moveForward(moves)
            #return blackPieces[init.boardState[position]*-1-1].moveForward(moves)
        elif position == 0:
            for i in range(0,7,1):
                if init.BlackPiece.pieces[i].position == 0:
                    return init.BlackPiece.pieces[i].moveForward(moves)
                    #return blackPieces[i].moveForward(moves)
        else:
            return init.BlackPiece.pieces[init.boardState[position][0]*-1-1].moveForward(moves)
            #return blackPieces[init.boardState[position][0]*-1-1].moveForward(moves)
    else:
        #white
        if position > 4 and position < 13:
            return init.WhitePiece.pieces[init.boardState[position]-1].moveForward(moves)
            #return whitePieces[init.boardState[position]-1].moveForward(moves)
        elif position == 0:
            for i in range(0,7,1):
                if init.WhitePiece.pieces[i].position == 0:
                    return init.WhitePiece.pieces[i].moveForward(moves)
                    #return whitePieces[i].moveForward(moves)
        else:
            return init.WhitePiece.pieces[init.boardState[position][1]-1].moveForward(moves)
            #return whitePieces[init.boardState[position][1]-1].moveForward(moves)
    return

#LET the furthest piece be piece number 1.
#piece number 2 is the next one behind, and so on.
#pieces in start pile and end pile are arbitrarily ordered
#0 is black, 1 is white
def getPiecePositions(color):
    positions = []
    multiplier = 1
    if color == 0:
        multiplier= -1

    #end pile
    if init.boardState[15][color] > 0:
        for i in range(0, init.boardState[15][color], 1):
            positions.append(15)
    #after warzone
    for i in range(14,12,-1):
        if abs(init.boardState[i][color]) > 0:
            positions.append(i)
    #during warzone
    for i in range(12,4,-1):
        if init.boardState[i]*multiplier > 0:
            positions.append(i)
    #before warzone
    for i in range(4,0,-1):
        if abs(init.boardState[i][color]) > 0:
            positions.append(i)
    #start pile
    if init.boardState[0][color] > 0:
        for i in range(0, init.boardState[0][color], 1):
            positions.append(0)

    return positions


def checkWin():
    if init.boardState[15][0] == 7:
        return -1
    elif init.boardState[15][1] == 7:
        return 1
    else:
        return 0


def diceRoll():
    return random.randrange(0,2,1) + random.randrange(0,2,1) + random.randrange(0,2,1) + random.randrange(0,2,1)

def nnInputGen(moves):
    temp = []
    temp.append(moves)  #[0]: moves
    temp.append(11)      #[1]: distance from flower tile 1 to end
    temp.append(7)      #[2]: distance from flower tile 2 to end
    temp.append(1)     #[3]: distance from flower tile 3 to end
    positions = getPiecePositions(0)
    for i in range(0,7,1):
        positions[i] = 15 - positions[i]
    temp += positions

    positions = getPiecePositions(1)
    for i in range(0,7,1):
        positions[i] = 15 - positions[i]
    temp += positions
    return temp
    

##turn = random.randrange(0,2,1)

###MAIN LOOP
##while checkWin() == 0:
##    moves = diceRoll()
##    if turn == 0:
##        #black turn
####        pieceToMove = process()
####        print "BLACK TURN"
####        print "Black rolls " + str(moves)
####        pieceToMove = input("ENTER PIECE TO MOVE: ")
##        extraTurn = move(0,pieceToMove,moves)
##    else:
##        #white turn
####        pieceToMove = process()
####        print "WHITE TURN"
####        print "White rolls " + str(moves)
####        pieceToMove = input("ENTER PIECE TO MOVE: ")
##        extraTurn = move(1,pieceToMove,moves)
##
##    if not extraTurn:
##        turn += 1
##        turn %= 2
#init.turtle.done()
