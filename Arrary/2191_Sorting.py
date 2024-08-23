class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
#method 2
        def Jumbled(num):
            
            numStr = str(num)
            mapStr = ''.join(str(mapping[int(digit)]) for digit in str(numStr))
            
            return int(mapStr)

        hashtable2 = {}

        for num in nums:
            hashtable2[num] = Jumbled(num)

        sorted_nums = sorted(nums, key=hashtable2.get)
        
        return sorted_nums

#method 1
        #create the hashtable and mapping the num via the hashtable 
        hashtable = {}
        for num in nums:
            hashtable[num] = int(''.join(str(mapping[int(digit)]) for digit in str(num)))

        print(hashtable)
            
        return sorted(nums, key = hashtable.get)

        

        