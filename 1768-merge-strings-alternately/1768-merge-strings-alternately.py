class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        ptr1 = 0
        ptr2 = 0

        n = min(n1, n2)
        res = ""
        while(ptr1 < n and ptr2 < n):
            res += word1[ptr1] + word2[ptr2]
            ptr1 += 1
            ptr2 += 1

        if(ptr1 < n1):
            res += word1[ptr1 : ]
        
        if(ptr2 < n2):
            res += word2[ptr2 : ]

        return res

