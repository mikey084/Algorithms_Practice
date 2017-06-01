''' 
OOP Impementation of Tree Data Structure
'''

class BinaryTree(object):
    def __init__(self, rootObj):

        self.key = rootObj
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        if self.left == None
            self.left = BinaryTree(newNode)

        else:
            t = BinaryTree(newNode)
            t.left = self.left

    def insertRight(self, newNode):
        pass
