class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        s = list(secret)
        g = list(guess)

        i = 0

        while(i < len(s)):
            if s[i] == g[i]:
                bulls += 1
                s.pop(i)
                g.pop(i)
            else:
                i += 1

        gMap = {}
        for num in g:
            gMap[num] = 1 + gMap.get(num, 0)

        for num in s:
            if num in gMap and gMap[num] > 0:
                cows += 1
                gMap[num] -= 1
        
        return "{}A{}B".format(bulls, cows)