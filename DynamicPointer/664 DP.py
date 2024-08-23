class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]    
        return self.helper(0, n-1, s, dp)

    def helper(self, i, j, s, dp) -> int:
        print("i {} j {} call".format(i, j))
        #base case
        if i > j :
            print("i {} j {} exit, answer {}".format(i, j, 0))
            return 0
        elif i == j:
            return 1
        
        #check history
        if dp[i][j] != -1:
            print("i {} j {} exit".format(i, j))
            return dp[i][j]
        
        first_letter = s[i]
        # If the current character is not repeated in the rest of the string        
        answer = 1 + self.helper(i + 1, j, s, dp)
                
        for k in range(i + 1, j + 1):
            # If repeated then update the answer
            if s[k] == first_letter:
                # Splitting from i -> k - 1 (remove the last character)
                # and from k + 1 -> j             
                better_answer = self.helper(i, k - 1, s, dp) + self.helper(k + 1, j, s, dp)                
                answer = min(answer, better_answer)
                print("check better answer, i {}, j {}, k {}, answer {}".format(i, j, k, answer))
        dp[i][j] = answer
        print("i {} j {} exit, answer {}".format(i, j, answer))
        return answer

'''        
        n = len(s)
        #create n * n array
        dp = [[0] * n for _ in range(n)]

        #init the array
        for i in range(n):
            dp[i][i] = 1

        
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                dp[i][j] = dp[i][j-1] + 1
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] - (1 if s[k] == s[j] else 0))
        
        return dp[0][n-1]
'''        