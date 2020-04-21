#arr = [int(i) for i in input().split()]

import time
import random

arr = random.choices(range(9999999) , k=999999)



k = 0
start = time.time()

for i in arr:
    k=i
    k+=1
    k-=1
    k=i
    k+=1
    k-=1
    k=i
    k+=1
    k-=1
    k=i
    k+=1
    k-=1


end = time.time()
print(end-start)

start = time.time()
arr.sort()
end = time.time()
print(end-start)
