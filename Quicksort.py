def partition(arr,low,high): 
	i = ( low-1 )		 
	pivot = arr[high]	 
	for j in range(low , high): 
		if arr[j] < pivot: 
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 
	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return  i+1  

def quickSort(arr,low,high): 
	if low < high: 
		k = partition(arr,low,high)  
		quickSort(arr, low, k-1) 
		quickSort(arr, k+1, high) 

arr = [421,513,5,36,7,549,5]


toSearch = input('Enter the array seperated by space\n')
arr = [int(i) for i in toSearch.split()]
quickSort(arr ,0 , len(arr)-1 )
print (arr)
#quickSort(arr,0,len(arr)-1) 
#print(arr)

