from tkinter import *
from tkinter import ttk
from Graphs import Graph
import random


class PlotGraph:
    
    def plot(self,graph):
        self.root = Tk()
        self.root.columnconfigure(0, weight=1, minsize=75)
        self.root.rowconfigure(0, weight=1, minsize=50)
        self.canvas = Canvas(self.root)
        self.canvas.grid(column=0, row=0, sticky=(N, W, E, S) )
        self.nodeRadius = 24


        self.samplesX = random.sample(range(1,400, 2*self.nodeRadius), len(graph.vertList))
        self.samplesY = random.sample(range(1,400, 2*self.nodeRadius), len(graph.vertList))
        self.vertices = zip(self.samplesX,self.samplesY,graph.vertList)
        self.nodeCord = {}

        for x,y,vert in self.vertices:
            self.nodeCord[vert] = (x+self.nodeRadius, y+self.nodeRadius)
            self.canvas.create_oval(x,y,x+2*self.nodeRadius, y+2*self.nodeRadius , fill='red')
            self.canvas.create_text(x+self.nodeRadius, y+self.nodeRadius , text=vert)

        for a,b,w in graph.edgeArray:
            self.canvas.create_line(self.nodeCord[a.getId()] , self.nodeCord[b.getId()])
        


        self.root.mainloop()
