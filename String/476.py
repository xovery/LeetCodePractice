class Solution:
    def findComplement(self, num: int) -> int:
        binaryString = bin(num)[2:]        
        flipString = "".join(['0' if bit == '1' else '1' for bit in binaryString])                
        result = int(flipString, 2)

        return result
        