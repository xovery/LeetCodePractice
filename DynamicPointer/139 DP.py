class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        checkTable = [False] * (len(s) + 1)

        checkTable[0] = True

        for i in range(len(s)):
            if checkTable[i] == True:
                for word in wordDict:
                    if s[i:i+len(word)] == word:
                        checkTable[i+len(word)] = True 
        
        return checkTable[-1]