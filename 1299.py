class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxSee = 0
        curMax = arr[-1]
        arr[-1] = -1

        for i in range(len(arr)-2, -1, -1):
            maxSee = max(arr[i], curMax)            
            arr[i] = curMax
            curMax = maxSee
        
        return arr
                
        #TC = O(n)
        #SC = O(1)
