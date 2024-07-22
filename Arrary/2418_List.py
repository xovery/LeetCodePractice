class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

#method2. TC = O(nlogn)
        combined = list(zip(names, heights))
        combined.sort(key = lambda x:x[1], reverse = True)
        resultInOrder = [name for name, height in combined]
        return resultInOrder

#method1. TC = O(nlogn)
        hashmap = dict(zip(heights, names))
        result = []

        heights.sort(reverse = True)

        for i in range(len(heights)):
            result.append(hashmap[heights[i]])
        
        return result
        