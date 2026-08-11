class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderArr = []
        for char in order:
            orderArr.append(char)
        
        sMap = Counter(s)

        res = ""
        for char in orderArr:
            if char in sMap:
                count = sMap[char]
                res += char * count
                del sMap[char]

        for char, count in sMap.items():
            res += char * count
        
        return res

