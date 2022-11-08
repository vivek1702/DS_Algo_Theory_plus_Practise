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


def minval(root):
    if root == None:
        return 100000
    lmin = minval(root.left)
    rmin = minval(root.right)

    return min(lmin, rmin, root.data)

def maxval(root):
    if root == None:
        return -100000
    lmax = maxval(root.left)
    rmax = maxval(root.right)

    return max(lmax, rmax, root.data)

def isBst(root):
    if root == None:
        return True

    leftmax = maxval(root.left)
    rightmin = minval(root.right)

    if root.data <= leftmax and root.data > rightmin:
        return False

    isleftBst = isBst(root.left)
    isrghtBst = isBst(root.right)

    return isleftBst and isrghtBst

    

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

root = takeLevelwiseInput()
printBinarytree(root)