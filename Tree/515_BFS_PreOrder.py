# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []

        #BST, PreOrder

        queue = collections.deque()
        queue_size = 0
        queue.append(root)

        while queue:
            queue_len = len(queue)
            temp = []
            for i in range(queue_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                temp.append(node.val)
            
            res.append(max(temp)) 
            
        return res 
        