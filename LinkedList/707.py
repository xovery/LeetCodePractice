class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        
        result = self.head
        for _ in range(index+1):
            result = result.next
        
        return result.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        result = self.head
        node = ListNode(val)

        for _ in range(self.length):
            result = result.next
        
        result.next = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:

        if index > self.length:
            return
        
        result = self.head
        node = ListNode(val)

        for _ in range(index):
            result = result.next
        
        if result:
            node.next = result.next
            result.next = node
            self.length += 1
        

    def deleteAtIndex(self, index: int) -> None:

        if index < 0 or index >= self.length:
            return
        result = self.head

        for _ in range(index):
            result = result.next        

        result.next = result.next.next
        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)