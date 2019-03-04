from Knapsack import firstGreedyChoice
import random
class Bank:
    def __init__(self, players_list: list, nPicks: list, mask = [], trSize = 1):
        self.players_list = players_list
        self.nPicks = nPicks
        self.mask = mask
        self.trSize = trSize
        self.bankCacife = float("inf")
        self.bankQuotations = []
    

    def createFirstMask(self, size=3):
        maskSize = len(firstGreedyChoice()[2])
        mask = []
        for _ in range(size):
            r = random.randint(0,maskSize-1)
            if r not in mask:
                mask.append(r)
            else:
                while r in mask:
                    r = random.randint(0,maskSize-1)
                mask.append(r)
        self.mask = mask
        return self.mask

    def createBankQuotations(self, players_list = []):
        sums = []
        for m in range(2**len(self.mask)):            
            total = 0
            for p in players_list:
                total += p.ratings[m]
            sums.append(total)        
        print("\nSUMS:",sums)

        bankQuotations = list(map(lambda x: (1/x), sums))
        print("\nBANKQUOT:",bankQuotations)
        self.bankQuotations = bankQuotations
        return self.bankQuotations


    def best(self):
        pass

