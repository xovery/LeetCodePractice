# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        #DFS

        def dfs(node, path,result):

            if not node:
                return 
            
            path.append(str(node.val))
            print("add+"+str(node.val))

            if not node.left and not node.right:
                result.append("->".join(path))
            else:
                if node.left:
                    dfs(node.left, path, result)
                if node.right:
                    dfs(node.right, path, result)
            print("pop+"+str(node.val))
            path.pop() 
        
        result = []
        dfs(root, [], result)
        return result


        #BFS
        queue = collections.deque()
        mylist = []
        queue.append((root, str(root.val)))
        
        result = []

        while queue:
            
            node, path = queue.popleft()

            if not node.left and not node.right:
                result.append(path)
            else:
                if node.left:
                    queue.append((node.left, path+"->"+str(node.left.val)))
                if node.right:
                    queue.append((node.right, path+"->"+str(node.right.val)))

        return result
        
