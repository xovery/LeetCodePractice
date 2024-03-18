class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                prevAsteroid = stack.pop()

                if prevAsteroid > -asteroid:
                    asteroid = prevAsteroid
                elif prevAsteroid == -asteroid:
                    asteroid = 0

            if asteroid != 0:
                stack.append(asteroid)
        
        return stack