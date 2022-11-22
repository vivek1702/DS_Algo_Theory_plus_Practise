class BinarTreeImplementation:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def printTree_Detailed(root):
    if root is None:
        return

    print("   ",root.data)

    if root.left is not None:
        print("/",root.left.data)

    if root.right is not None:
        print("       |", root.right.data)

    printTree_Detailed(root.left)
    printTree_Detailed(root.right)

def LargestElement(root):
    if root is None:
        return -1
    leftlargest = LargestElement(root.left)
    righlargest = LargestElement(root.right)
    largest = max(leftlargest, righlargest, root.data)
    return largest
    

def treeInput():
    rootdata = int(input())
    if rootdata == -1:
        return None
    root = BinarTreeImplementation(rootdata)
    lefttree = treeInput()
    righttree = treeInput()
    root.left = lefttree
    root.right = righttree

    return root

root = treeInput()
printTree_Detailed(root)
LargestElement(root)