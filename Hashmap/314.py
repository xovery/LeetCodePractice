#class TreeNode:
#   def __init__(self, val=0, left=None, right=None)
#   self.val = val
#   self.left = left
#   self.right = right

class Solution:
    def verticalOrder(self, root:Optional([TreeNode])->List[List[int]]:
        if not root
            return []

        queue = collections.dequre()
        queue.append((root,0))
        lookup = collections.defaultdict(list)
        res = {}

        while queue:            
            node, column = queue.popleft()
            lookup[column].append(node.val)

            if node.left:
                queue.append((node.left, column-1))
            if node.right:
                queue.append((node.right, column+1))

        left = min(lookup.keys())
        right = max(lookup.keys())

        for i in range(left, right+1)
            res.append(lookup[i])

        return res

        

        
