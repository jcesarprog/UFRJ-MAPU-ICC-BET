import random
from itertools import chain, combinations

class Player:
    def __init__(self, knowledge=[], ratings=[], cacife=1000):
        self.knowledge = knowledge
        self.ratings = ratings
        self.cacife = cacife

    def createKnowledge(self, size):
        knowledge = []
        for _ in range(size):
            knowledge.append(random.random())
        self.knowledge = knowledge
        return self.knowledge

    def powerset(self, iterable):
        # powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
        s = list(iterable)
        return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

    def createRatings(self, mask: list):
        ratingSize = 2**len(mask)
        maksSubsets = self.powerset(mask)
        ratings = []  
        
        # M = {1,3}
        # t0 = (1 - k[1])*(1 - k[3])
        # t1 = k[1] * (1 - k[3])
        # t2 = k[3] * (1 - k[1])
        # t3 = k[3] * k[1]
       
        for ms in maksSubsets:
            t0 = 1
            if len(ms) == 0:
                for m in mask:
                    t0 *= (1-self.knowledge[m]) 
                ratings.append(t0)
                # print(t0)            
            else:
                tx = 1
                used = []
                # multiply part1 - used
                for i in range(len(ms)):
                    tx *= self.knowledge[ms[i]]
                    used.append(ms[i])
                # print("used", used)
                # Getting the diff beteween the lists as sets
                notUsed = list(set(mask)-set(used))
                # print(notUsed)
                # multiply part2 - notUsed
                for i in notUsed:
                    tx *= (1- self.knowledge[i])
                ratings.append(tx)

        self.ratings = ratings
        self.ratesSum = sum(self.ratings)
        return self.ratings

        
    def bet(self):
        pass

    def reset(self):
        knowledge = []
        ratings = []
        cacife = 1000
