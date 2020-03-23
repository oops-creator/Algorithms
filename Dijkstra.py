from Heap import PriorityQueue
from Graphs import Graph , Vertex

def dijkstra(aGraph, start):
    pq = PriorityQueue()
    start.distance = 0
    pq.buildHeap([(v , v.distance) for v in aGraph])

    while not pq.currentSize == 0:
        currentVert =  pq.delMin()
        print(currentVert)
        for nextVert in currentVert.getConnections():
            newDist = currentVert.distance + currentVert.getWeight(nextVert)
            if newDist < nextVert.distance:
                nextVert.distance = newDist
                nextVert.pred = currentVert
                pq.decreaseKey(nextVert,newDist)

    

