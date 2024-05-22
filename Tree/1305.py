# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        
        queue1 = collections.deque()
        queue2 = collections.deque()

        res1 = []
        res2 = []

        def helper(node, res):
            if not node:
                return
                      
            helper(node.left, res)            
            res.append(node.val)         
            helper(node.right, res)

        helper(root1, queue1)
        helper(root2, queue2)

        final = []

        while queue1 and queue2:
            if queue1[0] <= queue2[0]:
                final.append(queue1.popleft())
            else:
                final.append(queue2.popleft())
        
        if queue1:
            final.extend(queue1)
        if queue2:
            final.extend(queue2)            
        
        return final

        #TC O(n)

'''
        stack = []
        queue = collections.deque()

        def helper(rootNode):
            nonlocal stack
            if not rootNode:
                return
            
            queue.append(rootNode)
            queueLen = 0
            while queue:
                queueLen = len(queue)
                for i in range(queueLen):
                    node = queue.popleft()
                    stack.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)           

        helper(root1)
        helper(root2)
                
        stack = sorted(stack)

        return stack

        TC O(nlogn)
'''        