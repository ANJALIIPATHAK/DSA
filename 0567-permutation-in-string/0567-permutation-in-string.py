class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        if(m > n):
            return False
        sorteds1 = sorted(s1)
        for i in range(0, n-m+1):
            if(sorted(s2[i : i + m]) == sorteds1):
                return True
        return False
