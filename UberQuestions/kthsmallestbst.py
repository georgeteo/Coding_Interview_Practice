class bstnode(object):
    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

    def insert(self, data):
        if data <= self.data:
            if not self.left:
                self.left = bstnode(data, self)
            else:
                self.left.insert(data)
        else:
            if not self.right:
                self.right = bstnode(data, self)
            else:
                self.right.insert(data)

    def find_min(self):
        if not self.left and not self.right:
            return self
        if self.left:
            return self.left.find_min()
        else:
            return self.right.find_min()

    def find(self, data):
        if self.data == data:
            return self
        if not self.left and not self.right:
            return None
        left_return = self.left.find(data)
        if left_return != None:
            return left_return
        right_return = self.right.find(data)
        if right_return != None:
            return right_return
        return None

    def delete(self):
        # if leaf node
        print "Begin delete for: ", self.data
        if (not self.left) and (not self.right):
            print "   No children"
            if self.parent.left == self:
                print "         Left"
                self.parent.left = None
            elif self.parent.right == self:
                print "         Right"
                self.parent.right = None
            else:
                return None
        # If only one child
        if ((self.left) or (self.right)) and (not (self.left and self.right)):
            print "    One child"
            if self.left:
                child = self.left
            else:
                child = self.right
            if self.parent.left == self:
                self.parent.left = child
            elif self.parent.right == self:
                self.parent.right = child
            else:
                return child
        # If two children, replace this node with inorder successor
        if self.left and self.right:
            print "    Two children"
            self.data = self.right.find_min().data
            self.right.find_min().delete()

def inordertraversal(root):
    if (not root.left) and (not root.right):
        yield root
    else:
        if (root.left):
            for result in inordertraversal(root.left):
                yield result
        yield root
        if (root.right):
            for result in inordertraversal(root.right):
                yield result

if __name__=="__main__":
    bstroot = bstnode(3, None)
    bstroot.insert(1)
    bstroot.insert(5)
    bstroot.insert(2)
    bstroot.insert(0)
    bstroot.insert(4)
    bstroot.insert(6)

    print "Before:"
    for i in inordertraversal(bstroot):
        print i.data

    bstroot.find(1).delete()

    print "After:"
    for i in inordertraversal(bstroot):
        print i.data
