class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0 or len(words[0])== 0:
            return []
        
        lookup = {}

        for word in words:
            lookup[word] = lookup.get(word, 0) + 1
            
        result = []
        wordLength = len(words[0])
        wordCount = len(words)   

        for i in range((len(s)-wordLength*wordCount)+1):
            lookup2 = {}
            for j in range(0, wordCount):
                nextWordIndex = i + j * wordLength
                word = s[nextWordIndex: nextWordIndex + wordLength]

                if word not in lookup:
                    break
                
                lookup2[word] = lookup2.get(word, 0) + 1

                if lookup2[word] > lookup[word]:
                    break
                
                if j + 1 == wordCount:
                    result.append(i)

        return result

        