arr = [int(i) for i in input("Enter the array ").split()]

prefixSumArr = []
prefixSumArr.append(arr[0]) 

for i,_ in enumerate(arr[1:]):
    prefixSumArr.append(prefixSumArr[i]+arr[i+1])

def sumQuery(a,b):
    return prefixSumArr[b]-(prefixSumArr[a-1] if a>0 else 0)

while True:
    a = int(input("Enter the start index of range query "))
    b = int(input("Enter the end index of range query "))
    print(sumQuery(a,b))
