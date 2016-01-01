class treemap(object):
    def __init__(self, key, value, parent):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
    def get(self, key):
        '''DFS to get key'''
        if self.key == key:
            return self.value
        elif key < self.key:
            if self.left:
                return self.left.get(key)
        else:
            if self.right:
                return self.right.get(key)
        return None
    def set(self, key, value):
        ''' DFS to set key value'''
        if self.key == key:
            self.value = value
        elif key < self.key:
            if self.left:
                self.left.set(key, value)
            else:
                self.left = treemap(key, value, self)
        else:
            if self.right:
                self.right.set(key, value)
            else:
                self.right = treemap(key, value, self)
    def size_computed(self):
        if not self.right and not self.left:
            return 1
        return self.right + self.left + 1
