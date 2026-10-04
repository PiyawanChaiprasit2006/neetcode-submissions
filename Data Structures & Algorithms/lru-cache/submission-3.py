class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.nxt = None
        self.prev = None
    
class LRUCache:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.nxt = self.right
        self.right.prev = self.left

    def remove(self, add: Node):
        add.nxt.prev = add.prev
        add.prev.nxt = add.nxt

    def add(self, add: Node):
        
        self.right.prev.nxt = add
        add.prev = self.right.prev
        add.nxt = self.right
        self.right.prev = add
        

    def get(self, key: int) -> int:
        
        if key in self.cache:
            get = self.cache[key]
            self.remove(get)
            self.add(get)

            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            put = self.cache[key]
            self.remove(put)
            self.add(put)

            self.cache[key].value = value

        else:
            add = Node(key, value)
            self.cache[key] = add
            self.add(add)

        if len(self.cache) > self.cap:
            lru = self.left.nxt

            self.cache.pop(lru.key)
            self.remove(lru)

            



        
        
