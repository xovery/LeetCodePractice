# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def appendT(self, root:Optional[TreeNode]):

        if root:
            self.appendT(root.left)
            heapq.heappush(self.heap, root.val)
            self.appendT(root.right)



    def __init__(self, root: Optional[TreeNode]):  
        self.stack = []              
        self.heap = []
        if root:                                    
            self.appendT(root.left)
            heapq.heappush(self.heap, root.val)
            self.appendT(root.right)
    

    def next(self) -> int:
       
        if len(self.heap) > 0:
            return heapq.heappop(self.heap)
        return 0
        
        
    def hasNext(self) -> bool:
        return len(self.heap) > 0
        



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()