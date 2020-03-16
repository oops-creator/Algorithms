import math 
import time

#Dynamic Programming: Find min number of coins required to create a total. Returns math.inf if not possible using coins.
coins = [int(i) for i in input('Enter space seperated coins ').split()]
memory = {0:0}

def solve(x):
    if x in memory.keys():
        return memory[x]
    for i in range(1,x+1):
        memory[i] = math.inf
        for c in coins:
            if i-c>=0 :
                memory[i] = min(memory[i-c]+1 , memory[i])

    return memory[x]
    


while True:
    x = input('Enter the required number ')
    start = time.time()
    print(solve(int(x)))
    print(time.time()-start)