class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        if k < arr[0]:
            return k

        arrSet = set(arr)
        i = 1

        while i <= arr[len(arr)-1]:
            if i not in arrSet:
                k -= 1
            if k == 0:
                return i

            i += 1

        while k > 1:
            i +=1
            k -=1

        return i


