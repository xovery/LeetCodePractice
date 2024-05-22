# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None          

        def findMeet(head):

            slowP = fastP =head
            while fastP and fastP.next:               
                slowP = slowP.next
                fastP = fastP.next.next
                if fastP == slowP:
                    return fastP           
            return None
        
        Meet = findMeet(head)

        if Meet == None:
            return None
        
        new = head              
                
        while Meet != new:
            new = new.next
            Meet = Meet.next                                        
        
        return new
                        
        



