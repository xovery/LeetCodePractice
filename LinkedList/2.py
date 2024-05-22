# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if not l1:
            return l2
        if not l2:
            return l1

        init = ListNode(-1)
        head = init
        carry = 0
        while l1 and l2:            
                head.next = ListNode((l1.val + l2.val + carry) % 10)
                carry = (l1.val + l2.val + carry) // 10
                l1 = l1.next
                l2 = l2.next
                head = head.next

        while l1:
                head.next = ListNode((l1.val + carry) % 10)
                carry = (l1.val + carry) // 10
                l1 = l1.next
                head = head.next        
        
        while l2:
                head.next = ListNode((l2.val + carry) % 10)
                carry = (l2.val + carry) // 10
                l2 = l2.next
                head = head.next      

        if carry:
            head.next = ListNode(carry)  
        
        return init.next

                        



        