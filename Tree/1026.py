# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        result = 0

        def helperDiff(node, currMin, currMax):
            nonlocal result 

            if not node:
                return 0

            result = max(result, abs(currMax-node.val), abs(currMin-node.val))
            currMax = max(currMax, node.val)
            currMin = min(currMin, node.val)

            helperDiff(node.left, currMin, currMax)
            helperDiff(node.right, currMin, currMax)

        helperDiff(root, root.val, root.val)

        return result



        

    

        


        



        