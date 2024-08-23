class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance = [[float('inf')]*n for _ in range(n)]

        for i in range(n):
            distance[i][i] = 0

        for i, j, dis in edges:
            distance[i][j] = dis
            distance[j][i] = dis
        
        for k in range(n):        
            for i in range(n):
                for j in range(n):
                    if distance[i][j] > distance[i][k] + distance[k][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]

        minReach = float('inf')
        city = -1

        for i in range(n):
            reachCity = sum(1 for j in range(n) if distance[i][j] <= distanceThreshold)
            print("i:", i, "reach:", reachCity)
            if reachCity < minReach or (minReach == reachCity and i > city):
                city = i 
                minReach = reachCity
        

        return city
                

        