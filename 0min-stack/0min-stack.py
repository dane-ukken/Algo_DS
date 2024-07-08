class MinStack:

    def __init__(self):
        self.minVal = float(inf)
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        newMin = min(self.minVal, val)
        self.minStack.append(newMin)
        self.stack.append(val)
        self.minVal = newMin

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        if not self.minStack:
            self.minVal = float(inf)
        else:
            self.minVal = self.minStack[-1]
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()