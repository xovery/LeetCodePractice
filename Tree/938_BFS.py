# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        if not root:
            return result
        
        queue = collections.deque()
        queue_size = 0
        queue.append(root)

        sum = 0

        while queue:
            queue_len = len(queue)
            for i in range(queue_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if node.val >= low and node.val <= high:
                    result += node.val
            
        return result