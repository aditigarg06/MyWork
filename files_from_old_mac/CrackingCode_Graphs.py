def checkHeight(root):
    if root == None:
        return -1
    leftHeight = checkHeight(root.left)
    if leftHeight == -2:
        return -2
    rightHeight = checkHeight(root.right)
    if rightHeight == -2:
        return -2

    heightDiff = leftHeight - rightHeight
    if abs(heightDiff) > 1:
        return -2
    else:
        return max(leftHeight,rightHeight) +1

def isBalanced(root):
    return checkHeight(root) != -2