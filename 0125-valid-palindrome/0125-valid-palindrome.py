class Solution:
    def isPalindrome(self, s: str) -> bool:
        def helper(start, end):
            if(start >= end):
                return True
            if(cleanS[start] != cleanS[end]):
                return False
            return helper(start + 1, end - 1)
        cleanS = ""
        for char in s:
            if(char.isalnum()):
                cleanS += char.lower()
        print(cleanS)
        
        return helper(0, len(cleanS)-1)
