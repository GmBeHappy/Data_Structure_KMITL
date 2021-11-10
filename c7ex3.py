class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
        else:
            CNode = self.root
            while True:
                if data > CNode.data:
                    if CNode.right is None:
                        CNode.right = newNode
                        break
                    CNode = CNode.right

                elif data < CNode.data:
                    if CNode.left is None:
                        CNode.left = newNode
                        break
                    CNode = CNode.left

        return self.root

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left)
            print(str(cur_node.data))
            self._print_tree(cur_node.right)

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def countLeq(node, num):
    if node == None:
        return 0
    if node.data <= num:
        return 1 + countLeq(node.left, num) + countLeq(node.right, num)
    else:
        return countLeq(node.left, num) + countLeq(node.right, num)

tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.insert(int(e))
printTree90(tree.root)
print("--------------------------------------------------")
print(countLeq(tree.root,int(data[1])))