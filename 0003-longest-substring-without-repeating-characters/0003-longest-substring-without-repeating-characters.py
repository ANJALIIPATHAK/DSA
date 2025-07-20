class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        for i in range(0, len(s)):
            charSet = set()
            subStr = ""
            for j in range(i, len(s)):
                if(s[j] not in charSet):
                    subStr += s[j]
                    charSet.add(s[j])
                else:
                    break
            maxLength = max(maxLength, len(subStr))
        return maxLength
