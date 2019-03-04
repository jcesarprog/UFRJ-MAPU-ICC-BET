import random
class Item:
    def __init__(self, name: str, profit: float, weight:float):
        self.name = name
        self.profit = profit
        self.weight = weight
    
    
items_List = []

for i in range(20):
    items_List.append(Item('Item-'+str(i),random.randint(1,10),random.randint(1,7)))

items_name, items_profit, items_weight = [], [], []

# Sorting the Item list 
items_List = sorted(items_List, key = lambda i: i.weight, reverse = True)

for i in items_List:
    items_name.append(i.name)
    items_profit.append(i.profit)
    items_weight.append(i.weight)
