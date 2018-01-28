import interface
import gameEngine
import math
import copy
import random

def run(boardState, moves, color, depth):
    #print("=================================================================")
    #print("=================================================================")
    #print("EXPECTIMAX")
    #print(color, "MOVE",moves)
    newBoard = simplifyBoard(boardState)
    #print(newBoard)
    piece, score = playNode(newBoard, color, moves, copy.copy(depth))
    return piece

#white wants to maximize score, black wants to minimize
def playNode(boardState, color, moves, depth):
    #print("DEPTH ", depth,"PLAYNODE")
    #extraTurn, validMove, newBoard moveSimulator(boardState, color, piece, moves)

    bestMove = 0
    
    if color == 0:
        bestScore = math.inf
    else:
        bestScore = -math.inf

    upper = 6
    lower = -1
    if boardState[0][color] > 1:
        upper = upper - boardState[0][color] + 1
    lower += boardState[15][color]
    
    for i in range(upper, lower, -1):
        #try moving piece
        extraTurn, validMove, tempBoard = moveSimulator(boardState, color, i+1, moves)
        if validMove:
            if extraTurn:
                nextColor = color
            else:
                nextColor = (color+1)%2
            tempScore = diceNode(tempBoard, nextColor, (depth-1))
        else:
            continue
        if color == 0:
            #black, minimize score
            if tempScore < bestScore:
                bestMove = i
                bestScore = tempScore
        else:
            #white, maximize score
            if tempScore > bestScore:
                bestMove = i
                bestScore = tempScore

    return bestMove + 1, bestScore

    

def diceNode(boardState, color, depth):
    #print("DEPTH ", depth, "DICENODE")
    if depth == 0:
        #print("Cutoff, getScore()")
        return getScore(boardState)

    score = 0

    tempMove, tempScore = playNode(copy.deepcopy(boardState), color, 0, (depth))
    score += tempScore * 0.0625

    tempMove, tempScore = playNode(copy.deepcopy(boardState), color, 1, (depth))
    score += tempScore * 0.25

    tempMove, tempScore = playNode(copy.deepcopy(boardState), color, 2, (depth))
    score += tempScore * 0.375

    tempMove, tempScore = playNode(copy.deepcopy(boardState), color, 3, (depth))
    score += tempScore * 0.25

    tempMove, tempScore = playNode(copy.deepcopy(boardState), color, 4, (depth))
    score += tempScore * 0.0625
    return score



#negative score: black in lead
#positive score: white in lead
def getScore(boardState):
    white, black = getProgress(boardState)
    return white - black


def getProgress(boardState):
    blackArr = getPiecePositions(boardState,0)
    whiteArr = getPiecePositions(boardState,1)
    black = 0
    white = 0
    for i in blackArr:
        black += i
    for i in whiteArr:
        white += i
    return white, black

#returns positions of 7 pieces of that color, sorted from furthest travelled to closest (to start)
#0 is black, 1 is white
def getPiecePositions(boardState, color):
    ##print("=================================================================")
    ##print("GETPOSITIONS: ", color)
    ##print(boardState)
    positions = []
    multiplier = 1
    if color == 0:
        multiplier= -1

    #end pile
    if boardState[15][color] > 0:
        for i in range(boardState[15][color]):
            positions.append(15)
    ##print(positions)
    #after warzone
    for i in range(14,12,-1):
        if abs(boardState[i][color]) > 0:
            positions.append(i)
    ##print(positions)
    #during warzone
    for i in range(12,4,-1):
        if boardState[i]*multiplier > 0:
            positions.append(i)
    ##print(positions)
    #before warzone
    for i in range(4,0,-1):
        if abs(boardState[i][color]) > 0:
            positions.append(i)
    ##print(positions)
    #start pile
    if boardState[0][color] > 0:
        for i in range(0, boardState[0][color], 1):
            positions.append(0)
    ##print(positions)
    
    #if (len(positions)) != 7:
    #    raise Exception("PANIC: pos array only has ", len(positions), " items")
    ##print("=================================================================")
    return copy.deepcopy(positions)


