# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#solution with deque
#TC nlog(n)
#SC n
'''        queue = collections.deque()

        for i in range(len(lists)):
            node = lists[i]
            while node:
                queue.append(node.val)
                node = node.next
        
        queue = collections.deque(sorted(queue))
        result = ListNode(-1)
        dummy_head = result

        for i in range(len(queue)):
            val = queue.popleft()
            node = ListNode(val)
            node.next = None
            dummy_head.next = node
            dummy_head = node

        return result.next
'''


        