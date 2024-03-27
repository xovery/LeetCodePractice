# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        #edge check
        if not root:
            return result

        
        columnTable = defaultdict(list)

        #deque for BFS
        queue = collections.deque()
        queue.append((root, 0, 0))

        #BFS algorithm
        while queue:
            node, row, col = queue.popleft()
            if node:
                columnTable[col].append((row, node.val))
                queue.append((node.left, row+1, col-1))
                queue.append((node.right, row+1, col+1))
             
        #sorted col
        for key in sorted(columnTable):
            temp = []

            #sorted row 
            for row, nodeValue in sorted(columnTable[key]):
                temp.append(nodeValue)
            result.append(temp)

        return result


        