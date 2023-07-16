class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, x: int):
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()
    
    def empty(self) -> bool:
        return len(self.stack) == 0

class MyQueue:

    def __init__(self):
        self.items = Stack()

    def push(self, x: int) -> None:
        self.items.push(x)

    def pop(self) -> int:
        temp = Stack()

        while not self.items.empty():
            temp.push(self.items.pop())

        item = temp.pop()

        while not temp.empty():
            self.items.push(temp.pop())

        return item
        

    def peek(self) -> int:
        temp = Stack()

        while not self.items.empty():
            temp.push(self.items.pop())

        item = temp.pop()
        temp.push(item)

        while not temp.empty():
            self.items.push(temp.pop())

        return item
        

    def empty(self) -> bool:
        return self.items.empty()
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()