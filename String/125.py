class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s:
            return true

        left = 0
        right = len(s)-1
        s = s.lower()

        valid_string = "abcdefghijklmnopqrstuvwxyz1234567890"
        
        while left < right:
            while left < right and s[left] not in valid_string:
                left += 1
            while left < right and s[right] not in valid_string:
                right -= 1

            
            if s[right] != s[left]:
                return False

            left += 1
            right -= 1
        
        return True