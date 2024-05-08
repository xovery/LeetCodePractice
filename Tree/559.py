"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        queue = collections.deque()
        queue.append(root)
        size = 0
        stack = []

        while queue:
            size += 1
            for i in range(len(queue)):
                n = queue.popleft()                                    
                if (len(n.children) > 0):
                    for i in range(len(n.children)):
                        queue.append(n.children[i])                        


        return size

        