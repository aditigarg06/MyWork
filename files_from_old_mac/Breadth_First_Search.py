import queue

class Node:
    def __init__(self ,key):
        self.data = key
        self.parent = None
        self.distance = None
        self.visited = 0

def BFS(source):
    source.distance = 0
    source.visited= 1
    Queue = queue.Queue(maxsize= len(graph))
    Queue.put(source)
    while not Queue.empty():
        node = Queue.get()
        for adjacent_node in graph[node]:
            if adjacent_node.visited == 0:
                adjacent_node.visited = 1
                adjacent_node.distance = node.distance + 1
                adjacent_node.parent = node
                Queue.put(adjacent_node)

def Print_Path(source,node):
    if source == node:
        print (source.data)
    elif node.parent == None:
        print ("No path from " + source +" to " + node + "exists.")
    else:
        Print_Path(source,node.parent)
        print (node.data)

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

BFS(A)
Print_Path(A,F)







