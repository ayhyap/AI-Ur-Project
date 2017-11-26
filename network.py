import random
import math
def sigmoid(z):
    return 1/(1+math.exp(-z))
class network:
    global input_nodes
    global hidden_nodes
    global output_nodes
    input_nodes = 18
    hidden_nodes = 12
    output_nodes = 7

    #Function for initializing each network
    def __init__(self, child = False, mother = None, father = None):
        self.hiddenArray1 = []
        self.hiddenArray2 = []
        self.outputArray = []
        self.hiddenBias1 = []
        self.hiddenBias2 = []
        self.outputBias = []
        self.competence = False

        #This part of the code creates entirely random networks
    	if (child == False):
            for i in range(0, hidden_nodes, 1):
                self.hiddenArray1.append([])
                for j in range(0, input_nodes, 1):
                    self.hiddenArray1[i].append(random.uniform(-5, 5))
            for i in range(0, hidden_nodes, 1):
                self.hiddenArray2.append([])
                for j in range(0, input_nodes, 1):
                    self.hiddenArray2[i].append(random.uniform(-5, 5))
    	    for i in range(0, output_nodes, 1):
                self.outputArray.append([])
                for j in range(0, hidden_nodes, 1):
                    self.outputArray[i].append(random.uniform(-5, 5))
       	    for i in range(0, hidden_nodes, 1):
                self.hiddenBias1.append(random.uniform(-5, 5))
       	    for i in range(0, hidden_nodes, 1):
                self.hiddenBias2.append(random.uniform(-5, 5))
            for i in range(0, output_nodes, 1):
                self.outputBias.append(random.uniform(-5, 5))
        #This code creates a new network based on a father and mother network
        else :
            for i in range(0, hidden_nodes, 1):
                self.hiddenArray1.append([])
                for j in range(0, input_nodes, 1):
                    if (random.random() > 0.5) :
                        self.hiddenArray1[i].append(father.hiddenArray1[i][j])
                    else:
                        self.hiddenArray1[i].append(mother.hiddenArray1[i][j])
            for i in range(0, hidden_nodes, 1):
                self.hiddenArray2.append([])
                for j in range(0, input_nodes, 1):
                    if (random.random() > 0.5) :
                        self.hiddenArray2[i].append(father.hiddenArray2[i][j])
                    else:
                        self.hiddenArray2[i].append(mother.hiddenArray2[i][j])
            for i in range(0, output_nodes, 1):
                self.outputArray.append([])
                for j in range(0, hidden_nodes, 1):
                    if (random.random() > 0.5) :
                        self.outputArray[i].append(father.outputArray[i][j])
                    else:
                        self.outputArray[i].append(mother.outputArray[i][j])
            for i in range(0, hidden_nodes, 1):
                if (random.random() > 0.5) :
                    self.hiddenBias1.append(father.hiddenBias1[i])
                else :
                    self.hiddenBias1.append(mother.hiddenBias1[i])
            for i in range(0, hidden_nodes, 1):
                if (random.random() > 0.5) :
                    self.hiddenBias2.append(father.hiddenBias2[i])
                else :
                    self.hiddenBias2.append(mother.hiddenBias2[i])
            for i in range(0, output_nodes, 1):
                if (random.random() > 0.5) :
                    self.outputBias.append(father.outputBias[i])
                else :
                    self.outputBias.append(mother.outputBias[i])
    #Class method for creating a new network from a father and mother network
    @classmethod
    def child(cls, mother, father):
    	return cls(True, mother, father)

    #This function is where the network does it calculations.
    #It takes its weights, bias, and gamestate inputs and outputs a move.
    def run(self,inputs):
    	hidden1 = []
    	hiddenOutput1 = []
    	hidden2 = []
    	hiddenOutput2 = []
    	outputInputs = []
    	output = []
    	for i in range(0, hidden_nodes, 1):
            hiddenOutput1.append([])
            for j in range(0, input_nodes, 1):
            	hiddenOutput1[i].append(inputs[j] * self.hiddenArray1[i][j])
        for i in range(0, hidden_nodes, 1):
        	hidden1.append(sigmoid(sum([i - j for i, j in zip(hiddenOutput1[i], self.hiddenBias1)])))
        	
    	for i in range(0, hidden_nodes, 1):
            hiddenOutput2.append([])
            for j in range(0, hidden_nodes, 1):
            	hiddenOutput2[i].append(hidden1[j] * self.hiddenArray2[i][j])
        for i in range(0, hidden_nodes, 1):
        	hidden2.append(sigmoid(sum([i - j for i, j in zip(hiddenOutput2[i], self.hiddenBias2)])))
        	
    	for i in range(0, output_nodes, 1):
            outputInputs.append([])
            for j in range(0, hidden_nodes, 1):
            	outputInputs[i].append(hidden2[j] * self.outputArray[i][j])
        for i in range(0, output_nodes, 1):
        	output.append(sigmoid(sum(outputInputs[i])))
        return output.index(max(output))+1
    #This function mutates a network, changing the weights and bias
    def mutate(self):
    	for i in range(0, hidden_nodes, 1):
            for j in range(0, input_nodes, 1):
               	self.hiddenArray1[i][j] = self.hiddenArray1[i][j] * random.normalvariate(1,0.1)
        for i in range(0, hidden_nodes, 1):
            for j in range(0, input_nodes, 1):
               	self.hiddenArray2[i][j] = self.hiddenArray2[i][j] * random.normalvariate(1,0.1)
        for i in range(0, output_nodes, 1):
            for j in range(0, hidden_nodes, 1):
           	    self.outputArray[i][j] = self.outputArray[i][j] * random.normalvariate(1,0.1)
       	for i in range(0, hidden_nodes, 1):
           	self.hiddenBias1[i] = self.hiddenBias1[i] * random.normalvariate(1,0.1)
       	for i in range(0, hidden_nodes, 1):
           	self.hiddenBias2[i] = self.hiddenBias2[i] * random.normalvariate(1,0.1)
        for i in range(0, output_nodes, 1):
           	self.outputBias[i] = self.outputBias[i] * random.normalvariate(1,0.1)
