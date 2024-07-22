class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        
        result = []

        def palindromicCheck(left, right, s):
            nonlocal count
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count +=1
                result.append(s[left:right+1])
                left -= 1
                right += 1
                

        for i in range(len(s)):
            palindromicCheck(i, i, s)
            if(i+1 < len(s) and s[i] == s[i+1]):
                palindromicCheck(i, i+1, s)
        
        print(result)
        return count

        #TC O(N^2) where N == length of string
        #SC O(1) 


