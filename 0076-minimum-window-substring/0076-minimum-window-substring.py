class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        tMap = {}
        for char in t:
            tMap[char] = 1 + tMap.get(char, 0)

        need = len(tMap)
        have = 0

        windowMap = {}
        res = [-1, -1]
        resLen = float("inf")

        left = 0
        for right in range(0, len(s)):
            windowMap[s[right]] = 1 + windowMap.get(s[right], 0)
            if s[right] in tMap and windowMap[s[right]] == tMap[s[right]]:
                have += 1
            while have == need:
                # Update res if required
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = (right - left + 1)
                # Shrink window if possible
                windowMap[s[left]] -= 1
                if s[left] in tMap and windowMap[s[left]] < tMap[s[left]]:
                    have -= 1
                left += 1
        
        left, right = res
        return s[left : right + 1] if resLen != float("inf") else ""