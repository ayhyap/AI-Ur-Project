# notes : for simplicity we assume we could have equal chance for all posible states (including the extra steps)
# the function at the bottom shows an example of how to call the expectimax
# depth of 2 or above take long time to process
import Test as init
import copy
from operator import itemgetter
import sys
sys.setrecursionlimit(1000000)

class Score(object):
   DISTANCE = 1.0
   ALLY_FLOWER = -1.0
   FINISH = 2.0
   WAR_AREA = -1.0

class Color (object):
    WHITE = 1
    BLACK = 0
def updateFutureBoardState(boardState,futureBoardStates, indexOfPieceToMove, step, color,isRoot ,isExtra, policyFromParent):
   newBoardState = copy.deepcopy(boardState[0])      # deep copy of a board state ####changed
   destination = indexOfPieceToMove + step
   flowerTiles= {4,8,14}
   if destination >= 15:                               #arrive endpoint
       newBoardState[indexOfPieceToMove][color] -= 1
       newBoardState[15][color] += 1

   if destination >= 1 and destination < 15:
       if havePieces(newBoardState,color,destination):     # It is not posible to move the piece to the grid which is full
           newBoardState =  None
       else:                                       # when it is a legit step
           newBoardState[destination][color] += 1
           newBoardState[indexOfPieceToMove][color] -= 1
           if newBoardState[destination][opponentColor(color)] == 1 and destination in range(5,13):
               newBoardState[0][abs(color - 1)] += 1    
               newBoardState[destination][opponentColor(color)] -= 1
           if destination in flowerTiles:
               if isRoot:
                    extraTurnHandler(futureBoardStates, [(newBoardState, indexOfPieceToMove)], color ,indexOfPieceToMove)
               else:
                    extraTurnHandler(futureBoardStates, [(newBoardState, boardState[1])], color, policyFromParent)
               newBoardState = None

   if newBoardState is not None:                          # add newboardState
       # if (newBoardState, indexOfPieceToMove) not in futureBoardStates:
            if isExtra == True :
                futureBoardStates.append((newBoardState, policyFromParent))
            elif isRoot == True:
                futureBoardStates.append((newBoardState,indexOfPieceToMove))
            else:
                futureBoardStates.append((newBoardState,boardState[1]))

def opponentColor(color):
   return abs(color-1)

def havePieces(boardState,color,place):
   if(boardState[place][color] >= 1):
       return True
   return False
def extraTurnHandler (futureBoardStates, boardStates , color, inheritedPolicy):
    futureBoardStatesByChanceNode = []
    for states in boardStates:
        for step in range(0, 5):
            for gridNum in range(0, 15):
                if havePieces(states[0], color, gridNum) == True:
                    updateFutureBoardState(states, futureBoardStates, gridNum, step, color, False, True, inheritedPolicy) #

def getBoardStatesByChanceNode(futureBoardStates, boardStates , colorOfOpponent):                  # helper function that takes a list of BS and return all posible states by CN
   futureBoardStatesByChanceNode = []
   for states in boardStates:
       for step in range(0,5):
           for gridNum in range(0, 15):
               if havePieces(states[0],colorOfOpponent,gridNum) == True:
                   updateFutureBoardState(states,futureBoardStates, gridNum, step, colorOfOpponent, False ,False ,states[1])

def valuePolicyEvaluator(valuesAndPolicies):
   policyList = [x[1] for x in valuesAndPolicies]
   policyCountList  = [ [x, policyList.count(x)] for x in set(policyList)]
   expectedPolicyList = []
   for policyCount in policyCountList:
       sum = 0
       for x in valuesAndPolicies:
           if x[1] == policyCount[0]:
               sum += x[0]
       expectedPolicyList.append((sum / policyCount[1],policyCount[0]))
   return max(expectedPolicyList, key=itemgetter(0))

def expectiMaxIterate(boardState, step, color, depth, isRoot):                          #return value and policy
   futureBoardStates = []
   futureBoardStatesByChanceNode = []
   for counter in range(0,15):                                                 #get all posible future Board States  ** range(0-15) = 0-14
       if havePieces(boardState[0], color, counter):                              # if ctr + step = extra turn consideration has not been added
           updateFutureBoardState(boardState,futureBoardStates, counter, step , color, isRoot, False , boardState[1])

   getBoardStatesByChanceNode(futureBoardStatesByChanceNode,futureBoardStates,opponentColor(color))
   valuesAndPolicies = []
   if depth > 1:                                    #recurse and return
       for diceRoll in range(0,5):
           for states in futureBoardStatesByChanceNode :
               valuesAndPolicies.append( expectiMaxIterate(states,diceRoll,color,depth-1,False) )
       return valuePolicyEvaluator(valuesAndPolicies)

   for states in futureBoardStatesByChanceNode:
       valuesAndPolicies.append( (calculate(states[0],color),states[1]) )

   return valuePolicyEvaluator(valuesAndPolicies)




def getQuantitizedBoardState(boardstate):
  temp = []
  temp.append(boardstate[0])
  for i in range(1, 5):
      if boardstate[i][0] != 0 and boardstate[i][1] != 0:
          temp.append([1,1])
      elif boardstate[i][0] == 0  and boardstate[i][1] != 0:
          temp.append([0,1])
      elif boardstate[i][0] != 0 and boardstate[i][1] == 0:
          temp.append([1,0])
      else :temp.append([0,0])

  for i in range(5, 13):
      if boardstate[i] == 0:
          temp.append([0,0])
      elif boardstate[i] > 0:
          temp.append([0,1])
      elif boardstate[i] < 0:
          temp.append([1,0])

  for i in range(13, 15):
      if boardstate[i][0] != 0 and boardstate[i][1] != 0:
          temp.append([1,1])
      elif boardstate[i][0] == 0 and boardstate[i][1] != 0:
          temp.append([0,1])
      elif boardstate[i][0] != 0 and boardstate[i][1] == 0:
          temp.append([1,0])
      else :temp.append([0,0])

  temp.append(boardstate[-1])
  return (temp,-1)

def calculate(boardstate,color):
   score = 0.0
   for i in range (0,16):
       score += boardstate[i][color] * i *Score.DISTANCE
       score -= boardstate[i][opponentColor(color)] * i * Score.DISTANCE
       if i in range(5,13):
           score += (boardstate[i][color] * Score.WAR_AREA)
           score -= boardstate[i][opponentColor(color)] * Score.WAR_AREA
       if i in {4,14}:
           score += (boardstate[i][color] * Score.ALLY_FLOWER)
           score -= boardstate[i][opponentColor(color)] * Score.ALLY_FLOWER
       if i in {16}:
           score += (boardstate[i][color] * Score.FINISH)
           score -= boardstate[i][opponentColor(color)] * Score.FINISH

   return score

def numOfPiece(bs,index,color):
    temp = index
    pNum = 0
    for i in range(15, -1, - 1):
        pNum += bs[i][color]
        if i == index:
            return pNum



   # print expectiMaxIterate(([[2, 5], [1, 0], [1, 0], [1, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 1]], -1), 4, Color.BLACK, 1 ,True)

def moveByExpectimax(bs,color,step,depth):
    boardstate = getQuantitizedBoardState(bs)
    index= expectiMaxIterate(boardstate, step, color, depth, True)[1]    # 1 for our diceroll is 1 ,2 for depth of 2,allway input true in the 5th parameter
    return numOfPiece(boardstate[0],index,color)                                            # it will return (the value of the root node, the policy evaluated by the expectimax)
                                                             # the policy means which board index that we should move a piece from that index
