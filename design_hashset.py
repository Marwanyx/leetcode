class MyHashSet:

    def __init__(self):
        self._items = defaultdict(list)

    def add(self, key: int) -> None:
        if key not in self._items:
            self._items.append(key)        

    def remove(self, key: int) -> None:
        if key in self._items:
            self._items.remove(key)

    def contains(self, key: int) -> bool:
        return key in self._items
        

s = MyHashSet()
s.add(1)
s.add(2)
print(s.contains(1)) # True
print(s.contains(3)) # False
s.add(2)
print(s.contains(2)) # True
s.remove(2)
print(s.contains(2)) # False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)