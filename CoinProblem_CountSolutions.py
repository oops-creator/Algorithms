import math 
import time

coins = [int(i) for i in input('Enter space seperated coins ').split()]
count = {}
count[0] = 1


def solve(x):
    if x in count.keys():
        return count[x]
    for i in range(1,x+1):
        count[i] = 0
        for c in coins:
            if i-c>=0:
                count[i] += count[i-c]
    return count[x]


while True:

    x = input('Enter the required number ')
    start = time.time()
    print(solve(int(x)))
    print(time.time() - start)