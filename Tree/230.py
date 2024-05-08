# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        res = 0
        def RecursiveHelper(node):
            nonlocal res, k

            if not node:
                return
                    
            RecursiveHelper(node.left)
            
            k -= 1
            if k == 0:
                res = node.val
                        
            RecursiveHelper(node.right)

        RecursiveHelper(root)
        return res