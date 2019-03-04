from Item import items_weight, items_List

class Knapsack:
    def __init__(self, capacity = 15.0):
        self.capacity  = capacity
    
def firstGreedyChoice():
    bag = Knapsack()
    weightSum = 0
    i = 0
    maxSize = len(items_List)
    choice = []
    while weightSum < sum(items_weight):
        weightSum += items_weight[i]        
        if weightSum > bag.capacity:
            break
        choice.append(1)
        i += 1

    while maxSize > len(choice):
        choice.append(0)

    return items_weight[:i], items_List[:i], choice



        
        
