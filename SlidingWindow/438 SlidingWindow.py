class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        windowSize = len(p)
        start = 0        
        output = []
        lookup = {}
        matched = 0

        #TC O(n) 
        #SC O(n)
        for char in p:
            lookup[char] = lookup.get(char, 0) + 1 

        for end in range(len(s)):
            right = s[end]

            if right in lookup:
                lookup[right] -=1

                if lookup[right] == 0:
                    matched += 1

            if matched == len(lookup):
                output.append(start)

            if end >= windowSize - 1:
                left = s[start]

                if left in lookup:
                    if lookup[left] == 0:
                        matched -= 1

                    lookup[left] += 1
                
                start += 1
            
        return output
        
        '''
        #TC = O(nlogn)
        #SC = O(n)
        currStr = collections.deque()
        temp2 = sorted(p)
        for end in range(len(s)):

            currStr.append(s[end])

            while len(currStr) > windowSize:
                currStr.popleft()
                start += 1

            if (end-start+1) == windowSize:
                temp1 = sorted(currStr)
                                
                if temp1 == temp2:
                    output.append(start)
            
        return output
        '''


            
