import gameEngine
import random

#LET the furthest piece NOT AT THE END PILE be piece number 1.
#piece number 2 is the next one behind, and so on.
#pieces in start pile are arbitrarily ordered
#0 is black, 1 is white
#returns true if extra move, false otherwise
def move(color, piece, moves):
    temp = getPiecePositions(color)
    position = temp[piece - 1]
    for i in range(7):
        if i == 6 or piece + i > 6:
            position = temp[6]
            break
        if position == 15:
            position = temp[piece + i]
        else:
            break
        
    if color == 0:
        #black
        if position > 4 and position < 13:
            return gameEngine.BlackPiece.pieces[gameEngine.boardState[position]*-1-1].moveForward(moves)
        elif position == 0:
            for i in range(0,7,1):
                if gameEngine.BlackPiece.pieces[i].position == 0:
                    return gameEngine.BlackPiece.pieces[i].moveForward(moves)
        elif position == 15:
            return False
        else:
            return gameEngine.BlackPiece.pieces[gameEngine.boardState[position][0]*-1-1].moveForward(moves)
    else:
        #white
        if position > 4 and position < 13:
            return gameEngine.WhitePiece.pieces[gameEngine.boardState[position]-1].moveForward(moves)
        elif position == 0:
            for i in range(0,7,1):
                if gameEngine.WhitePiece.pieces[i].position == 0:
                    return gameEngine.WhitePiece.pieces[i].moveForward(moves)
        elif position == 15:
            return False
        else:
            return gameEngine.WhitePiece.pieces[gameEngine.boardState[position][1]-1].moveForward(moves)
    return

#returns positions of 7 pieces of that colour, sorted from furthest travelled to closest (to start)
#0 is black, 1 is white
def getPiecePositions(color):
    positions = []
    multiplier = 1
    if color == 0:
        multiplier= -1

    #end pile
    if gameEngine.boardState[15][color] > 0:
        for i in range(0, gameEngine.boardState[15][color], 1):
            positions.append(15)
    #after warzone
    for i in range(14,12,-1):
        if abs(gameEngine.boardState[i][color]) > 0:
            positions.append(i)
    #during warzone
    for i in range(12,4,-1):
        if gameEngine.boardState[i]*multiplier > 0:
            positions.append(i)
    #before warzone
    for i in range(4,0,-1):
        if abs(gameEngine.boardState[i][color]) > 0:
            positions.append(i)
    #start pile
    if gameEngine.boardState[0][color] > 0:
        for i in range(0, gameEngine.boardState[0][color], 1):
            positions.append(0)

    if len(positions) != 7:
        print(positions)
        raise Exception("position array has only indices:", len(positions))
    return positions

#checks if someone has won
#returns 0 if no winner
#returns 1 if white win, -1 if black win
def checkWin():
    if gameEngine.boardState[15][0] == 7:
        return -1
    elif gameEngine.boardState[15][1] == 7:
        return 1
    else:
        return 0

def reset():
    gameEngine.resetBoard()

def diceRoll():
    return random.randrange(0,2,1) + random.randrange(0,2,1) + random.randrange(0,2,1) + random.randrange(0,2,1)
