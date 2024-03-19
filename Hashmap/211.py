class WordDictionary:

    def __init__(self):
        self.lookup = {}
        

    def addWord(self, word: str) -> None:
        length = len(word)

        if length not in self.lookup:
            self.lookup[length] = [word]
        else:
            self.lookup[length].append(word)

    def search(self, word: str) -> bool:
        length = len(word)

        if length not in self.lookup:
            return False

        arr = self.lookup[length]

        if word in arr:
            return True
        
        for item in self.lookup[length]:
            match = False

            for i in range(length):
                if word[i] == item[i] or word[i] == ".":
                    match = True
                else:
                    match = False
                    break;
            if match:
                return True

        return match

        

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)