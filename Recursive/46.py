class Solution:

    def printList(self, nums, currList):

            if len(nums) == len(currList):
                self.output.append(currList[:])
                return
            
            for num in nums:
                if num in currList:
                    continue
                
                currList.append(num)
                self.printList(nums, currList)
                currList.pop()
  
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        self.printList(nums, [])

        return self.output