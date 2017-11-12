import turtle
import board
import globalVars

#global score turtles, because i'm lazy
whiteStartCount = 0
blackStartCount = 0
whiteEndCount = 0
blackEndCount = 0


#initialize piece turtles
boardState = [[7,7],[0,0],[0,0],[0,0],[0,0],0,0,0,0,0,0,0,0,[0,0],[0,0],[0,0]]    #0 is none, negative integers is black, positive integers is white
#             start   1     2     3     4*  1 2 3 4*5 6 7 8   1     2*   end      #for combined zones, [black, white]
#               [0]   1     2     3     4   5 6 7 8 9 101112  13   14    15


    
def screenSetup():
    if globalVars.turtleMode: 
        global whiteStartCount
        global blackStartCount
        global whiteEndCount
        global blackEndCount
        
        whiteStartCount = turtle.Turtle()
        blackStartCount = turtle.Turtle()
        whiteEndCount = turtle.Turtle()
        blackEndCount = turtle.Turtle()
        board.draw()
    
        #score turtles
        whiteStartCount.hideturtle()
        whiteStartCount.up()
        whiteStartCount.goto(0,250)
        whiteStartCount.write("0",False,"center",("Arial", 20, "normal"))
    
        blackStartCount.hideturtle()
        blackStartCount.up()
        blackStartCount.goto(0,-280)
        blackStartCount.write("0",False,"center",("Arial", 20, "normal"))
    
        whiteEndCount.hideturtle()
        whiteEndCount.up()
        whiteEndCount.goto(200,250)
        whiteEndCount.write("0",False,"center",("Arial", 20, "normal"))
    
        blackEndCount.hideturtle()
        blackEndCount.up()
        blackEndCount.goto(200,-280)
        blackEndCount.write("0",False,"center",("Arial", 20, "normal"))

#helper functions:

#sets score turtle
def setScore(inTurtle,value):
    
    if globalVars.turtleMode:
        inTurtle.clear()
        inTurtle.write(value,False,"center",("Arial", 20, "normal"))

def updateScore():
    
    if globalVars.turtleMode: 
        setScore(whiteEndCount,boardState[15][1])
        setScore(whiteStartCount,boardState[0][1])
        setScore(blackEndCount,boardState[15][0])
        setScore(blackStartCount,boardState[0][0])

#sets boardstate index to 0
#index is 0 to 15
#color: 0 for black, 1 for white
def removeFromIndex(index,color):
    if index > 4 and index < 13:
        #warzone
        boardState[index] = 0
    elif index == 0 or index == 15:
        #start or end pile
        boardState[index][color] -= 1
        updateScore()
    else:
        boardState[index][color] = 0


def resetBoard():
    
    global boardState
    boardState = [[7,7],[0,0],[0,0],[0,0],[0,0],0,0,0,0,0,0,0,0,[0,0],[0,0],[0,0]]
    for piece in BlackPiece.pieces:
        piece.position = 0
        if globalVars.turtleMode:
            piece.piece.goto(BlackPiece.path[0][0],BlackPiece.path[0][1])

    for piece in WhitePiece.pieces:
        piece.position = 0
        if globalVars.turtleMode:
            piece.piece.goto(WhitePiece.path[0][0],WhitePiece.path[0][1])
    updateScore()


class BlackPiece:
    #static variable
    pieces = []
    path = [ [0,-200], [-50,-100], [-150,-100], [-250,-100], [-350,-100], [-350,0], [-250,0], [-150,0], [-50,0], [50,0], [150,0], [250,0], [350,0], [350,-100], [250,-100], [200,-200] ]
    pieceCount = 0

    #constructor
    def __init__(self):
        
        if globalVars.turtleMode:
            #turtle stuff
            self.piece = turtle.Turtle()
            self.piece.resizemode("user")
            self.piece.turtlesize(3,3,1)
            self.piece.up()
            self.piece.shape("circle")
            self.piece.fillcolor("black")
            self.piece.goto(BlackPiece.path[0][0],BlackPiece.path[0][1])

        #housekeeping
        BlackPiece.pieceCount+=1
        BlackPiece.pieces.append(self)

        #identity
        self.position = 0
        self.id = BlackPiece.pieceCount
        
    #move 'self' piece 'steps' steps forward
    #returns true if extra turn (land on flowered tile)
    #returns false otherwise
    def moveForward(self, steps):
        
        #check if invalid steps (or 0 steps): do nothing you filthy cheater
        if steps < 1 or steps > 4:
            return False

        #calculate target position
        temp = self.position + steps

        #check target tile
        if temp > 4 and temp < 13:                 #warzone
            if boardState[temp] == 0:       #empty tile
                removeFromIndex(self.position,0)    #remove from original spot
                
                boardState[temp] = self.id * -1     #add to new spot
                self.position = temp                #update self position
                if globalVars.turtleMode:
                    self.piece.goto(BlackPiece.path[temp][0],BlackPiece.path[temp][1])  #move turtle
                if temp == 8:
                    #flower tile
                    return True
                else:
                    return False
            elif boardState[temp] > 0:      #occupied by WHITE piece (enemy)
                if temp == 8:   #flower tile, enemy piece is safe
                    return False
                else:           #normal tile, kick off
                    WhitePiece.pieces[boardState[temp]-1].reset()
                    removeFromIndex(self.position,0)    #remove from original spot
                    boardState[temp] = self.id * -1     #add to new spot
                    updateScore()
                    self.position = temp                #update self position
                    if globalVars.turtleMode:
                        self.piece.goto(BlackPiece.path[temp][0],BlackPiece.path[temp][1])  #move turtle
                    return True
            else:   #occupied by BLACK piece (friendly)
                #do nothing
                return False;
        else:                    #safe zone
            #check if end
            if temp > 14:
                #endzone
                boardState[15][0] += 1
                removeFromIndex(self.position,0)    #remove from original spot
                updateScore()
                self.position = 15
                if globalVars.turtleMode:
                    self.piece.goto(BlackPiece.path[15][0],BlackPiece.path[15][1])
                return False
            elif boardState[temp][0] == 0:    #empty tile
                removeFromIndex(self.position,0)    #remove from original spot
                    
                boardState[temp][0] = self.id * -1  #add to new spot
                self.position = temp                #update self position
                if globalVars.turtleMode:
                    self.piece.goto(BlackPiece.path[temp][0],BlackPiece.path[temp][1])  #move turtle
                if temp == 4 or temp == 14:
                    #flower tile
                    return True
                else:
                    return False
            else:   #tile occupied by friendly piece, do nothing
                return False

    #send a piece back to start and update boardState        
    def reset(self):
        
        boardState[0][0] += 1
        removeFromIndex(self.position, 0)
        if globalVars.turtleMode:
            self.piece.goto(BlackPiece.path[0][0],BlackPiece.path[0][1])
        self.position = 0
        

