# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def helper (node, currMax):
            nonlocal goodNode
            if node.val >= currMax:
                goodNode += 1
                currMax = node.val
            if node.left:
                helper(node.left, currMax)
            if node.right:
                helper(node.right, currMax)
        
        goodNode = 0
        helper(root, float('-inf'))

        return goodNode

        
            

                


