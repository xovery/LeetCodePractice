class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        richman = 0

        for account in accounts:
            current = sum(account)
            richman = max(richman, current)
        return richman


                        


        