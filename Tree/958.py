# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return rue
        
        queue = collections.deque()

        queue.append(root)
        bCheck = False

        while queue:
            node = queue.popleft()    
            
            if not node:                
                bCheck = True
                continue

            if bCheck:
                return False
            
            queue.append(node.left)
            queue.append(node.right)

        return True