#color: 0 is black, 1 is white
#1 is most progress NOT AT END PILE, 7 is least progress
#returns EXTRATURN (bool), VALIDMOVE (bool), boardState
def moveSimulator(boardState, color, piece, moves):
    #print("=================================================================")
    #print("MOVESIMULATOR")
    newBoard = copy.deepcopy(boardState)
    
    if moves < 0 or moves > 4:
        #always invalid
        #print("--INVALID: moves out of bounds")
        return False, False, newBoard
    if moves == 0:
        #always valid
        #print("++++VALID: no move")
        return False, True, newBoard
    
    if color == 0:
        #black
        posArray = getPiecePositions(boardState, 0)
        position = posArray[piece - 1]
    else:
        #white
        posArray = getPiecePositions(boardState, 1)
        position = posArray[piece - 1]
    
    for i in range(7):
        if i == 6 or piece + i > 6:
            position = posArray[6]
            break
        if position == 15:
            position = posArray[piece + i]
        else:
            break

    #check if player has already won
    if position == 15:
        #always invalid
        #print("--INVALID: player has won already")
        return False, False, newBoard
    
    target = position + moves
    if target > 15:
        target = 15
    
    
    #check target tile
    if target > 4 and target < 13:
        #warzone
        if newBoard[target] == 0:     #empty tile
            newBoard = removeFromIndex(newBoard, position, color)
            newBoard = addToIndex(newBoard, target, color)
            if target == 8:
                #extra turn
                #print("++++VALID: warzone empty flower")
                return True, True, newBoard
            else:
                #print("++++VALID: warzone empty")
                return False, True, newBoard
        else: #occupied tile
            #boardState: -1 is black, 1 is white
            #color: 0 is black, 1 is white
            #BS[] + color
            #BB = -1    BW = 0      WB = 1      WW = 2
            state = newBoard[target] + color
            if state == -1 or state == 2:
                #move same color: invalid
                #print("--INVALID: warzone friendly occupied")
                return False, False, newBoard
            else:
                #move different color
                if target == 8:
                    #move to safe spot: invalid
                    #print("--INVALID: warzone flower occupied")
                    return False, False, newBoard
                else:
                    newBoard = removeFromIndex(newBoard, target, (color+1)%2)
                    newBoard = addToIndex(newBoard, 0, (color+1)%2)
                    newBoard = removeFromIndex(newBoard, position, color)
                    newBoard = addToIndex(newBoard, target, color)
                    #print("++++VALID: warzone displace")
                    return False, True, newBoard
    elif target == 15:
        newBoard = removeFromIndex(newBoard, position, color)
        newBoard = addToIndex(newBoard, target, color)
        #print("++++VALID: end")
        return False, True, newBoard
    else: 
        #safezone
        if color == 0:
            index = -1
        else:
            index = 1
        if newBoard[target][color] != 0:
            #occupied: invalid
            #print("--INVALID: safezone occupied")
            return False, False, newBoard
        else:
            #empty: valid
            newBoard = removeFromIndex(newBoard, position, color)
            newBoard = addToIndex(newBoard, target, color)
            if target == 8:
                #print("++++VALID: safezone empty flower")
                return True, True, newBoard
            else:
                #print("++++VALID: safezone empty")
                return False, True, newBoard

def simplifyBoard(boardState):
    newBoard = boardState
    for i in range(16):
        if i > 4 and i < 13:
            #warzone
            if newBoard[i] > 0:
                newBoard[i] = 1
            elif newBoard[i] < 0:
                newBoard[i] = -1
        elif i == 0 or i == 15:
            #pile
            pass
        else:
            #safe zone
            if newBoard[i][0] != 0:
                newBoard[i][0] = -1
            
            if newBoard[i][1] != 0:
                newBoard[i][1] = 1
    return newBoard


def removeFromIndex(boardState, index, color):
    #print("=================================================================")
    #print("Remove ", color, " from ", index)
    #print("BEFORE:",boardState)
    
    newBoard = copy.deepcopy(boardState)
    if index > 4 and index < 13:
        #warzone
        newBoard[index] = 0
    elif index == 0 or index == 15:
        #start or end pile
        newBoard[index][color] -= 1
    else:
        #safe zone
        newBoard[index][color] = 0

    #print("AFTER:",newBoard)
    return newBoard


def addToIndex(boardState, index, color):
    #print("=================================================================")
    #print("Add ", color, " to ", index)
    #print("BEFORE:", boardState)
    mult = 1
    if color == 0:
        mult = -1
    
    newBoard = copy.deepcopy(boardState)
    if index > 4 and index < 13:
        #warzone
        newBoard[index] = mult
    elif index == 0 or index == 15:
        #start or end pile
        newBoard[index][color] += 1
    else:
        #safe zone
        newBoard[index][color] = mult
    #print("AFTER:",newBoard)
    return newBoard

###random board gen
##def gen():
##    black = random.sample(range(16), 7)
##    white = [0,1,2,3,4,13,14]
##    bs = [[0,0],[0,0],[0,0],[0,0],[0,0],0,0,0,0,0,0,0,0,[0,0],[0,0],[0,0]]
##    for x in black:
##        bs = addToIndex(bs, x, 0)
##    for x in white:
##        bs = addToIndex(bs, x, 1)
##    return bs        
##
###testing
##for m in range(1,5):
##    bs = gen()
##    p = run(bs, m, 0)
##    print(p)
