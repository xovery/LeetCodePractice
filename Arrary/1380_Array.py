class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
      
        result = []
        for row in range(len(matrix)):
            
            #find the min value of each row 
            rowMin = min(matrix[row])
            #determin the col Num
            colIndex = matrix[row].index(rowMin)
            
            #initl the colMax with first row
            colMax = matrix[0][colIndex]
            #find the max colMax in the colIndex.
            for row2 in range(len(matrix)):
                colMax = max(colMax, matrix[row2][colIndex])

            if rowMin == colMax:
                result.append(rowMin)    
    

        return result
