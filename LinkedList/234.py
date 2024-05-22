# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def reverseList(head:ListNode) -> ListNode:
            prev = None
            while head:
                next_node = head.next
                head.next = prev
                prev = head
                head = next_node
            return prev

        if not head:
            return False

        fast = slow = head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        firstHalf = slow
        secondHalf = reverseList(firstHalf)

        while head and secondHalf:
            if head.val != secondHalf.val:
                return False
            head = head.next
            secondHalf = secondHalf.next
        
        return True

# common method 2
        if not head:
            return False

        fast = slow = head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        #if slow at center, slow = slow.next
        if fast:
            slow = slow.next

        while slow:
            if stack.pop() != slow.val:
                return False
            slow = slow.next
        
        return True

# common method 1
# TC 2n
# SC 2n
        if not head:
            return False
        
        stack = []
        queue = collections.deque()

        while head:
            stack.append(head.val)
            queue.append(head.val)
            head = head.next
        
        for i in range(len(stack)):
            if stack.pop() != queue.popleft():
                return False
        
        return True

         
        