'''
implement BST methods
'''

class Node:

    def __init__(self):
        self.data = data
        self.leftChild = None
        self.rightChild = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    def insertNode(self, data, node):

        if data < node.data:
            if node.leftChild:
                self.insertNode(self, data, node)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(self, data, node)
            else:
                node.rightChild = Node(data)



    def getMinVal(self):

        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):

        if node.leftChild:
            return self.getMin(node.leftChild)

        return node.data

    def getMaxVal(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self, node):
        if node.rightChild:
            return self.getMax(node.rightChild)

        return node.data

    def traverse(self):
        if self.root:
            return self.traverseInOrder(self.root)

    def traverseInOrder(self, node):
        if node.leftChild:
            self.traverseInOrder(node.leftChild)

        print(node.data + '\n')

        if node.rightChild:
            self.traverseInOrder(node.rightChild)

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    def removeNode(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.leftChild = self.removeNode(data, node.leftChild)

        elif data > node.data:
            node.rightChild = self.removeNode(data, node.rightChild)

        else:
            if not node.leftChild and node.rightChild:
                print("removing leaf node ...")
                del node
                return None

            if not self.leftChild:
                print("removing node with a single right child")
                tempNode = node.rightChild
                del node
                return tempNode
            elif not self.rightChild:
                print('removing node with a single left child')
                tempNode = node.leftChild
                del node
                return tempNode

            print("removing Node with two Children")
            tempNode = self.getPredecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.removeNode(tempNode.data, node.leftChild)


    def getPredecessor(self, node):
        if node.rightChild:
            return self.getPredecessor(node.rightChild)

        return node








