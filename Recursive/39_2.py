class Solution:

    def printCombination(self, candidates: List[int], target: int, currList):

        if (sum(currList) == target):
            currList = sorted(currList)
            if currList not in self.output:
                self.output.append(currList[:])
            return
        elif (sum(currList) > target):
            return
        

        
        for num in candidates:
        #for i in range(index, len(candidates))
        #    if num in currList:
        #        continue
            
            currList.append(num)
            self.printCombination(candidates, target, currList)
            currList.pop()


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.output = []
        self.printCombination(candidates, target, [])

        return self.output
        