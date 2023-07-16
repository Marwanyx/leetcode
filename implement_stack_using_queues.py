class Queue:
    def __init__(self):
        self._items = []
    
    def enqueue(self, x: int):
        self._items.append(x)

    def dequeue(self) -> int:
        return self._items.pop(0)
    
    def empty(self) -> bool:
        return len(self._items) == 0

class MyStack:

    def __init__(self):
        self._items = Queue()

    def push(self, x: int) -> None:
        temp = Queue()
        temp.enqueue(x)

        while not self._items.empty():
            temp.enqueue(self._items.dequeue())

        while not temp.empty():
            self._items.enqueue(temp.dequeue())

    def pop(self) -> int:
        return self._items.dequeue()

    def top(self) -> int:
        item = self._items.dequeue()
        temp = Queue()

        while not self._items.empty():
            temp.enqueue(self._items.dequeue())

        self._items.enqueue(item)
        while not temp.empty():
            self._items.enqueue(temp.dequeue())

        return item

    def empty(self) -> bool:
        return self._items.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

s = MyStack()
s.push(1)
s.push(2)
print(s.top()) # 2
print(s.pop()) # 2
print(s.empty()) # False

