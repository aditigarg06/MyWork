class Node:
    def __init__(self,value):
        self.data = value
        self.p = None
        self.left = None
        self.right = None

#Returns sorted array. Takes O(n) time.
def inOrderTraversal(root):
    if root is not None:
        inOrderTraversal(root.left)
        print (root.data)
        inOrderTraversal(root.right)

#Search for a key. Operation takes O(h) time
def treeSearch(node,key):
    while node is not None and node != key:
        if key < node.key:
            node = node.left
        else:
            node = node.right
    return node

def treeMin(node)
    while node.left is not None:
        node = node.left
    return node

def treeMax(node):
    while node.right is not None:
        node = node.right
    return node

#complexity O(h)
def treeInsert(root,node):
    temp = root
    while temp is not None:
        parent = temp
        if node.data <  temp.data:
            temp = temp.left
        else:
            temp = temp.right
    node.p = parent
    if parent is None:
        root = node
    elif parent.key < node.key:
        parent.left = node
    else:
        parent.right = node



