# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []

        def buildGraph(node, parent):
            if not node:
                return
            if parent:
                self.graph[node].append(parent)
            if node.left:
                self.graph[node].append(node.left)
                buildGraph(node.left,node)
            if node.right:
                self.graph[node].append(node.right)
                buildGraph(node.right,node)

        self.graph = defaultdict(list)
        buildGraph(root, None)
        seen = set()
        res = []
        queue = collections.deque()
        queue.append([target, 0])

        while queue:
            node, level = queue.popleft()

            if node in seen:
                continue
            seen.add(node)

            if level == k:
                res.append(node.val)
            else:
                for connected in self.graph[node]:
                    queue.append([connected, level+1])

        return res


                


            


        


        