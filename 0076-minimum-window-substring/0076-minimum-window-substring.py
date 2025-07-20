class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(t == ""):
            return ""
        
        countT = {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        need = len(countT)
        
        countWindow = {}

        have = 0
        left = 0
        res = [-1, -1]
        resLen = float("inf")
        for right in range(0, len(s)):
            countWindow[s[right]] = 1 + countWindow.get(s[right], 0)
            if(s[right] in countT and countWindow[s[right]] == countT[s[right]]):
                have += 1
            while(have == need):
                if(resLen > right - left + 1):
                    res = [left, right]
                    resLen = right - left + 1
                countWindow[s[left]] -= 1
                if(s[left] in countT and countWindow[s[left]] < countT[s[left]]):
                    have -= 1
                left += 1
        left = res[0]
        right = res[1]
        if(resLen != float("inf")):
            return s[left : right + 1]
        else:
            return ""
                
