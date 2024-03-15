class MinStack:

    def __init__(self):
        self.st = []
        self.minSt = [inf]

    def push(self, val: int) -> None:
        self.minSt.append(min(self.minSt[len(self.minSt)-1], val))
        self.st.append(val)
        
    def pop(self) -> None:
        self.st.pop()
        self.minSt.pop()

    def top(self) -> int:
        return self.st[len(self.st)-1]

    def getMin(self) -> int:
        return self.minSt[len(self.minSt)-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()