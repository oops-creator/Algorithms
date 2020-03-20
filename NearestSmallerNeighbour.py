arr = [int(i) for i in input("Enter the array ").split()]
stack = []
stack.append(arr[0])

for i in arr[1:]:
    if stack[-1] > i:
        while stack[-1]<i:
            stack.pop()

    print(stack[-1] , "is smallest nearest neighbour of " , i)
    stack.append(i)

    