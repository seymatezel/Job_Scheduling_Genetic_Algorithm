# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:59:19 2024

@author: Şeyma_Tezel 
"""
#Random 4 rankings
from random import shuffle
list=[[3,4,5],
       [5,7,10],
       [2,3,5],
       [8,10,10],
       [4,9,5],
       [1,3,10],
       [3,8,5],
       [7,9,10],
       [6,11,10],
       [2,4,5],
       [4,5,10]]
rankings= []
costs=[]
for i in range(4):
    order_of_work=[0,1,2,3,4,5,6,7,8,9,10]
    shuffle(order_of_work)
    rankings.append(order_of_work)
for  order_of_work in rankings:
    time=0
    cost=0
    for j in order_of_work:
        time+=list[j][0]
        delay=time-list[j][1]
        if delay>0:
            cost+=delay*list[j][2]
    print( order_of_work, "   Total Cost:", cost)
    
 
#The two least expensive of these four randomly generated 
    costs.append(cost)
the_cheapest1_cost=min(costs) 
the_cheapest1_ranking = costs.index(the_cheapest1_cost)
print("The Best Solution 1: ", rankings[the_cheapest1_ranking], "      Total Cost:",the_cheapest1_cost )
costs.remove(the_cheapest1_cost)
the_cheapest2_cost=min(costs)
the_cheapest2_ranking = costs.index(the_cheapest2_cost)
print("The Best Solution 2: ", rankings[the_cheapest2_ranking], "      Total Cost:", the_cheapest2_cost)


#Single-Point Crossover (Permutation-based Crossover)
from random import randint
crossover_point = randint(1, 10)
print ("Generated Random Number ForSingle-Point Crossover : " ,crossover_point)
print("The Best Solution 1: ", rankings[the_cheapest1_ranking], "      Total Cost:",the_cheapest1_cost )
print("The Best Solution 2: ", rankings[the_cheapest2_ranking], "      Total Cost:", the_cheapest2_cost)
new_ranking1 =rankings[the_cheapest1_ranking][:crossover_point]
for k in rankings[the_cheapest2_ranking]:
    if k not in new_ranking1:
        new_ranking1.append(k)

new_ranking2 =rankings[the_cheapest2_ranking][:crossover_point]
for k in rankings[the_cheapest1_ranking]:
    if k not in new_ranking2:
        new_ranking2.append(k)

time=0
cost1=0
for x in new_ranking1:
    time=time+list[x][0]
    delay= time-list[x][1]
    if delay>0:
        cost1=cost1+ delay*list[x][2] 
print("New Ranking1:", new_ranking1, "    Total Cost:", cost1)

time=0
cost2=0
for x in new_ranking2:
    time=time+list[x][0]
    delay= time-list[x][1]
    if delay>0:
        cost2=cost2+ delay*list[x][2] 
print("New Ranking2:", new_ranking2, "    Total Cost:", cost2)

#The minimum cost among the 4 sequences
rankings2 =[rankings[the_cheapest1_ranking],rankings[the_cheapest2_ranking],new_ranking1, new_ranking2 ]
costs2=[the_cheapest1_cost,the_cheapest2_cost, cost1, cost2]
the_cheapest_cost=min(costs2)
the_cheapest_ranking=costs2.index(the_cheapest_cost)
print("The Best Ranking:" ,rankings2[the_cheapest_ranking],"Total Cost:",the_cheapest_cost)


#Mutation
random_number2=randint(0,10)
random_number3=randint(0,10)
while random_number2==random_number3:
    random_number3=randint(0,10)  
print("Generated Random Number For Mutation :",random_number2," and ",random_number3 )

mutated_ranking = rankings2[the_cheapest_ranking].copy()
a=mutated_ranking[random_number2]
mutated_ranking[random_number2]=mutated_ranking[random_number3]
mutated_ranking[random_number3]=a

time=0
mutated_cost=0
for y in mutated_ranking:
    time=time+list[y][0]
    delay= time-list[y][1]
    if delay>0:
        mutated_cost+= delay*list[y][2] 
print("Mutated Ranking:", mutated_ranking, "    Total Cost:", mutated_cost)
print("Not Mutated Ranking:",rankings2[the_cheapest_ranking],"Total Cost:",the_cheapest_cost)
    
rankings3=[mutated_ranking,rankings2[the_cheapest1_ranking]]
costs3=[mutated_cost, the_cheapest_cost]
the_cheapest_cost2=min(costs3)
the_cheapest_ranking2=costs3.index(the_cheapest_cost2)
print("Final The Best Ranking:" ,rankings3[the_cheapest_ranking2],"Total Cost:",the_cheapest_cost2)





