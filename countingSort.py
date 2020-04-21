

def sort(array , func=lambda x: x):
    funcarr = list(map(func , array))
    maxnum = int(max(funcarr))
    store = [0]*(maxnum+1)
    retval = [0]*(len(array)+1)
    for i , val in enumerate(funcarr):
        store[val]+=1

    for i in range(1,len(store)):
        store[i] = store[i]+store[i-1]

    for i in range(len(array) -1 , -1 , -1):
        retval[store[funcarr[i]]] = array[i]
        store[funcarr[i]]-=1

    return retval[1:]


if __name__ == "__main__":
    arr = [int(i) for i in input().split()]
    print(sort(arr))
   


