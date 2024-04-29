# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

#recursive
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def printNode(root):
            if root:
                result.append(root.val)
                printNode(root.left)
                printNode(root.right)
                
        printNode(root)
        
        return result



        

#iterative
'''
        result = []
        stack = []
        stack.append(root)

        #LIFO
        while stack:
            node = stack.pop()
            
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)                
        return result   
'''



        