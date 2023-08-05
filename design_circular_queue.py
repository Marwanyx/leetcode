class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.items = []

    def enQueue(self, value: int) -> bool:
        if len(self.items) == self.size:
            return False
        else:
            self.items.insert(0, value)
            return True

    def deQueue(self) -> bool:
        if self.items == []:
            return False
        else:
            self.items.pop()
            return True
            

    def Front(self) -> int:
        if self.items == []:
            return -1
        else:
            return self.items[-1]

    def Rear(self) -> int:
        if self.items == []:
            return -1
        else:
            return self.items[0]

    def isEmpty(self) -> bool:
        return self.items == []

    def isFull(self) -> bool:
        if len(self.items) == self.size:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

s = MyCircularQueue(3)
print(s.enQueue(1))
print(s.enQueue(2))
print(s.enQueue(3))
print(s.enQueue(4))
print(s.Rear())
print(s.isFull())
print(s.deQueue())
print(s.enQueue(4))
print(s.Rear())
