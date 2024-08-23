class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        frequencymap = Counter(nums)
        nums.sort(key = lambda x:(frequencymap[x], -x))
        #TC O(nlogn)
        #SC O(1)

        return nums
'''        
        frequencymap = {}
        
        for i in range(len(nums)):
            frequencymap[nums[i]] = frequencymap.get(nums[i], 0) + 1
        
        #frequencymap = sorted(frequencymap)

        frequencymap_sorted = sorted(frequencymap.items(), key = lambda x:(x[1], -x[0]))

        result = []

        for key, count in frequencymap_sorted:
            for i in range(count):
                result.append(key)
        
        return result
'''



        