def partition(arr , low, high):
    i = low
    pivot = arr[low]
    j = high+1
    for x in range(high , i , -1):
        if arr[x] > pivot:
            j = j-1
            arr[j] , arr[x] = arr[x] , arr[j]
    arr[j-1] , arr[low] = arr[low] , arr[j-1]
    return j-1


def quickSort(arr,low,high): 
	if low < high: 
		k = partition(arr,low,high)  
		quickSort(arr, low, k-1) 
		quickSort(arr, k+1, high) 

arr = [421,513,5,36,7,549,5]

quickSort(arr,0,len(arr)-1) 
print(arr)

        


