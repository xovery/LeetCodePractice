class Solution:


    def addOperators(self, num: str, target: int) -> List[str]:
        if num == "":
            return []

        res = []

        def backtrack(currIdx, currPath, currRes, prevNum):
            if currIdx == len(num):
                if currRes == target:
                    res.append(currPath)
                return

            for i in range(currIdx, len(num)):
                # the number can combine but ignore the 0X number 
                if i > currIdx and num[currIdx] == "0":
                    break

                #the currNumStr could be large then 1 digit.
                currNumStr = num[currIdx:i+1]
                currNum = int(currNumStr)

                if currIdx == 0:
                    backtrack(i+1, currNumStr, currNum, currNum)
                else:
                    backtrack(i+1, currPath + "+" + currNumStr, currRes+currNum, currNum)
                    backtrack(i+1, currPath + "-" + currNumStr, currRes-currNum, -currNum)
                    backtrack(i+1, currPath + "*" + currNumStr, currRes-prevNum+prevNum*currNum, prevNum*currNum )



        backtrack(0, "", 0, 0)

        return res