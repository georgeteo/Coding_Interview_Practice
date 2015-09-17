'''
My implementation of Binary Trees in Python
'''

class binary_tree(object):
    def __init__(self, id, depth, left_child=None, right_child=None):
        self.__id = id
        self.__left_child = left_child
        self.__right_child = right_child
        self.__depth = depth

    @property
    def id(self):
        return self.__id

    @property
    def left_child(self):
        return self.__left_child

    @left_child.setter
    def left_child(self, left_child_data):
        self.__left_child = left_child_data

    @property
    def right_child(self):
        return self.__right_child

    @right_child.setter
    def right_child(self, right_child_data):
        self.__right_child = right_child_data

    @property
    def depth(self):
        return self.__depth

    @depth.setter
    def depth(self, depth):
        self.__depth = depth

    def add_children(self, right_child, left_child):
        self.__left_child = binary_tree(left_child, self.depth + 1)
        self.__right_child = binary_tree(right_child, self.depth + 1)

    def insert(self, data):
        bt = binary_tree(data, self.depth + 1)
        self.__left_child.push()
        bt.left_child = self.__left_child
        self.__right_child.push()
        bt.right_child = self.__right_child
        self.__left_child = bt
        self.__right_child = None

    def push(self):
        self.pre_order_traversal(increment)

    def pre_order_traversal(self, callback):
        if self.__left_child is not None:
            self.__left_child.pre_order_traversal(callback)
        self.__id, self.__depth = callback(self.__id, self.__depth)
        if self.__right_child is not None:
            self.__right_child.pre_order_traversal(callback)

    def in_order_traversal(self, callback):
        self.__id, self.__depth = callback(self.__id, self.__depth)
        if self.__left_child is not None:
            self.__left_child.in_order_traversal(callback)
        if self.__right_child is not None:
            self.__right_child.in_order_traversal(callback)

    def post_order_traversal(self, callback):
        if self.__right_child is not None:
            self.__right_child.post_order_traversal(callback)
        self.__id, self.__depth = callback(self.__id, self.__depth)
        if self.__left_child is not None:
            self.__left_child.post_order_traversal(callback)

def print_node(val, count):
    buf = "  " * count
    print buf + str(val)
    return val, count

def increment(val, count):
    count +=1
    return val, count

if __name__ == "__main__":
    bt = binary_tree(0, 0, binary_tree(1, 1), binary_tree(2, 1))
    bt.left_child.add_children(3,4)
    bt.right_child.add_children(5,6)
    print "Pre Order Traversal:"
    bt.pre_order_traversal(print_node)
    print ""

    print "In Order Traversal"
    bt.in_order_traversal(print_node)
    print ""

    print "Post Order Traversal"
    bt.post_order_traversal(print_node)
    print ""
