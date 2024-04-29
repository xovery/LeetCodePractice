# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        queue = collections.deque()
        queue.append(root)
        queue_len = 0
        Sum = 0

        while queue:
            queue_len = len(queue)                            
            Sum = 0
            for i in range(queue_len):
                node = queue.popleft()
                if node:
                    Sum += node.val            
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        
        return Sum

            

        