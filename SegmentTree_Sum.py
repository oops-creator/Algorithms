arr = [int(i) for i in input("Enter the array ").split()]
n  = len(arr)

import math
segmentTree = [0]*(2*(2**math.floor(math.log(n,2))))
m = len(segmentTree)

def buildTree():
    for i in range(n) :  
        segmentTree[n + i] = arr[i] 
    for i in range(n - 1, 0, -1) :  
        segmentTree[i] = segmentTree[2*i+1] + segmentTree[2*i]

buildTree()

def sumOfVal(a,b):
    a+=n
    b+=n
    total = 0
    while a<=   b:
        if a%2==1:
            total+=segmentTree[a]
            a+=1
        if b%2==0:
            total+=segmentTree[b]
            b-=1
    
        a//=2
        b//=2
    return total

def update(pos , increment):
        pos+=n
        segmentTree[pos] +=increment
        pos//=2
        while pos>=1:
            segmentTree[pos] = segmentTree[2*pos] + segmentTree[2*pos+1]
            pos//=2


while True:
    start = int(input("Enter the start index "))
    end = int(input("Enter the end index "))
    print(sumOfVal(start,end))

 
    