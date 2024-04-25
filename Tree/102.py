# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        queue = collections.deque()
        queue.append(root)
        queue_len = 0

        #BFS to search the tree
        while queue:
            queue_len = len(queue)
            curr_list = []

            for i in range(queue_len):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                curr_list.append(node.val)
            
            result.append(curr_list)        

        return result
        
        
        