"""
1. Selecionar solução aleatória inicial valida, de forma gulosa (ok)
2. O critério de parada foi satisfeito? (OK - 'if')
3. Fim (OK - 'break' )
4. Selecionar máscara aleatória (primeira mask da banca OK)
5. Calcular os pesos dos jogadores para cada escolha
6. Calcular as apostas dos jogadores e efetivá-las
7. Aplicar transformações à melhor solução e atualizar seu valor se pertinente
8. Pagar os prêmios das apostas vencedoras dos jogadores
9. Remover jogadores que quebraram substituindo-os por novos

"""

from Bank import Bank
from Item import Item, items_List, items_name, items_profit, items_weight
from Knapsack import Knapsack, firstGreedyChoice
from Player import Player
import random

bag = Knapsack()

print(bag.capacity)
# print(firstGreedyChoice()[0])
# print(firstGreedyChoice()[1]) 
""" 
f_greedyW, f_greedyV, f_greedyC = firstGreedyChoice() 
print(f_greedyW)
print(f_greedyV)
print(f_greedyC)
 """

# print(items_List, '\n', items_name, '\n', items_profit, '\n', items_weight)

""" 
p1 = Player()
f_greedyW, f_greedyV = firstGreedyChoice() 
p1.createKnowledge(len(f_greedyW))
print("Player_K:", p1.knowledge)
"""


# f_greedyW, f_greedyV = firstGreedyChoice() 
# print(f_greedyW)
# print(f_greedyV)

# print(random.sample(range(100), 10))

bank = Bank([],[])
mask = bank.createFirstMask(3)
print("Mask:", mask) 
# firstGreedyChoice()

players_list = []
for _ in range(20):
    p = Player()
    p.createKnowledge(len(items_List))
    p.createRatings(mask)
    players_list.append(p)

print("rantings:")
for p in players_list:
    print(p.ratings)

bank.createBankQuotations(players_list)


