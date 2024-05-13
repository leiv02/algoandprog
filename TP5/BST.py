class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def addElement(node, value):
    if node is None:
        return Node(value)
    elif value < node.value:
        node.left = addElement(node.left, value)
    else:
        node.right = addElement(node.right, value)
    return node

def createTree(values):
    root = None
    for value in values:
        root = addElement(root, value)
    return root

def findValue(node, value):
    if node is None:
        return False
    elif value == node.value:
        return True
    elif value < node.value:
        return findValue(node.left, value)
    else:
        return findValue(node.right, value)

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, key):
    if root is None:
        return root
    if key < root.value:
        root.left = deleteNode(root.left, key)
    elif key > root.value:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = minValueNode(root.right)
        root.value = temp.value
        root.right = deleteNode(root.right, temp.value)
    return root

def inorderTraversal(root):
    if root:
        inorderTraversal(root.left)
        print(root.value)
        inorderTraversal(root.right)

def preorderTraversal(root):
    if root:
        print(root.value)
        preorderTraversal(root.left)
        preorderTraversal(root.right)

def postorderTraversal(root):
    if root:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.value)

# Example 
values = [5, 3, 7, 1, 4, 8, 6]
root = createTree(values)
print("Initial tree (Inorder Traversal):")
inorderTraversal(root)

print("Initial tree (Preorder Traversal):")
preorderTraversal(root)

print("Initial tree (Postorder Traversal):")
postorderTraversal(root)

print("Searching for 4 in the tree:")
print(findValue(root, 4))  

print("Searching for 10 in the tree:")
print(findValue(root, 10))  

root = deleteNode(root, 8)
print("Tree after deleting node 8 (Inorder Traversal):")
inorderTraversal(root)

root = deleteNode(root, 3)
print("Tree after deleting node 3 (Inorder Traversal):")
inorderTraversal(root)
