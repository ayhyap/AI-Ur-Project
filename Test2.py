import Test as init
import random

init.screenSetup()

#initialize piece turtles
#boardState = [[7,7],[0,0],[0,0],[0,0],[0,0],0,0,0,0,0,0,0,0,[0,0],[0,0],[0,0]]    #0 is none, negative integers is black, positive integers is white
#             start   1     2     3     4*  1 2 3 4*5 6 7 8   1     2*   end      #for combined zones, [black, white]
#               [0]   1     2     3     4   5 6 7 8 9 101112  13   14    15

blackPieces = []
whitePieces = []

for i in range(7):
    init.setScore(init.blackStartCount,i+1)
    blackPieces.append(init.BlackPiece())
    init.setScore(init.whiteStartCount,i+1)
    whitePieces.append(init.WhitePiece())

end = 0
turn = random.randrange(0,2,1)

#LET the furthest piece (not at end) be piece number 1.
#piece number 2 is the next one behind, and so on.
#pieces in start pile are arbitrarily ordered
def move(color, piece, moves):
    temp = getPiecePositions(color)
    offset = 0
    for i in range(0,7,1):
        if temp[i] != 15:
            break
        else:
            offset += 1
    if offset+piece-1 > 6:
        #invalid move
        return
    
    position = temp[offset + piece - 1]
    
    #position = getPiecePositions(color)[piece-1]
    if color == 0:
        #black
        if position > 4 and position < 13:
            blackPieces[init.boardState[position]*-1-1].moveForward(moves)
        elif position == 0:
            for i in range(0,7,1):
                if blackPieces[i].position == 0:
                    blackPieces[i].moveForward(moves)
        else:
            blackPieces[init.boardState[position][0]*-1-1].moveForward(moves)
    else:
        #white
        if position > 4 and position < 13:
            whitePieces[init.boardState[position]-1].moveForward(moves)
        else:
            whitePieces[init.boardState[position][1]-1].moveForward(moves)
    return

    
    if color == 0:
        #black
        for i in range(14,12,-1):
            if init.boardState[i][0] < 0:
                piece -= 1
            if piece == 0:
                blackPieces[init.boardState[i][0]*-1-1].moveForward(moves)
                return
        for i in range(12,4,-1):
            if init.boardState[i] < 0:
                piece-=1
            if piece == 0:
                blackPieces[init.boardState[i]*-1-1].moveForward(moves)
                return
        for i in range(4,0,-1):
            if init.boardState[i][0] < 0:
                piece -= 1
            if piece == 0:
                blackPieces[init.boardState[i][0]*-1-1].moveForward(moves)
                return
        if piece > init.boardState[0][0]:
            #invalid move!
            return
        else:
            #pick any one from start pile
            for i in range(0,7,1):
                if blackPieces[i].position == 0:
                    blackPieces[i].moveForward(moves)
                    return
    else:
        #white
        for i in range(14,12,-1):
            if init.boardState[i][1] > 0:
                piece -= 1
            if piece == 0:
                whitePieces[init.boardState[i][1]-1].moveForward(moves)
                return
        for i in range(12,4,-1):
            if init.boardState[i] > 0:
                piece-=1
            if piece == 0:
                whitePieces[init.boardState[i]-1].moveForward(moves)
                return
        for i in range(4,0,-1):
            if init.boardState[i][1] > 0:
                piece -= 1
            if piece == 0:
                whitePieces[init.boardState[i][1]-1].moveForward(moves)
                return
        if piece > init.boardState[0][1]:
            #invalid move!
            return
        else:
            #pick any one from start pile
            for i in range(0,7,1):
                if whitePieces[i].position == 0:
                    whitePieces[i].moveForward(moves)
                    return

#LET the furthest piece (not at end) be piece number 1.
#piece number 2 is the next one behind, and so on.
#pieces in start pile are arbitrarily ordered
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


#while end == 0:
    
    
print turn

if end == 1:
    print "WHITE WINS"
else:
    print "BLACK WINS"
#init.turtle.done()
