first =  input("Enter first string ")
second =  input("Enter second string ")

def cost(a,b):
    return 0 if a==b else 1

def distance(a,b):
    if len(a) == 1 and len(b)==1:
        return cost(a,b)
    if len(a) == 1 or len(b) == 1:
        return cost(a[0],b[0])

    return min(distance(a,b[:-1])+1 , distance(a[:-1],b)+1 , distance(a[:-1],b[:-1]) + cost(a[-1],b[-1]))


print("Edit distance is " ,distance(first,second))