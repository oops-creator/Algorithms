import countingSort

def sort(arr):
    maxlen = 0
    for i in arr:
        maxlen = max(maxlen , len(i))
    for i , val in enumerate(arr):
        arr[i] = val.zfill(maxlen)
    for i in range(maxlen-1 , -1 , -1):
        arr =  countingSort.sort(arr , lambda x: int(x[i]))
    return [int(i) for i in arr]
    

