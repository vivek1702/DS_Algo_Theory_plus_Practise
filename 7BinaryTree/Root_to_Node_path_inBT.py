import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    
def printBinarytree(root):
    if root == None:
        return

    print(root.data,end=":")
    if root.left != None:
        print("L",root.left.data, end=",")

    if root.right != None:
        print("R",root.right.data, end=",")

    print()

    printBinarytree(root.left)
    printBinarytree(root.right)

def takeLevelwiseInput():
    q = queue.Queue()
    print("enter root")
    rootnode = int(input())
    if rootnode == -1:
        return
    root = BinaryTreeNode(rootnode)
    q.put(root)
    while (not (q.empty())):
        current_node = q.get()

        print("enter left node of", current_node.data)
        leftchildData = int(input())
        if leftchildData != -1:
            leftchild = BinaryTreeNode(leftchildData)
            current_node.left = leftchild
            q.put(leftchild)

        print("enter right node of", current_node.data)
        rightchildData = int(input())
        if rightchildData != -1:
            rightchild = BinaryTreeNode(rightchildData)
            current_node.right = rightchild
            q.put(rightchild)

    return root

def nodeToRootPath(root, s):
    if root == None:
        return

    if root.data == s:
        l = []
        l.append(root.data)
        return l

    leftsubNode = nodeToRootPath(root.left, s)
    if leftsubNode != None:
        leftsubNode.append(root.data)
        return leftsubNode

    rightsubNode = nodeToRootPath(root.right, s)
    if rightsubNode != None:
        rightsubNode.append(root.data)
        return rightsubNode

    else:
        return None
    

root = takeLevelwiseInput()
printBinarytree(root)
print(nodeToRootPath(root, 5))