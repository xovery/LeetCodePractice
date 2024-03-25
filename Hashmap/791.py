class Solution:
    def customSortString(self, order: str, s: str) -> str:
        #lookup = defaultdict(int)
        lookup = {}
        res = []

        for char in s:
            lookup[char] = lookup.get(char, 0) + 1

        for char in order:
            if char in lookup:
                res.append(char * lookup[char])
                del lookup[char]

        for char in lookup:
            res.append(char*lookup[char])


        return "".join(res)


                

        