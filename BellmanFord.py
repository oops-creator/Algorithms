from Graphs import Graph , Vertex

def bellmanFord(aGraph, start):
    start.distance = 0
    for _ in aGraph:
        for edge in aGraph.getEdges():
            newDist = edge[0].distance + aGraph.edgeList[edge]
            if newDist < edge[1].distance:
                edge[1].distance = newDist
                edge[1].pred = edge[0]

    for edge in aGraph.getEdges():
        assert edge[0].distance + aGraph.edgeList[edge] >= edge[1].distance

    

