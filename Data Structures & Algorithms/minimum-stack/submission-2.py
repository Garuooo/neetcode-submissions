class MinStack:
    def __init__(self):
        self.stack=[]

    def push(self,val):
        self.stack.append(val)
        return None
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None
    
    def top(self):
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self):
        return min(self.stack)