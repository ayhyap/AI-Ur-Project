generation = 0

def Matchmaker(ppl):
    global generation
    temp = []
    gap = ppl/2 - generation
    if gap < 1:
        gap = 1
    for i in range(0, gap, 1):
        temp.append([i,i+gap])
    for i in range(gap*2, ppl, 2):
        temp.append([i,i+1])
    generation += 1
    return temp
