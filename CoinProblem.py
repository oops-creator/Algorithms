import math 
import time

#Dynamic Programming: Find min number of coins required to create a total. Returns math.inf if not possible using coins.
coins = [int(i) for i in input('Enter space seperated coins ').split()]
memory = {}

def solve(x):
    if x<0:
        return math.inf

    if x==0:
        return 0

    if x in memory.keys():
        return memory[x]
    
    best = math.inf
    for c in coins:
        best = min(solve(x-c) +1 , best)
    memory[x] = best

    return best


while True:
    x = input('Enter the required number ')
    print(solve(int(x)))
