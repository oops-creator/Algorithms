from Graphs import Graph 
from BellmanFord import bellmanFord

g = Graph()
g.addEdge(1,2 , -1)
g.addEdge(2,3 , 1)
g.addEdge(2,4 , 1)
g.addEdge(4,1,-1)

bellmanFord(g,g.getVertex(1))
for i in g:
    print(str(i), "has distance from 1" , i.distance)