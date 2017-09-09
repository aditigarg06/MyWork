class Node:
    def __init__(self ,key):
        self.data = key
        self.state = None

def buildOrder(projects):
    stack = []
    for project in projects:
        if project.state == None:
            if not dfs_visit(project,stack):
                return None
    return stack


def dfs_visit(project,stack):
    if project.state == "partial":
        return False

    if project.state == None:
        project.state = "partial"
        #print (project.data)
        for adjNodes in graph[project]:
            dfs_visit(adjNodes,stack)
        project.state = "complete"
        stack.append(project)

    return True

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')

graph = { A: [F],
         B: [F],
         C: [D],
         D: [A,B],
         E: [],
         F : []
        }

projects =[A,B,C,D,E,F]
order = buildOrder(projects)
for project in order:
    print(project.data)