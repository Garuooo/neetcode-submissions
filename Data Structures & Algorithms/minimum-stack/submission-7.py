class MinStack:
    def __init__(self):
        self.stack=[]
        self.minimum = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) == 1 or val < self.minimum:
            self.minimum=val

    def pop(self) -> None:
        if self.stack:
            last_element = self.stack.pop()
            if self.minimum == last_element:
                if self.stack:
                    self.minimum = min(self.stack)
                else:
                    self.minimum = None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]        

    def getMin(self) -> int:
        return self.minimum
