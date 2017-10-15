class Vertex:
    def __init__(self, val):
        # type: (object) -> object
        self.val = val
        self.parent = None
        self.distance = 0
        self.visited = False


a = Vertex("a")
b = Vertex("b")
c = Vertex("c")
d = Vertex("d")
e = Vertex("e")

adj_list = {a: [c],
            b: [c, e],
            c: [a, b, d, e],
            d: [c],
            e: [c, b],
            }


def breadthFirstSearch(source):
    """

    :type source: object
    """
    source.distance = 0
    source.visited = True

    queue = [source]

    while len(queue) > 0:
        u = queue.pop(0)
        for v in adj_list[u]:
            if not v.visited:
                v.parent = u
                v.distance = v.distance + 1
                v.visited = True
                queue.append(v)


def printPath(node):
    path = [node.val]
    while node.parent != None:
        path.append(node.parent.val)
        node = node.parent
    print "->".join(path[::-1])

breadthFirstSearch(a)
printPath(b)
