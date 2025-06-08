class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        sMap = {}
        tMap = {}

        for char in s:
            sMap[char] = 1 + sMap.get(char, 0)

        for char in t:
            tMap[char] = 1 + tMap.get(char, 0)

        return (sMap == tMap)