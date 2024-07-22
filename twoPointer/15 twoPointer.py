class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # TC = O(n^2)
        # SC = O(n)
        res = []
        length = len(nums)
        nums.sort()

        for pointIdx in range(length-2):
            if pointIdx > 0 and nums[pointIdx] == nums[pointIdx-1]:
                continue

            pointLeft = pointIdx+1
            pointRight = length -1

            while pointLeft < pointRight:
                sum = nums[pointIdx] + nums[pointLeft] + nums[pointRight]

                if sum < 0:
                    pointLeft += 1
                elif sum > 0:
                    pointRight -= 1
                else:
                    res.append([nums[pointIdx], nums[pointLeft], nums[pointRight]])

                    while pointLeft < pointRight and nums[pointLeft] == nums[pointLeft+1]:
                        pointLeft +=1
                    while pointLeft < pointRight and nums[pointRight] == nums[pointRight-1]:
                        pointRight -=1
                    pointLeft +=1
                    pointRight -=1
            
        return res
                


            
        