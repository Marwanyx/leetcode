class MinStack:

    def __init__(self):
        self.items = []
        self.min = []

    def push(self, val: int) -> None:
        if not self.items:
            self.min.append(val)
        else:
            self.min.append(min(val, self.min[-1]))

        self.items.append(val)
        

    def pop(self) -> None:
        self.items.pop()
        self.min.pop()
        

    def top(self) -> int:
        return self.items[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Time complexity: O(1)

minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # -3
minStack.pop()
print(minStack.top())  # 0
print(minStack.getMin())  # -2