class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        maxRepeat = 0
        start = 0
        lookup = {}

        for end in range(len(s)):
            lookup[s[end]] = lookup.get(s[end], 0) + 1
            maxRepeat = max(maxRepeat, lookup[s[end]])

            if(end-start+1-maxRepeat) > k:
                lookup[s[start]] -= 1
                start += 1
            
            maxLength = max(maxLength, end-start+1)
        
        return maxLength





