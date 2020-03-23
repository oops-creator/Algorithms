class MinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def heapifyUp(self,i):
        while i//2:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i//2] , self.heapList[i] = self.heapList[i] , self.heapList[i//2]
            i //=2

    def insert(self, i):
        self.heapList.append(i)
        self.currentSize +=1
        self.heapifyUp(self.currentSize)


    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def heapifyDown(self,i):
        while i*2<=self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[mc],self.heapList[i] = self.heapList[i] ,self.heapList[mc]
            i = mc


    def delMin(self):
        minVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -=1
        self.heapList.pop()
        self.heapifyDown(1)
        return minVal

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.heapifyDown(i)
            i = i -1



class MaxHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def heapifyUp(self,i):
        while i//2:
            if self.heapList[i] > self.heapList[i//2]:
                self.heapList[i//2] , self.heapList[i] = self.heapList[i] , self.heapList[i//2]
            i //=2

    def insert(self, i):
        self.heapList.append(i)
        self.currentSize +=1
        self.heapifyUp(self.currentSize)


    def maxChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] > self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def heapifyDown(self,i):
        while i*2<=self.currentSize:
            mc = self.maxChild(i)
            if self.heapList[i] < self.heapList[mc]:
                self.heapList[mc],self.heapList[i] = self.heapList[i] ,self.heapList[mc]
            i = mc


    def delMax(self):
        maxVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -=1
        self.heapList.pop()
        self.heapifyDown(1)
        return maxVal

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.heapifyDown(i)
            i = i -1





class PriorityQueue:
    def __init__(self):
        self.heapList = [(0,0)]
        self.currentSize = 0

    def heapifyUp(self,i):
        while i//2:
            if self.heapList[i][1] < self.heapList[i//2][1]:
                self.heapList[i//2] , self.heapList[i] = self.heapList[i] , self.heapList[i//2]
            i //=2

    def insert(self, i):
        self.heapList.append(i)
        self.currentSize +=1
        self.heapifyUp(self.currentSize)


    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2][1] < self.heapList[i*2+1][1]:
                return i * 2
            else:
                return i * 2 + 1

    def heapifyDown(self,i):
        while i*2<=self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i][1]> self.heapList[mc][1]:
                self.heapList[mc],self.heapList[i] = self.heapList[i] ,self.heapList[mc]
            i = mc


    def delMin(self):
        minVal = self.heapList[1][0]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -=1
        self.heapList.pop()
        self.heapifyDown(1)
        return minVal

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [(0,0)] + alist[:]
        while (i > 0):
            self.heapifyDown(i)
            i = i -1

    def decreaseKey(self,vert , val):
        for i in range(len(self.heapList)):
            if self.heapList[i][0] == vert.getId():
                self.heapList[i][1] = val
                self.heapifyDown(1)
                return


