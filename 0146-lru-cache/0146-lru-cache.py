class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        
        #LRU -> Left Node
        self.left = Node(0, 0)

        #MRU -> Right Node
        self.right = Node(0, 0)

        #Initially we have empty linked list
        self.left.next = self.right
        self.right.prev = self.left

    # Remove any given node
    def remove(self, node) -> None:
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    # Insert given node from the right
    def insert(self, node) -> None:
        prev = self.right.prev
        next = self.right

        node.next = next
        node.prev = prev

        prev.next = node
        next.prev = node

    def get(self, key : int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

    def put(self, key : int, val : int) -> None:
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