class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        
        for noneOrderStr in strs:
            orderStr = "".join(sorted(noneOrderStr))
            result[orderStr].append(noneOrderStr)
        
        return result.values()
        