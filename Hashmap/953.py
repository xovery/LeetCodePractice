class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lookup = {}

        for idx, char in enumerate(order):
            lookup[char] = idx
        
        for word1, word2 in zip(words, words[1:]):
            if len(word1) > len(word2) and word1[:len(word2)] == word2:
                return False
            
            for char1, char2 in zip(word1, word2):
                if lookup[char1] > lookup[char2]:
                    return False
                elif lookup[char1] < lookup[char2]:
                    break
            
        return True

        #SC O(n)
        #TC O(mxn)

        