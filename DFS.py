from Graphs import Graph
from Graphs import Vertex

graph = Graph()

for i in range(6):
    graph.addVertex(i)

graph.addEdge(0,1,5)
graph.addEdge(0,5,2)
graph.addEdge(1,2,4)
graph.addEdge(2,3,9)
graph.addEdge(3,4,7)
graph.addEdge(3,5,3)
graph.addEdge(4,0,1)
graph.addEdge(5,4,8)
graph.addEdge(5,2,1)

visited = {}
def DFS(node):
    if node in visited.keys() and visited[node] == True:
        return
    visited[node] = True
    print(node)
    for i in graph.getVertex(node).getConnections():
        DFS(i.getId())


DFS(0)



