# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        queue = collections.deque()
        queue.append((root,0))
        queue_len = 0

        while (queue):
            queue_len = len(queue)            
            left_most_idx = queue[0][1]
            right_most_idx = queue[-1][1]
            max_width = max(max_width, right_most_idx - left_most_idx + 1)

            for _ in range(len(queue)):
                node, index = queue.popleft()
                if node.left:
                    queue.append((node.left, index * 2))
                if node.right:
                    queue.append((node.right, index * 2 + 1))
                    
        return max_width





#another idea in writing            
'''
        map = {}
        num = 0

        def helper(node, layer):

            if not node:
                return
            
            map.append([node.val, layer])

            if node.left:
                helper(node, layer - 1)
            if node.right:
                helper(node, layer + 1)
        
        helper(root, 1)
        maxWidth = 1

        for i in range(len(map)):
            min = min(map(i))
            max = max(map(i))
            width = max - min

            if width > maxWidth:
                maxWidth = width
        
        return maxWidth
'''


