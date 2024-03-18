from typing import List

class Solution:
    def groupSetting(self, strings: List(str)) -> List[List(str)]:
    
        output = collections.defaultdict(list)
    
        for string in strings:
            shiftSeq = ()        
            for char in string:
                shiftSeq += (ord(char)-ord[0])%26,
            output[shiftSeq].append(string)
        
        return output.values
           

        


