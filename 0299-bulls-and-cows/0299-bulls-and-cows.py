class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        s = list(secret)
        g = list(guess)

        i = 0
        j = 0

        while(j < len(s)):
            if s[j] == g[j]:
                bulls += 1
                s.pop(j)
                g.pop(j)
            else:
                j += 1
            i += 1
            print(bulls)

        sMap = {}
        for num in s:
            sMap[num] = 1 + sMap.get(num, 0)

        for num in g:
            if num in sMap and sMap[num] > 0:
                cows += 1
                sMap[num] -= 1
        
        return "{}A{}B".format(bulls, cows)