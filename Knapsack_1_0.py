weightsList  = [int(i) for i in input('Enter the weights\n').strip().split()]
profitsList = [int(i) for i in input('Enter the profits\n').strip().split()]

mw = int(input('Enter the max weight\n'))

def knapSack(W, wtList, valList): 
    n = len(valList)
    K = [[0 for x in range(W + 1)] for x in range(n + 1)] 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wtList[i-1] <= w: 
                K[i][w] = max(valList[i-1] + K[i-1][w-wtList[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w]
    return K[n][W] 

print(knapSack(mw , weightsList , profitsList))
    