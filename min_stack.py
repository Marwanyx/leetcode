class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        self.items.append(val)

    def pop(self) -> None:
        self.items.pop()
        
    def top(self) -> int:
        item = self.items.pop()
        self.items.append(item)
        return item
        
    def getMin(self) -> int:
        return min(self.items)