import Test2 as board
import Test as init
import weights
import csv
import random
import multiprocessing
#import ExMax.py

#Prints a networks information to a csv file for future use
def write(network, string):
    with open('network'+string+'.csv','wb') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        for i in range(0,len(network.hiddenArray1),1):
            wr.writerow(network.hiddenArray1[i])
        for i in range(0,len(network.hiddenArray2),1):
            wr.writerow(network.hiddenArray2[i])
        for i in range(0,len(network.outputArray),1):
            wr.writerow(network.outputArray[i])
        wr.writerow(network.hiddenBias1)
        wr.writerow(network.hiddenBias2)
        wr.writerow(network.outputBias)

#Reads a file in a creates a network with the information
def read(string):
    with open('network'+string+'.csv','rb') as csvfile:
        rd = [list(map(float,rec)) for rec in csv.reader(csvfile, delimiter=',')]
        temp = []
        x = int(string)-1
        y = 0
        networksBest.append(weights.network())
        for row in rd:
            temp.append(row)
        for i in range(0,12,1):
            networksBest[x].hiddenArray1[i] = temp[y]    
            y += 1
        for i in range(0,12,1):
            networksBest[x].hiddenArray2[i] = temp[y]
            y += 1
        for i in range(0,7,1):
            networksBest[x].outputArray[i] = temp[y]
            y += 1
        networksBest[x].hiddenBias1 = temp[y]
        y += 1
        networksBest[x].hiddenBias2 = temp[y]
        y += 1
        networksBest[x].outputBias = temp[y]


#Test code for read write functions
##write(networks[1],'1')
##read('1')
##write(networksBest[0],'2')

# Test code for child and mutate function
##testFather = weights.network()
##testFather.hiddenArray1 = [[0 for col in range(18)] for row in range(12)]
##testFather.hiddenArray2 = [[0 for col in range(18)] for row in range(12)]
##testFather.outputArray = [[0 for col in range(12)] for row in range(7)]
##testFather.hiddenBias1 = [0] * 12
##testFather.hiddenBias2 = [0] * 12
##testFather.outputBias = [0] * 7
##
##testMother = weights.network()
##testMother.hiddenArray1 = [[1 for col in range(18)] for row in range(12)]
##testMother.hiddenArray2 = [[1 for col in range(18)] for row in range(12)]
##testMother.outputArray = [[1 for col in range(12)] for row in range(7)]
##testMother.hiddenBias1 = [1] * 12
##testMother.hiddenBias2 = [1] * 12
##testMother.outputBias = [1] * 7
##
##testChild = weights.network.child(testMother, testFather)
##testChild.mutate()
##print(testChild.hiddenArray1)


def play(player1, player2):
    
    init.screenSetup()
    for i in range(7):
        init.setScore(init.blackStartCount,i+1)
        init.BlackPiece()
        #blackPieces.append(init.BlackPiece())
        init.setScore(init.whiteStartCount,i+1)
        init.WhitePiece()
        #whitePieces.append(init.WhitePiece())


    turn = int(random.randrange(0,2,1))
    turn_count = 1
    turn_limit = 200

    init.resetBoard()
    #MAIN LOOP
    while (board.checkWin() == 0):
        if (turn_count >= turn_limit):
            break
        turn_count += 1
##        print(turn_count)
##        print(turn)
        moves = board.diceRoll()
        if turn == 0:
            #black turn
            if moves == 0:
                turn += 1
                turn %= 2
                continue
            pieceToMove = player2.run(board.nnInputGen(moves))
            extraTurn = board.move(0,pieceToMove,moves)
        else:
            #white turn
            if moves == 0:
                turn += 1
                turn %= 2
                continue
            pieceToMove = player1.run(board.nnInputGen(moves))
            extraTurn = board.move(1,pieceToMove,moves)

        if extraTurn:
            turn_count += 0
        else:
            turn += 1
            turn %= 2
    if (turn_count >= turn_limit):
        return board.breakTie()
    return board.checkWin()

#This function will eventually have Networks play against each other. Current set for round robbin
def train():
    global wins
    for i in range(0, len(networks) - 1,1):
        for j in range(i+1, len(networks),1):
##            print("White (" + str(i) + ") VS Black (" + str(j) + ")")
            winner = play(networks[i],networks[j])
            if winner == 1:
##                print "White wins"
                wins[i] += 1
            elif winner == -1:
##                print "Black wins"
                wins[j] += 1
            else:
                continue
##                print "TIE"


