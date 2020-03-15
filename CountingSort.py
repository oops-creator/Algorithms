def counting(A):
    maximum = max(A)
    count = [0] * (maximum+1)
    for i in A:
        count[i] +=1
    for i in range(1,len(count)):
        count[i] = count[i] + count[i-1]
    arr = [0] * len(A)
    for i in range(len(A)-1 , -1 , -1):
        arr[count[A[i]]-1] = A[i]
        count[A[i]]-=1
    return arr


array = [1,2,3,4,5]
print(counting(array))
