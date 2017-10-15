class Node:
    def __init__(self,val):
        self.val = val
        self.parent = None
        self.discovered = 0
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

def DFS(v,time,graph):
    v.visited = 1
    time = time + 1
    v.discovered = time
    for u in graph[v]:
        if u.visited == 0:
            u.parent = v
            DFS(u,time,graph)
        v.visited = 1
        time = time + 1
        v.completionTime = time

def printDFSbyTime(source,graph):
    while source.parent != None:
        print source.val,str(source.discovered),str(source.completionTime)
        source = source.parent

time = 0
DFS(A,time,graph)
printDFSbyTime(C, graph)


