# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        temp = TreeNode(-1)
        curr = temp
        stack = []
        stack.append(root)


        while stack:
            node = stack.pop()
            curr.left = None
            curr.right = node
            curr = node

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        root = temp.right
                


                    
        return
        