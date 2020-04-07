from Graphs import Graph

class Kruskal:
    def __init__(self , graph):
        self.graph = graph
        self.edges = list(graph.edgeArray)
        self.edges.sort(key=lambda x: x[2])
        self.link = {}
        self.size = {}
        for i in graph:
            self.link[i] = i

        for i in graph:
            self.size[i] = 1
    
    def find(self,a):
        while a!=self.link[a]:
            a = self.link[a]
        return a

    def same(self,a,b):
        return self.find(a) == self.find(b)

    def unite(self,a,b):
        a = self.find(a)
        b = self.find(b)
        if self.size[a] < self.size[b]:
            a,b=b,a
        self.size[a]+=self.size[b]
        self.link[b] = a


    def minSpanning(self):
        for i in self.edges:
            if not self.same(i[0] , i[1]):
                self.unite(i[0] , i[1])
