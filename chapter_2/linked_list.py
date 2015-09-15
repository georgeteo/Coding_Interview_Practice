class single_node(object):
    '''
    Node for singly linked list.
    Consists of data and pointer to next Node
    '''
    def __init__(self, data=None):
        self.data = data
        self.next = None

class singly_linked_list(object):
    '''
    Data structure for singly linked list
    '''
    def __init__(self, head=None):
        self.head = head
        self.length = 1 if head else 0 # Allows for O(1) size

    def add(self, data):
        '''
        Adding to the head of the list and pushing list down
        '''
        new_node = single_node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insert(self, data, after=None):
        '''
        Insert node after: index, or data
        '''
        new_node = single_note(data)
        if type(after) == int:
            __insert_by_index(new_node, after)
        else:
            __insert_by_data(new_node, after)

    def __insert_by_index(self, new_node, after):
        '''
        Private method to insert node by after specific index
        '''
        if after > self.length:
            raise ValueError("Can't insert at index greater than length of the list.")
        insertion_node = self.head
        for i in xrange(after):
            insertion_node = insertion_node.next
        next_node = insertion_node.next
        insertion_node.next = new_node
        new_node.next = next_node

    def __insert_by_data(self, new_node, data, n=1):
        '''
        Private helper method to insert node after nth occurance of specific data
        '''
        insertion_node = self.head
        while n > 1 or insertion_node.data != data:
            if insertion_node.data == data:
                n -= 1
            insertion_node = insertion_node.next
        if insertion_node is None:
            raise ValueError("Data occurs less than n times.")
        next_node = insertion_node.next
        insertion_node.next = new_node
        new_node.next = next_node

    def search(self, data, n=1):
        '''
        Searches linked list for nth occurance of data
        Worst and Average case: O(n)
        Best case: O(1)
        '''
        node = self.head
        while n > 1 or node.data != data:
            if node.data == data:
                n -= 1
            node = node.next
        if node is None:
            raise ValueError("Data occurs less than n times.")
        return node

    def delete(self, data, n=1):
        '''
        Deletes first n occurances of data
        '''
        node = self.head
        while n > 0:
            if node.data == data:
                '''
                If copy next node to this node,
                garbage collect next node
                '''
                node.data = node.next.data
                node.next = node.next.next
                n -= 1
            if node is None:
                raise ValueError("Data occurs less than n times.")

    def __str__(self):
        node = self.head
        string = ""
        while node:
            string = string + str(node.data) + " -> "
            node = node.next
        return string
