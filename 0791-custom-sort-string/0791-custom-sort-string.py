class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderArr = []
        for char in order:
            orderArr.append(char)
        
        sMap = {}
        for char in s:
            sMap[char] = 1 + sMap.get(char, 0)

        res = ""
        for char in orderArr:
            if char in sMap:
                count = sMap[char]
                res += char * count
                del sMap[char]

        for char, count in sMap.items():
            res += char * count
        
        return res

