class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        
        res = 0
        i = 0
        j = 0
        players.sort()
        trainers.sort()
        while j < len(trainers) and i < len(players):
            if (players[i] <= trainers[j]):
                i+=1
                res+=1
            j+=1

        return res
        #TC nlogn

        