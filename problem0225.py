class MyStack(object):

    def __init__(self):
        self.lifo = []

    def push(self, x):
        self.lifo.append(x)

    def pop(self):
        return self.lifo.pop(-1)
        
    def top(self):
        return self.lifo[-1]

    def empty(self):
        return len(self.lifo) == 0
