# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def HelperLCA(node, p1, p2):
            if not node:
                return
            
            if node.val == p1 or node.val==p2:
                return node
            
            left = HelperLCA(node.left, p1, p2)
            right = HelperLCA(node.right, p1, p2)

            if left and right:
                return node
            if left:
                return left
            if right:
                return right

        lca = HelperLCA(root, startValue, destValue)

        queue = collections.deque()
        queue.append((lca, ""))
        pathStart = 0
        pathDest = ""

        while queue:
            node, path = queue.popleft()

            if node.val == startValue:
                pathStart = len(path)
            if node.val == destValue:
                path_dest = path
            if node.left:
                queue.append((node.left, path+"L"))
            if node.right:
                queue.append((node.right, path+"R"))
            
        result = "U"*pathStart + path_dest

        return result
            

        

        