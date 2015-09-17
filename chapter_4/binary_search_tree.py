'''
My implementation of Binary Search Tree
'''

class binary_search_tree(object):
    def __init__(self, id, depth):
        self.__id = id
        self.__depth = depth
        self.__left_child = None
        self.__right_child = None

    @property
    def id(self):
        return self.__id

    @property
    def depth(self):
        return self.__depth

    @depth.setter
    def depth(self, depth):
        self.__depth = depth

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

    def add(self, new_id):
        if new_id <= self.__id:
            if self.__left_child is None:
                self.__left_child = binary_search_tree(new_id, self.depth + 1)
            else:
                self.__left_child.add(new_id)
        else:
            if self.__right_child is None:
                self.__right_child = binary_search_tree(new_id, self.depth + 1)
            else:
                self.__right_child.add(new_id)

    def pre_order_traversal(self, callback):
        if self.__left_child is not None:
            self.__left_child.pre_order_traversal(callback)
        self.__id, self.__depth = callback(self.__id, self.__depth)
        if self.__right_child is not None:
            self.__right_child.pre_order_traversal(callback)

def print_node(val, count):
    buf = "  " * count
    print buf + str(val)
    return val, count

if __name__ == "__main__":
    bst = binary_search_tree(0, 0)
    bst.add(-1)
    bst.add(-3)
    bst.add(-2)
    bst.add(3)
    bst.add(2)
    bst.add(1)
    bst.pre_order_traversal(print_node)
