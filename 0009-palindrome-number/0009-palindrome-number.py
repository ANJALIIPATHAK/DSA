class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        
        reversedNum = 0
        originalNum = x
        while(x > 0):
            lastDigit = x % 10
            reversedNum = (reversedNum * 10) + lastDigit
            x = x // 10
        print(reversedNum)
        return (reversedNum == originalNum)