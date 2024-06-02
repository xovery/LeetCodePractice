class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointA = 0
        pointB = len(numbers)-1
        
        #TC = n
        #method 1
        while pointA < pointB:
            if (numbers[pointA]+numbers[pointB]) == target:
                res.append(pointA+1)
                res.append(pointB+1)
                return [pointA+1, pointB+1] 
            elif (numbers[pointA]+numbers[pointB]) > target:
                pointB -= 1
            else:
                pointA += 1 

        return res
        #method 2
        #TC n*n
        for i in range(len(numbers)):
            check = target - numbers[i]
            if check in numbers:            
                for j in range(len(numbers)):
                    if numbers[j] == check and i != j:
                        return [i+1, j+1]
            

        return []

        