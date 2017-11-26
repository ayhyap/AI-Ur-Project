import gameEngine as init
import random
import turtleUI_bool as globalVars
import turtle

#LET the furthest piece be piece number 1.
#piece number 2 is the next one behind, and so on.
#pieces in start pile are arbitrarily ordered
#0 is black, 1 is white
def move(color, piece, moves):
    temp = getPiecePositions(color)
    position = temp[piece - 1]
    if color == 0:
        #black
        if position > 4 and position < 13:
            return init.BlackPiece.pieces[init.boardState[position]*-1-1].moveForward(moves)
        elif position == 0:
            for i in range(0,7,1):
                if init.BlackPiece.pieces[i].position == 0:
                    return init.BlackPiece.pieces[i].moveForward(moves)
        elif position == 15:
            return False
        else:
            return init.BlackPiece.pieces[init.boardState[position][0]*-1-1].moveForward(moves)
    else:
        #white
        if position > 4 and position < 13:
            return init.WhitePiece.pieces[init.boardState[position]-1].moveForward(moves)
        elif position == 0:
            for i in range(0,7,1):
                if init.WhitePiece.pieces[i].position == 0:
                    return init.WhitePiece.pieces[i].moveForward(moves)
        elif position == 15:
            return False
        else:
            return init.WhitePiece.pieces[init.boardState[position][1]-1].moveForward(moves)
    return

#returns positions of 7 pieces of that colour, sorted from furthest travelled to closest (to start)
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

#checks if someone has won
#returns 0 if no winner
#returns 1 if white win, -1 if black win
def checkWin():
    if init.boardState[15][0] == 7:
        return -1
    elif init.boardState[15][1] == 7:
        return 1
    else:
        return 0

def breakTie():
    if init.boardState[15][0] < init.boardState[15][1]:
        return -1
    if init.boardState[15][0] > init.boardState[15][1]:
        return 1
    if init.boardState[0][0] > init.boardState[0][1]:
        return -1
    if init.boardState[0][0] < init.boardState[0][1]:
        return 1
    return 0

def checkCompetence(color):
    return init.boardState[15][color] > 0

#Binom(4,0.5), 4 coin tosses
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
