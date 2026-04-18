class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            minimum = min(self.min_stack[-1],val)
            self.min_stack.append(minimum)
        else:
            self.min_stack.append(val)
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
