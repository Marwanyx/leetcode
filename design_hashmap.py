class MyHashMap:

    def __init__(self):
        self._items = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self._items)):
            if self._items[i][0] == key:
                self._items.pop(i)
                self._items.append((key, value))
                return
            
        self._items.append((key, value))

    def get(self, key: int) -> int:
        for i in range(len(self._items)):
            if self._items[i][0] == key:
                return self._items[i][1]
        
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self._items)):
            if self._items[i][0] == key:
                self._items.pop(i)
                return
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

m = MyHashMap()
m.put(1, 1)
m.put(2, 2)
print(m.get(1)) # 1
print(m.get(3)) # -1
m.put(2, 1)
print(m.get(2)) # 1
m.remove(2)
print(m.get(2)) # -1