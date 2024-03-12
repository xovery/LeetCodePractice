class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        #hash_map = {word: 1 for word in words}
        hash_map = {}
        max_res = 1
        for word in words:
            hash_map[word] = 1
            for i in range(len(word)):
                new_word = word[:i] + word[i+1:]
                res = hash_map.get(new_word, -math.inf)
                if hash_map[word] < res + 1:
                    hash_map[word] = res + 1
                    max_res = max(max_res, hash_map[word])
        return max_res
