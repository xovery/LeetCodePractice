# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        countGood = 0
        def dfsHelper( node):   
            nonlocal countGood         
            if not node:
                return []
            if not node.left and not node.right:
                return [1]  # Leaf node with distance 1
            
            left_distances = dfsHelper(node.left)
            right_distances = dfsHelper(node.right)

            for ld in left_distances:
                for rd in right_distances:
                    if ld + rd <= distance:
                        countGood += 1

            # Prepare distances for the parent node
            new_distances = []
            for d in left_distances + right_distances:
                if d + 1 < distance:
                    new_distances.append(d + 1)      
            return new_distances  
        
        dfsHelper(root)
        return countGood

