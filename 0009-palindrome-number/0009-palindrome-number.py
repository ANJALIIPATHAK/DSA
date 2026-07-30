class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x != 0 and x % 10 == 0:
            return False

        reversedHalf = 0

        while(x > reversedHalf):
            lastDigit = x % 10
            reversedHalf= reversedHalf * 10 + lastDigit
            x = x // 10
        
        return x == reversedHalf or x == reversedHalf // 10