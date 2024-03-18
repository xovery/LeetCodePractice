class Solution:
    def leftRowColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
    rowLength, colLentigh = binaryMatrix.dimensions()
    rol, col = 0, colLentigh-1
    leftMost = -1
    
    while row < rowLength and col > 0
        if binaryMatrix.get(row, col) == 1
            leftMost = col
            col -= 1
        else
            rol += 1
    
    return leftMost