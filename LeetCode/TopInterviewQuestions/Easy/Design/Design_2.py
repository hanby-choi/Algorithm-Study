# Min Stack
class MinStack(object):

    def __init__(self):
        self.stack = []
        
    def push(self, val):
        if self.stack:
            min_val = self.getMin()
            if val < min_val:
                self.stack.append((val, val))
            else:
                self.stack.append((val, min_val))
        else:
            self.stack.append((val, val))
        

    def pop(self):
        self.stack.pop()
        

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        else:
            return None
        

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        else:
            return None