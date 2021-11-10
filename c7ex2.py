class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        if self.root == None:
            self.root = newNode
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left == None:
                        current.left = newNode
                        return self.root
                    else:
                        current = current.left
                else:
                    if current.right == None:
                        current.right = newNode
                        return self.root
                    else:
                        current = current.right
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def height(self, node):
        if node == None:
            return -1
        else:
            left = self.height(node.left)
            right = self.height(node.right)
            if left > right:
                return left + 1
            else:
                return right + 1

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
if(T.height(root) != -1):
    print(f"Height of this tree is : {T.height(root)}")
else:
    print("Height of this tree is : 0")