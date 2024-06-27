class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        
        #hashmap
        left = 0
        lookup = {}
        for right in range(len(s)):
            if s[right] in lookup:                
                #prevent left is less then previous 
                left = max(left, lookup[s[right]] + 1)                
            lookup[s[right]] = right
            maxLen = max(maxLen, right - left + 1)
        return maxLen

        #deque        
        #maxLen = 0
        res = collections.deque()

        for end in range(len(s)):        
            while s[end] in res:
                res.popleft()
            
            res.append(s[end])

            maxLen = max(maxLen, len(res))
        
        return maxLen





            
            
        
        return maxLen
        