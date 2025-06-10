class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if(x < 0):
            negative = True
            x = -1 * x

        reversedNum = 0
        while(x > 0):
            lastDigit = x % 10
            if(lastDigit == 0 and reversedNum == 0):
                x = x // 10
                continue
            else:
                reversedNum = (reversedNum * 10) + lastDigit
                x = x // 10
            if(reversedNum >= (2 **31 -1)):
                return 0
        if(negative == True):
            return (-1 * reversedNum)
        else:
            return reversedNum


        