class GenricTree:
    def __init__(self, data) -> None:
        self.data = data
        self.children = list()

def printTree(root):
    if root == None: #this is not the base case, this is edge case
        return 

    print(root.data)
    for child in root.children:
        printTree(child)

def printTreeDetailed(root):
    if root == None:
        return

    print(root.data, ":", end='')
    for child in root.children:
        print(child.data,',',end='')
    print()
    for child in root.children:
        printTreeDetailed(child)

def takeTreeInput():
    print("Enter the root ")
    rootData = int(input())
    if rootData == -1:
        return None

    root = GenricTree(rootData)
    print("enter the number for children for ", rootData)
    childrenCount = int(input())
    for i in range(childrenCount):
        child = takeTreeInput()
        root.children.append(child)
    return root

def NumNodes(root):
    count = 1
    if root == None:
        return 0
    for child in root.children:
        count = count + NumNodes(child)
    return count

root = takeTreeInput()
printTreeDetailed(root)
print(NumNodes(root))





