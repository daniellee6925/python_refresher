"""
HashTables - 'Dictionary'
search element by key O(1)
great time complexity, not great space complexity
"""


class HashTable:
    def __init__(self) -> None:
        self.Max = 100
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)  # returns int representing the unicode Code
        return h % self.Max

    def __setitem__(self, key, value):  # <-- dunder methods
        h = self.get_hash(key)
        found = False
        # stores a linked list
        for idx, element in enumerate(self.arr[h]):  # idx = key, element = value
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self, key):
        h = self.get_hash(key)
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
        self.arr[h] = None


"""
collision happens when key is already used.
One solution is storing a linked list for the value
One solution is linear probing
-> finds the next available space that is empty O(n)
"""

if __name__ == "__main__":
    t = HashTable()
    t["march 6"] = 120
    t["march 6"] = 100
    t["march 8"] = 59
    t["march 9"] = 23
    t["march 17"] = 75
    del t["march 17"]
    print(t.arr)
