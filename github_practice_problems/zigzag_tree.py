'''
Print zigzag tree: for every other node print left or right most node for a level.

Solution: BFS.
Coplexity: O(n) in number of nodes
'''

from Queue import Queue
def zigzag_print(root):
    q = Queue()
    q.put((root, 0))
    last_node_level = (None, -1)
    while not q.empty():
        nodepair = q.get()
        node = nodepair[0]
        level = nodepair[1]
        last_node_level = last_node[1]
        if last_node_level != level:
            if level%2 == 0:
                if last_node_level != -1:
                    print last_node[0].data
                print node.data
        last_node = nodepair
        if not node.left:
            q.put((node.left, level + 1))
        if not node.right:
            q.put((node.right, level +1))
