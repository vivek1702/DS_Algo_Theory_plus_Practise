#first time changing the structure of a tree

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

def removeLeaf(root):
    if root is None:
        return
    if root.left == None and root.right == None:
        return
    
    root.left = removeLeaf(root.left)
    root.right = removeLeaf(root.right)
    return root


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