class WhitePiece:
    #static variable
    pieces = []
    path = [ [0,200], [-50,100], [-150,100], [-250,100], [-350,100], [-350,0], [-250,0], [-150,0], [-50,0], [50,0], [150,0], [250,0], [350,0], [350,100], [250,100], [200,200] ]
    pieceCount = 0

    #constructor
    def __init__(self):
        
        if globalVars.turtleMode:
            #turtle stuff
            self.piece = turtle.Turtle()
            self.piece.resizemode("user")
            self.piece.turtlesize(3,3,1)
            self.piece.up()
            self.piece.shape("circle")
            self.piece.fillcolor("white")
            self.piece.goto(WhitePiece.path[0][0],WhitePiece.path[0][1])
        
        #housekeeping
        WhitePiece.pieceCount+=1
        WhitePiece.pieces.append(self)

        #identity
        self.position = 0
        self.id = WhitePiece.pieceCount

    #move 'self' piece 'steps' steps forward
    #returns true if extra turn (land on flowered tile)
    #returns false otherwise
    def moveForward(self, steps):
        
        #check if invalid steps (or 0 steps): do nothing you filthy cheater
        if steps < 1 or steps > 4:
            return False

        #calculate target position
        temp = self.position + steps

        #check target tile
        if temp > 4 and temp < 13:                 #warzone
            if boardState[temp] == 0:       #empty tile
                removeFromIndex(self.position,1)    #remove from original spot
                
                boardState[temp] = self.id          #add to new spot
                self.position = temp                #update self position
                if globalVars.turtleMode:
                    self.piece.goto(WhitePiece.path[temp][0],WhitePiece.path[temp][1])  #move turtle
                if temp == 8:
                    #flower tile
                    return True
                else:
                    return False
            elif boardState[temp] < 0:      #occupied by BLACK piece (enemy)
                if temp == 8:   #flower tile, enemy piece is safe
                    return False
                else:           #normal tile, kick off
                    BlackPiece.pieces[boardState[temp]*-1-1].reset()
                    removeFromIndex(self.position,1)    #remove from original spot
                    updateScore()
                    boardState[temp] = self.id          #add to new spot
                    self.position = temp                #update self position
                    if globalVars.turtleMode:
                        self.piece.goto(WhitePiece.path[temp][0],WhitePiece.path[temp][1])  #move turtle
                    return True
            else:   #occupied by WHITE piece (friendly)
                #do nothing
                return False;
        else:                    #safe zone
            #check if end
            if temp > 14:
                #endzone
                boardState[15][1] += 1
                removeFromIndex(self.position,1)    #remove from original spot
                updateScore()
                self.position = 15
                if globalVars.turtleMode:
                    self.piece.goto(WhitePiece.path[15][0],WhitePiece.path[15][1])
                return False
            elif boardState[temp][1] == 0:    #empty tile
                removeFromIndex(self.position,1)    #remove from original spot
                    
                boardState[temp][1] = self.id       #add to new spot
                self.position = temp                #update self position
                if globalVars.turtleMode:
                    self.piece.goto(WhitePiece.path[temp][0],WhitePiece.path[temp][1])  #move turtle
                if temp == 4 or temp == 14:
                    #flower tile
                    return True
                else:
                    return False
            else:   #tile occupied by friendly piece, do nothing
                return False

    #send a piece back to start and update boardState        
    def reset(self):
        
        boardState[0][1] += 1
        removeFromIndex(self.position, 1)
        if globalVars.turtleMode:
            self.piece.goto(WhitePiece.path[0][0],WhitePiece.path[0][1])
        self.position = 0
