class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}

    def get(self, key: int) -> int:
        # {thing: (item, age)}
        if key in self.hashMap:
            val = self.hashMap[key][1]
            self.hashMap[key] = (self.hashMap[key][0], val + 1)
            return self.hashMap[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.hashMap) == self.capacity:
            # do in O(1)

            # find the oldest item
            oldest = None
            for k, v in self.hashMap.items():
                if oldest is None:
                    oldest = k
                elif v[1] < self.hashMap[oldest][1]:
                    oldest = k

            # remove the oldest item
            del self.hashMap[oldest]
        else:
            if key in self.hashMap:
                self.hashMap[key][0] = value
            elif key not in self.hashMap:
                self.hashMap[key] = (value, 0)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

s = LRUCache(2)
s.put(1, 1)
s.put(2, 2)
print(s.get(1))
s.put(3, 3)
print(s.get(2))
s.put(4, 4)
print(s.get(1))
print(s.get(3))
print(s.get(4))