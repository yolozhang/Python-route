#-*-coding=utf-8-*-
class Node(object):
    def __init__(self, elem=-1,lchild=None, rchild=None):
        self.elem=elem
        self.lchild=lchild
        self.rchild=rchild

class Tree(object):
    def __init__(self):
        self.root=Node()
        self.nodequeue=[]
    def addnode(self, elem):
        node =Node(elem)
        if self.root.elem == -1:
            self.root=node
            self.nodequeue.append(self.root)
        else:
            treeNode = self.nodequeue[0]
            if treeNode.lchild == None:
                treeNode.lchild=node
                self.nodequeue.append(treeNode.lchild)
            else:
                treeNode.rchild=node
                self.nodequeue.append(treeNode.rchild)
                self.nodequeue.pop(0)
#    def traversal(self):
 #       return

class traversal(object):
    def preorder(self,root):
        if root==None:
            return
        print(root.elem,end=' ')
        self.preorder(root.lchild)
        self.preorder(root.rchild)
    def postorder(self,root):
        if root==None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem,end=' ')
    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.lchild)
        print(root.elem,end=' ')
        self.inorder(root.rchild)
    def level(self,root):
        if root==None:
            return
        nodequeue=[]
        node=root
        nodequeue.append(node)
        while nodequeue:
            node=nodequeue.pop(0)
            print(node.elem,end=' ')
            if node.lchild !=None:
                nodequeue.append(node.lchild)
            if node.rchild !=None:
                nodequeue.append(node.rchild)
    def prestack(self,root):
        if root == None:
            return
        nodeStack=[]
        node=root
        while node or nodeStack:
            while node:
                print(node.elem,end=' ')
                nodeStack.append(node)
                node=node.lchild
            node=nodeStack.pop()
            node=node.rchild
    def poststack(self,root):
        if root == None:
            return
        nodeStack1 = []
        nodeStack2=  []
        node = root
        nodeStack1.append(node)
        while nodeStack1:
            node=nodeStack1.pop()
            if node.lchild:
                nodeStack1.append(node.lchild)
            if node.rchild:
                nodeStack1.append(node.rchild)
            nodeStack2.append(node)
        while nodeStack2:
            print(nodeStack2.pop().elem,end=' ')

    def instack(self,root):
        if root==None:
            return
        nodeStack=[]
        node=root
        while node or nodeStack:
            while node:
                nodeStack.append(node)
                node=node.lchild
            node = nodeStack.pop()
            print(node.elem,end=' ')
            node=node.rchild

#tree's diameter equal to the sum of left and right's depth  1-2-3-4-5 => 4-2-1-3 ,d=3
class Diameter(object):
    def getDepth(self, root):
        if not root:
            return 0
        l=self.getDepth(root.lchild)
        r=self.getDepth(root.rchild)
        self.d=max(self.d,l+r) #???
        return max(l,r)+1
    def diaofTree(self,root):
        self.d=0
        self.getDepth(root)
        return self.d


if __name__=='__main__':
    elems=range(10)
    tree=Tree()
    trave=traversal()
    dia=Diameter()
    for elem in elems:
        tree.addnode(elem)

    print('level:')
    trave.level(tree.root)
    print()
    print('preorder:')
    trave.preorder(tree.root)
    print()
    print('postorder:')
    trave.postorder(tree.root)
    print()
    print('poststack')
    trave.poststack(tree.root)
    print()
    print(dia.diaofTree(tree.root))
