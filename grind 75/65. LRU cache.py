""""
dictionary
doubly linked list # todo

LRU cache implementation


O(1) time

METHOD 1: using dict
"""


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru = {}

    def get(self, key: int) -> int:
        a = self.lru.pop(key, None)
        if a == None:
            return -1
        self.lru[key] = a
        return a

    def put(self, key: int, value: int) -> None:
        if self.lru.get(key, None) != None:
            a = self.lru.pop(key)
            self.lru[key] = value
            return        
        if len(self.lru) == self.capacity:
            self.lru.pop(next(iter(self.lru)))
            # a = self.lru.pop(next(iter(self.lru)))
            # print("evicted: ", a)
        self.lru[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
OPTIMAL METHOD USING doubly linked list
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.index = {}
        self.capacity = capacity
        
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _to_front(self, node):
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next.prev = node

    def _touch(self, node):
        self._remove(node)
        self._to_front(node)
        

    def get(self, key: int) -> int:
        if key not in self.index:
            return -1

        node = self.index[key]
        self._touch(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.index:
            node = self.index[key]
            node.val = value
            self._touch(node)
            return

        if len(self.index) == self.capacity:
            evicted = self.tail.prev
            self._remove(evicted)
            del self.index[evicted.key]
        
        node = Node(key, value)
        self.index[key] = node
        self._to_front(node)
"""