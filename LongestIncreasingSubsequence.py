#Find longest subsequence of in length l 

arr = [int(i) for i in input("Enter the space seperated numbers ").split()]
longestSub = {}

def length(num):
    for i in range(num+1):
        longestSub[i] = 1
        for j in range(i):
            if arr[j] < arr[i]:
                longestSub[i] = max(longestSub[i] , longestSub[j] +1)

    return longestSub[num]

while True:
    l = int(input("Enter the max position for increasing subsequence "))
    l = l if l < len(arr) else len(arr) - 1
    print(length(l))