class Node:
    def __init__(self ,key):
        self.data = key
        self.parent = None
        self.discovered = None
        self.finished = None
        self.visited = 0
def DFS():
    for vertex in graph:
        if vertex.visited == 0:
            DFS_visit(vertex)

def DFS_visit(vertex):
    global time
    time = time +1
    vertex.discovered = time
    vertex.visited =1
    for node in graph[vertex]:
        if node.visited == 0:
            node.parent = vertex
            DFS_visit(node)
    time = time + 1
    vertex.finished = time
    print (vertex.data)
    print (vertex.discovered)
    print (vertex.finished)

time = 0
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
DFS()