# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        forest = []
        def dfsHelper(node, is_root) -> TreeNode:
            if not node:
                return
            
            deleteRoot = node.val in to_delete

            if is_root and not deleteRoot:
                forest.append(node) 

            node.left = dfsHelper(node.left, deleteRoot)
            node.right = dfsHelper(node.right, deleteRoot)

            return None if deleteRoot else node

        #dfsHelper(root, True)
        #return forest

        if not root:
            return

        queue = collections.deque()
        queue.append(root)
        result = []
        prev = None

        def dfsHelper(node, prev, to_delete):

            if node == None:
                return

            if node.val in to_delete:
                if  prev.left and prev.left.val == node.val:                    
                    prev.left = None
                else:
                    prev.right = None
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                dfsHelper(node.left, node, to_delete)
                dfsHelper(node.right, node, to_delete)

        while queue:
            node = queue.popleft()            
            if node.val not in to_delete:
                result.append(node)
                dfsHelper(node.left, node, to_delete)
                dfsHelper(node.right, node, to_delete)
            else:                                                        
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result





        
