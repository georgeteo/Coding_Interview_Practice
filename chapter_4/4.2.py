'''
CCC 4.2: Determine if a specific route exists in a directed graph
'''
class Node(object):
    '''
    Credit: Jon Lee
    '''
    def __init__(self, data):
        self.data = data
        self.children = []

    def bfs(self, element):
        q = Queue()
        q.put(self)
        while !q.empty():
            cur = q.get()
            if cur.data == element:
                return cur
            for child in cur.children:
                q.put(child)

        return

    def dfs(self, element):
        if self.data == element:
            return self
        for child in self.children:
            ret = child.dfs(element)
            if ret:
                return ret
        return

    def has_route(self, start, end):
        start_node = self.bfs(start)
        if start_node and start_node.dfs(end):
            return True
        return False