##train()
##print(wins)
##print(len(wins))
#this function deletes networks based on the number of games won.
#Deletes until there are only 50 networks remaining.
def cull():
    for i in range(0,len(networks)-50,1):
        x = wins.index(min(wins))
        del networks[x]
        del wins[x]

##After deleteing networks, this function breeds the survivors to create childen
##Also adds 10 randomly generated immigrants
##def repopulate():
##    for i in range(0,25,1):
##        networks.append((weights.network.child(networks[i],networks[49-i]).mutate()))
##        networks.append((weights.network.child(networks[i],networks[i+1]).mutate()))
##    for i in range(0,10,1):
##        networks.append(weights.network())


def Matchmaker(ppl):
    global generation
    gap = ppl/2 - generation
    if gap < 1:
        gap = 1
    for i in range(0, gap, 1):
        networks.append(weights.network.child(networks[i],networks[i+gap]))
    for i in range(gap*2, ppl, 2):
        networks.append(weights.network.child(networks[i],networks[i+1]))




def trainWorker(i,j, return_queue, networkI, networkJ):
##def trainWorker(i,j):
    winner = play(networkI,networkJ)
    if winner == 1:
        #print str(i) + " WIN  " + str(j)
        return_queue.put(i)
    elif winner == -1:
        #print str(i) + " LOSE " + str(j)
        return_queue.put(j)
        #print str(i) + " TIE  " + str(j)
    return


##def multiTrain():
if __name__ == '__main__':
    print "INITIALIZATION"
    networksBest = []
    networks = []
    wins = []

    generation = 0
    generation_limit = 100

    
    #Generates 100 networks and initializes a list to count the amount of game wins for each network
    for i in range(0,100,1):
        networks.append(weights.network())
        wins.append(0)

    
    queue1 = multiprocessing.Queue()
    queue2 = multiprocessing.Queue()

    queues = [queue1, queue2]


    for h in range(0,generation_limit,1):
    
        print "==BEGIN " + str(h) + "th GENERATION ROUND ROBIN=="
        for i in range(0, len(networks) - 1,1):
            qIndex = i%2
            print "Competitor: " + str(i)
            jobs = []
            for j in range(i+1, len(networks),1):
                p = multiprocessing.Process(target = trainWorker, args=(i,j,queues[qIndex], networks[i], networks[j]))
                jobs.append(p)
                p.start()
                if len(jobs) == 8:
                    jobs[0].join()
                qIndex = (i+1)%2
            while queues[qIndex].empty() == False:
                wins[queues[qIndex].get()] += 1
            for proc in jobs:
                proc.join()
            

        
                
        print str(h) + "th ROUND ROBIN RESULTS:"
        print wins
        print "Average: " + str(float(sum(wins))/len(wins))
        print "Max: " + str(max(wins))
        print "Min: " + str(min(wins))
        print('Culling Networks')    
        cull()
        print('Repopulating Networks')
        x = len(networks)
        Matchmaker(x)
        Matchmaker(x)
        for i in range(0,10,1):
            networks.append(weights.network())
        print(len(networks))
        generation += 1
        wins = []
        for i in range(0,len(networks),1):
            wins.append(0)

    write(networks[wins.index(max(wins))],'1')
    del networks[wins.index(max(wins))]
    del wins[wins.index(max(wins))]
    write(networks[wins.index(max(wins))],'2')
    del networks[wins.index(max(wins))]
    del wins[wins.index(max(wins))]
    write(networks[wins.index(max(wins))],'3')
    del networks[wins.index(max(wins))]
    del wins[wins.index(max(wins))]


#### 4950 games are played per generation with 100 networks
#### 5995 games are played per generation with 110 networks
##for i in range(0,generation_limit,1):
##    print('Training Networks')
##    train()
##    print(wins)
##    print('Culling Networks')    
##    cull()
##    print('Repopulating Networks')
##    x = len(networks)
##    Matchmaker(x)
##    Matchmaker(x)
##    for i in range(0,10,1):
##        networks.append(weights.network())
##    print(len(networks))
##    generation += 1
##    wins = []
##    for i in range(0,len(networks),1):
##        wins.append(0)
##    
##
##
##write(networks[wins.index(min(wins))],'1')
##del networks[wins.index(min(wins))]
##del wins[wins.index(min(wins))]
##write(networks[wins.index(min(wins))],'2')
##del networks[wins.index(min(wins))]
##del wins[wins.index(min(wins))]
##write(networks[wins.index(min(wins))],'3')
##
