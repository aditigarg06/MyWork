class Node:
    def __init__(self,val):
        self.val = val
        self.parent = None
        self.completionTime = 0
        self.visited = 0

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')

graph = { A: [B, C],
         B: [A, D, E],
         C: [A, F],
         D: [B],
         E: [B, F],
         F: [C, E]}

def TopologicalSort(graph):
    for vertex in graph.keys():
        if vertex.visited == 0:
            DFS(vertex,graph)


def DFS(v,graph):
    global currentLabel
    v.visited = 1
    for u in graph[v]:
        if u.visited == 0:
            u.parent = v
            DFS(u,graph)
    v.completionTime = currentLabel
    currentLabel = currentLabel - 1

def printDFSbyTime(graph):
    for v in graph.keys():
        print v.val,str(v.completionTime)


currentLabel = len(graph.keys())
TopologicalSort(graph)
printDFSbyTime(graph)