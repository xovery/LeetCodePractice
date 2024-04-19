class Solution:

    def printCombination(self, candidates: List[int], target: int, currList, index):

        if (target == 0):
            self.output.append(currList[:])
            return
        elif (target < 0):
            return
        
        for i in range(index, len(candidates)):
            currList.append(candidates[i])
            self.printCombination(candidates, target-candidates[i], currList, i)
            currList.pop()


    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        self.output = []
        self.printCombination(candidates, target, [], 0)

        return self.output
        