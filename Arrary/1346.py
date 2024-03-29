class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        #seen = []

        for num in arr:
            if num * 2 in seen or num / 2 in seen:
                return True
            else:
                seen.add(num)
                #seen.apend

        return False

        #TC = O(N)
        #/SC = O(N)