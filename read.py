import network as weights
import csv

networksBest = []

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
