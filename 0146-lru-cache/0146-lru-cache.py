class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        # Map with key pointing to node of list
        self.cache = {}

        # Left -> LRU node
        self.left = Node(0, 0)

        # Right -> MRU node
        self.right = Node(0, 0)

        #Initially, list only has left and right nodes
        self.left.next = self.right
        self.right.prev = self.left

    #Remove any given node from list
    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    #Insert given node from right of list
    def insert(self, node):
        prev = self.right.prev
        next = self.right

        node.next = next
        node.prev = prev

        prev.next = node
        next.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1


    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, val)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)