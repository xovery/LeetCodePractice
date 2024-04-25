# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        self.result = 0
        if not root:
            return result
        
        #DFS
        def SumHelper(node):
            if node != None:
                if node.val >= low and node.val <= high:
                    self.result += node.val
                if node.val > low :
                    SumHelper(node.left)                    
                if node.val < high :
                    SumHelper(node.right)


        SumHelper(root)      

        return self.result
        
            


        