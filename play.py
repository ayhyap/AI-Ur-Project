import interface
import gameEngine
import random
import turtle

def play(p1,p2):
    gameEngine.setup()
    turn = random.randrange(0,2,1)
    turnCount = 0
    turnLimit = 200
    while interface.checkWin() == 0 and turnCount < turnLimit:
        turnCount += 1
        print ("turn number: " + str(turnCount))
        moves = interface.diceRoll()
        if turn == 0:
            #black turn
            print("BLACK TURN: " + str(moves))
            if moves == 0:
                print ("Unlucky! Black skips this turn.")
            else:
                if (p1 == 'h'):
                    valid = False
                    while valid == False:
                        valid = True
                        try:
                            pieceToMove = int(input("ENTER PIECE TO MOVE: "))
                        except:
                            valid = False
                            print("Invalid input!")
                else:
                    valid = False
                    while valid == False:
                        valid = True
                        try:
                            pieceToMove = int(input("ENTER PIECE TO MOVE: "))
                        except:
                            valid = False
                            print("Invalid input!")
                extraTurn = interface.move(0, pieceToMove, moves)
        else:
            #white turn
            print("WHITE TURN: "+ str(moves))
            if moves == 0:
                print("Unlucky! White skips this turn.")
            else:
                if (p2 == 'h') :
                    valid = False
                    while valid == False:
                        valid = True
                        try:
                            pieceToMove = int(input("ENTER PIECE TO MOVE: "))
                        except:
                            valid = False
                            print("Invalid input!")
                else:
                    valid = False
                    while valid == False:
                        valid = True
                        try:
                            pieceToMove = int(input("ENTER PIECE TO MOVE: "))
                        except:
                            valid = False
                            print("Invalid input!")
                extraTurn = interface.move(1, pieceToMove, moves)
                
        if extraTurn:
            print("Piece lands on a flowered tile, granting an EXTRA TURN!")
        else:
            turn += 1
            turn %= 2
    if turnCount >= turnLimit:
        print("Tie")
    else:
        if interface.checkWin() == -1:
            print("Black Wins")
        else:
            print("White Wins")

playerTypes = ['h']

p1 = ''
p2 = ''

while (p1 not in playerTypes or p2 not in playerTypes):
    print("The three player types are: (h)")
    p1 = input("player 1 is: (h)")
    p2 = input("player 2 is: (h)")
    if (p1 not in playerTypes or p2 not in playerTypes) :
        print("Your imputs are incorrect! Please try again!")
    
play(p1,p2)
turtle.done()
