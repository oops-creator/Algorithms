def partition(arr , low, high):
    i = low
    pivot = arr[low][2]
    j = high+1
    for x in range(high , i , -1):
        if arr[x][2] > pivot:
            j = j-1
            arr[j] , arr[x] = arr[x] , arr[j]
    arr[j-1] , arr[low] = arr[low] , arr[j-1]
    return j-1


def quickSort(arr,low,high): 
	if low < high: 
		k = partition(arr,low,high)  
		quickSort(arr, low, k-1) 
		quickSort(arr, k+1, high) 

weights = [int(i) for i in input("Enter the weights ").split()]
profits =  [int(i) for i in input("Enter the respective profits ").split()]
profitperweights = []
maxWeight = int(input('Enter max capacity of knapsack '))

for i in range(len(weights)):
    profitperweights.append(profits[i]/weights[i])

combi = list(zip(weights,profits,profitperweights))

quickSort(combi,0,len(combi)-1)

combi = combi[::-1]

counter = 0
allowedWeights = []
profit = 0
while maxWeight:
    if maxWeight-combi[counter][0]>=0:
        allowedWeights.append([combi[counter][0],1])
        maxWeight = maxWeight-combi[counter][0]
        profit+=combi[counter][1]
        counter+=1
    elif maxWeight!=0:
        fraction = maxWeight/combi[counter][0]
        allowedWeights.append([combi[counter][0],fraction])
        profit+=(combi[counter][1]*fraction)
        break

print(allowedWeights)
print(profit)

    
    









