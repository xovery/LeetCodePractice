class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:

        n = len(books)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            current_width = 0
            max_height = 0
            print("New {}".format(i))
            for j in range(i - 1, -1, -1):
                print("{}".format(j))
                current_width += books[j][0]
                if current_width > shelfWidth:
                    print("break")
                    break
                print("maxheight={}, books[{}][1]={}".format(max_height, j,books[j][1]))
                max_height = max(max_height, books[j][1])
                print("maxheight={}".format(max_height))
                print("dp[{}]={}, dp[{}]={} + max_height".format(i,dp[i], j, dp[j]))
                dp[i] = min(dp[i], dp[j] + max_height)
                print("dp[{}]={}".format(i, dp[i]))
        print(dp)
        return dp[n]

'''
        totalHeight = 0
        currWidth = 0
        currMaxHeight = - math.inf   
            
        print(books)
        for width, height in books:
            print("currWidth:", currWidth)
            if (currWidth + width <= shelfWidth):
                currMaxHeight = max(currMaxHeight, height)
                currWidth += width                
                print("currMaxHeight:", currMaxHeight, "currWidth:", currWidth)
            else:
                currWidth = width
                totalHeight += currMaxHeight
                currMaxHeight = height                
                print("currMaxHeight:", currMaxHeight, "totalHeight:", totalHeight)

        if (currMaxHeight != -math.inf):
            totalHeight += currMaxHeight

        return totalHeight
'''                



        

        