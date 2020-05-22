class vertex:
    def __init__(self, val):
        self.value = val
        self.adjacent = []


class undirect_graph:
    def __init__(self):
        self.vertices = {}
        self.vertex_number = 0
        self.adj = {}

    def addVertex(self, vt):
        self.vertices[vt.value] = vt
        self.adj[vt.value] = []
        self.vertex_number += 1

    def addEdge(self, v1,v2):   
        self.adj[v1].append(v2)
        self.adj[v2].append(v1)
        self.vertices[v1].adjacent.append(self.vertices[v2])
        self.vertices[v2].adjacent.append(self.vertices[v1])
    
    def printEdges(self):
        print(self.adj)
    
    