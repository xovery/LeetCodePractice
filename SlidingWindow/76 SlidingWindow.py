class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #edge checking

        lookup = {}
        start = 0
        finalStart = 0
        matched = 0
        minLen = len(s) + 1
        

        for char in t:
            lookup[char] = lookup.get(char, 0) + 1
        
        for end in range(len(s)):
            endChar = s[end]
            if endChar in lookup:
                lookup[endChar] -= 1
            
                if lookup[endChar] >= 0:
                    matched += 1
            
            while matched == len(t):
                if minLen > end - start + 1:
                    minLen = end - start + 1
                    finalStart = start

                lefChar = s[start]
                if lefChar in lookup:
                    if lookup[lefChar] == 0:
                        matched -= 1
                    lookup[lefChar] += 1
                start += 1
        
        if minLen > len(s):
            return ""

        return s[finalStart:finalStart+minLen]
        



        