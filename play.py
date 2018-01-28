import interface
import gameEngine
import random
import turtle
import expectimax
import copy

def play(p1,p2):
    gameEngine.setup()
    turn = random.randrange(0,2,1)
    turnCount = 0
    turnLimit = 400
    while interface.checkWin() == 0 and turnCount < turnLimit:
        extraTurn = False
        turnCount += 1
        #print ("turn number: " + str(turnCount))
        moves = interface.diceRoll()
        if turn == 0:
            #black turn
            print("B",moves)
            if moves == 0:
                print ("Unlucky!")
            else:
                if p1[0] == 'e':
                    pieceToMove = expectimax.run(copy.deepcopy(gameEngine.boardState), moves, 0, int(p1[1:]))
                elif p1 == 'r':
                    pieceToMove = random.randrange(1,8,1)
                else:
                    valid = False
                    while valid == False:
                        valid = True
                        try:
                            pieceToMove = int(input("ENTER PIECE TO MOVE: "))
                            if pieceToMove > 7 or pieceToMove < 0:
                                raise Exception("OOB")
                        except:
                            valid = False
                            print("Invalid input!")
                print(">>>", pieceToMove)
                extraTurn = interface.move(0, pieceToMove, moves)
        else:
            #white turn
            print("W",moves)
            if moves == 0:
                print("Unlucky!")
            else:
                if p2[0] == 'e':
                    pieceToMove = expectimax.run(copy.deepcopy(gameEngine.boardState), moves, 1, int(p2[1:]))
                elif p2 == 'r':
                    pieceToMove = random.randrange(1,8,1)
                else:
                    valid = False
                    while valid == False:
                        valid = True
                        try:
                            pieceToMove = int(input("ENTER PIECE TO MOVE: "))
                            if pieceToMove > 7 or pieceToMove < 0:
                                raise Exception("OOB")
                        except:
                            valid = False
                            print("Invalid input!")
                print(">>>", pieceToMove)
                extraTurn = interface.move(1, pieceToMove, moves)
                
        if extraTurn:
            print("EXTRA TURN!")
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

playerTypes = ['h','e','r']

p1 = ''
p2 = ''

while (p1 not in playerTypes or p2 not in playerTypes):
    print("The three player types are: (h)uman, (e)xpectimax, (r)andom")
    p1 = input("player 1 is: ")
    p2 = input("player 2 is: ")
    if (p1 not in playerTypes or p2 not in playerTypes) :
        print("Your inputs are incorrect! Please try again!")

eValid = ['1','2','3','4','5','6']

if p1 == 'e':
    invalid = True
    while invalid:
        try:
            depth = input("input expectimax depth for p1:")
            if depth not in eValid:
                print("Invalid Input!")
            else:
                p1 += str(depth)
                invalid = False
        except:
            print("Invalid Input!")
            
            
if p2 == 'e':
    invalid = True
    while invalid:
        try:
            depth = input("input expectimax depth for p2:")
            if depth not in eValid:
                print("Invalid Input!")
            else:
                p2 += str(depth)
                invalid = False
        except:
            print("Invalid Input!")

play(p1, p2)
##bwins = 0
##wwins = 0
##for _ in range(21):
##    play(p1,p2)
##    winner = interface.checkWin()
##    if winner == -1:
##        bwins += 1
##    elif winner == 1:
##        wwins += 1
##
##print("=====")
##print("=====")
##print("BLACK:", bwins)
##print("WHITE:", wwins)
