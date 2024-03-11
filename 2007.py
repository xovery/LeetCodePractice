class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2 == 1:
            return []
        
        lookup = defaultdict(int)
        for num in changed:
            lookup[num] = lookup.get(num, 0) + 1

            result = []
        
        for num in sorted(changed):
            if lookup[num] == 0:
                continue
            elif lookup[num+num] == 0:
                return []

            lookup[num] -= 1
            lookup[num+num] -=1

            result.append(num)

        return result

                        


        