class Solution:
    def maximumSwap(self, num: int) -> int:
        hashMap = {}
        numList = list(str(num))


        for idx, number in enumerate(numList):
            hashMap[number] = idx
        
        for idx, number in enumerate(numList):
            for digits in range (9, int(number), -1):
                digit_str = str(digits)

                if digit_str in hashMap and hashMap[digit_str] > idx:
                    numList[idx], numList[hashMap[digit_str]] = numList[hashMap[digit_str]], numList[idx]
                    return int("".join(numList))
                
        return num

        

        