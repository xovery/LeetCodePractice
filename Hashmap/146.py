class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
\
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lookup = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    #when adding the node to last before tail
    def addNode(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node
    
    #remove a node
    def removeNode(self, node):
        prev_node = node.prev
        prev_node.next = node.next
        node.next.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        
        node = self.lookup[key]
        self.removeNode(node)
        self.addNode(node)
        return node.val
            

    def put(self, key: int, value: int) -> None:
        

        if key in self.lookup:
            self.removeNode(self.lookup[key])
        elif self.capacity == len(self.lookup):
            lru = self.head.next
            self.removeNode(lru)
            del self.lookup[lru.key]     
        

        newNode = Node(key, value)
        #add into the double link list
        self.addNode(newNode)
        #add into the hash table
        self.lookup[newNode.key] = newNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)