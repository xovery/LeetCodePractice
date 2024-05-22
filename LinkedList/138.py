"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        
        lookup = {None:None}
        curr = head

        while curr:
            copyNode = Node(curr.val)
            lookup[curr] = copyNode
            curr = curr.next        
        
        curr = head

        while curr:
            copyNode = lookup[curr]
            copyNode.next = lookup[curr.next]
            copyNode.random = lookup[curr.random]
            curr = curr.next

        return lookup[head]

        