def bin(A , num , low , high):
    if low == high and A[low] == num:
        return low
    elif low==high and A[low] != num:
        return -1
    mid = (low+high)//2
    if A[mid] == num:
        return mid
    elif A[mid] < num:
        return bin(A,num , mid+1 , high)
    elif A[mid] > num:
        return bin(A,num,low , mid)
    return -1

toSearch = input('Enter the sorted array seperated by space\n')
arr = list(toSearch.split())
number = input('Enter the number to search\n')
print('The index is :' , bin(arr , number , 0 , len(arr)-1 ))

#arr = [1,2,3,4,5,675,8654]
#print(bin(arr , 3 , 0 , len(arr)-1))