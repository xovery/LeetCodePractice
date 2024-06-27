class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxFruits = 0
        currFruits = 0
        basket = {}
        start = 0
        
        for end in range(len(fruits)):
            currFruits += 1
            basket[fruits[end]] = basket.get(fruits[end], 0) + 1

            while len(basket) > 2:
                currFruits -= 1
                basket[fruits[start]] -= 1

                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]
                
                start += 1
        
            maxFruits = max(maxFruits, currFruits)
        return maxFruits
            





        